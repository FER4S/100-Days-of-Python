import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 32.704400
MY_LONG = 36.566022
MY_EMAIL = 'testing.for.python44@gmail.com'
MY_PASSWORD = '************'
YAHOO_MAIL = 'testing_for_python@yahoo.com'
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def over_head():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


def send_mail():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, YAHOO_MAIL,
                            'Subject:ISS IS OVERHEAD!\n\nISS 🛰 is above you.\n you can spot it in the sky')


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    hour = time_now.hour
    if hour <= sunrise or hour >= sunset:
        return True
    return False


while True:
    time.sleep(60)
    if is_night() and over_head():
        send_mail()
