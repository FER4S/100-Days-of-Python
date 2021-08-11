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

for city in sheet_data:
    flight_data = flight.get_flight(ORIGIN_CITY_IATA, city['iataCode'], tomorrow, six_month_from_today)
    if city['lowestPrice'] > flight_data.price:
        notification = NotificationManager(flight_data)

