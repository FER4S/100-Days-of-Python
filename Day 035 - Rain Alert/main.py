import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = os.environ.get("OWM_API_KEY")
lon = -0.127758
lat = 51.507351
account_sid = 'ACd1a51ab1194c73105a50dfc3804a72d0'
auth_token = os.environ.get('AUTH_TOKEN')
phone_number = os.environ.get('PHONE_NUMBER')

params = {
    'lat': lat,
    'lon': lon,
    'appid': api_key,
    'exclude': 'current,minutely,daily,alerts',
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params)
response.raise_for_status()

data = response.json()['hourly'][:12]
codes = [day['weather'][0]['id'] for day in data]
for code in codes:
    if code < 700:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token, http_client=proxy_client)
        message = client.messages \
            .create(
            body="It's going to rain today🌧, Remember to bring an umbrella☔",
            from_='+1 979 985 2763',
            to=phone_number
        )
        print(message.status)
        break
