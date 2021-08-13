import requests
import datetime as dt
from flight_data import FlightData

KIWI_ENDPOINT = 'https://tequila-api.kiwi.com'
API_KEY_IATA = 'KmKcLU9zWTccW00ll4OKozQiQZd4sAmL'
API_KEY_FLIGHT = 'bntWTMEzJPR3CuF4tnf_XQpgY8z1ozgS'
header_iata = {
    'apikey': API_KEY_IATA,
}
header_flight = {
    'apikey': API_KEY_FLIGHT,
}


class FlightSearch:

    def get_iata(self, name):
        response = requests.get(f'{KIWI_ENDPOINT}/locations/query', headers=header_iata,
                                params={'term': name})
        response.raise_for_status()
        iata_code = response.json()['locations'][0]['code']
        return iata_code

    def get_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        tomorrow = dt.datetime.now() + dt.timedelta(days=1)
        six_months = dt.datetime.now() + dt.timedelta(days=180)
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(f'{KIWI_ENDPOINT}/v2/search', headers=header_flight, params=params)
        try:
            data = response.json()['data'][0]
        except IndexError:
            try:
                params['max_stopovers'] = 1
                response = requests.get(f'{KIWI_ENDPOINT}/v2/search', headers=header_flight, params=params)
                data = response.json()['data'][0]
                flight_data = FlightData(data['price'], data['route'][0]['cityFrom'], data['route'][0]['flyFrom'],
                                         data["route"][1]["cityTo"], data["route"][1]["flyTo"],
                                         data["route"][0]["local_departure"].split("T")[0],
                                         data["route"][2]["local_departure"].split("T")[0],
                                         1, data['route'][0]['cityTo'])
                return flight_data
            except IndexError:
                print(f'No flights found with 0 or 1 stopovers to {params["fly_to"]}.')
                return None

        else:
            flight_data = FlightData(data['price'], data['route'][0]['cityFrom'], data['route'][0]['flyFrom'],
                                     data["route"][0]["cityTo"], data["route"][0]["flyTo"],
                                     data["route"][0]["local_departure"].split("T")[0],
                                     data["route"][1]["local_departure"].split("T")[0])
            # print(f'{flight_data.destination_city}: £{flight_data.price}')
            return flight_data
