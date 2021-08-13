from flight_data import FlightData
import os
from twilio.rest import Client
import smtplib

account_sid = os.environ['ACC_SID']
auth_token = os.environ['AUTH_TOKEN']
phone = os.environ['PHONE']
my_email = os.environ['MY_EMAIL']
my_pass = os.environ['MY_PASSWORD']
yahoo = os.environ['YAHOO']


class NotificationManager:
    def __init__(self, obj: FlightData, msg, email=''):
        self.price = obj.price
        self.from_city = obj.origin_city
        self.from_airport = obj.origin_airport
        self.to_city = obj.destination_city
        self.to_airport = obj.destination_airport
        self.out_date = obj.out_date
        self.return_date = obj.return_date
        self.email = email
        self.msg = msg

    def send_msg(self):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=self.msg,
            from_='+1 979 985 2763',
            to=phone
        )
        print(message.sid)

    def send_emails(self):
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_pass)
            connection.sendmail(my_email, self.email, f'Subject: New Low Price Flight\n\n{self.msg}')

