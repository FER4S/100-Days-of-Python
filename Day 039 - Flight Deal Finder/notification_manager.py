from flight_data import FlightData
import os
from twilio.rest import Client

account_sid = os.environ['ACC_SID']
auth_token = os.environ['AUTH_TOKEN']
phone = os.environ['PHONE']


class NotificationManager:
    def __init__(self, obj: FlightData):
        self.price = obj.price
        self.from_city = obj.origin_city
        self.from_airport = obj.origin_airport
        self.to_city = obj.destination_city
        self.to_airport = obj.destination_airport
        self.out_date = obj.out_date
        self.return_date = obj.return_date
        self.send_msg()

    def send_msg(self):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Low price alert!⚠ \n"
                 f"Only £{self.price} to fly from {self.from_city}-{self.from_airport} to "
                 f"{self.to_city}-{self.to_airport}, from {self.out_date} to {self.return_date}",
            from_='+1 979 985 2763',
            to=phone
        )
        print(message.sid)
