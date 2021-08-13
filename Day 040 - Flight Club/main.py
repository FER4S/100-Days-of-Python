from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

flight = FlightSearch()
data = DataManager()

sheet_data = data.get_sheet()
for city in sheet_data:
    if not city['iataCode']:
        city['iataCode'] = flight.get_iata(city['city'])
        data.put_sheet(city)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

emails = data.get_emails()

for city in sheet_data:
    flight_data = flight.get_flight(ORIGIN_CITY_IATA, city['iataCode'], tomorrow, six_month_from_today)
    if flight_data is None:
        continue
    if city['lowestPrice'] > flight_data.price:
        msg = f"Low price alert!! \nOnly {flight_data.price} Pound to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}"
        if flight_data.stop_overs > 0:
            msg += f'\nFlight has {flight_data.stop_overs} stop over, via {flight_data.via_city}.'
        msg += f'\nhttps://www.google.co.uk/flights?hl=en#flt=STN.{flight_data.destination_airport}.{flight_data.out_date}*{flight_data.destination_airport}.STN.{flight_data.return_date}'
        for email in emails:
            notification = NotificationManager(flight_data, msg, email['email'])
            notification.send_emails()
    # notification = NotificationManager(flight_data)
    # notification.send_msg()
