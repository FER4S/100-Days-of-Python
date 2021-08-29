import requests
from bs4 import BeautifulSoup
import smtplib
import os

product_url = 'https://www.amazon.ca/Gaming-GeForce-Keyboard-Windows-G713QR-ES96/dp/B08SJNPG9H/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    "Accept-Language": 'en-US,en;q=0.5',
}
target = 3100
gmail = os.environ['GMAIL']
password = os.environ['PASSWORD']
yahoo = os.environ['YAHOO']

response = requests.get(product_url, headers=headers)
html_web_page = response.text

soup = BeautifulSoup(html_web_page, 'html.parser')
price = float(soup.find(id="priceblock_ourprice").get_text().split('$')[1].replace(',', ''))
title = soup.find(id='productTitle').get_text().split(',')[0].strip()

if price <= target:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(gmail, password)
        connection.sendmail(gmail, yahoo, f'Subject: Amazon Price Alert!\n\n{title} is now ${price}.\n'
                                          f'Buy it now at:'
                                          f'{product_url}')
