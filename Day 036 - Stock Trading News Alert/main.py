import requests
import datetime as dt
# import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = '"Tesla Inc"'
stock_price_api_endpoint = 'https://www.alphavantage.co/query'
stock_price_api_key = 'AMPHWSTBJQGMHU7L'
news_api_endpoint = 'https://newsapi.org/v2/everything'
news_api_key = '035875bb44314a1f9448430842b8147c'
account_sid = 'ACd1a51ab1194c73105a50dfc3804a72d0'
auth_token = '******'
stock_price_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': stock_price_api_key,
}
news_params = {
    'q': COMPANY_NAME,
    'apiKey': news_api_key,
}

today = dt.datetime.today()
yesterday_date = (today - dt.timedelta(days=4)).strftime('%Y-%m-%d')
previous_day_date = (today - dt.timedelta(days=5)).strftime('%Y-%m-%d')

response = requests.get(stock_price_api_endpoint, stock_price_params)
response.raise_for_status()
data = response.json()
yesterday_close = float(data['Time Series (Daily)'][yesterday_date]['4. close'])
previous_day_close = float(data['Time Series (Daily)'][previous_day_date]['4. close'])
percentage = round((yesterday_close - previous_day_close)/yesterday_close*100)
percentage_emo = '🔺' if percentage > 0 else '🔻'
if abs(percentage) >= 0:
    percentage_str = f'{percentage_emo}{percentage}%'
    response = requests.get(news_api_endpoint, news_params)
    response.raise_for_status()
    news_articles = response.json()['articles'][:3]
    for news_article in news_articles:
        # proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"\n{STOCK}: {percentage_str}\n"
                 f"Headline: {news_article['title']}\n"
                 f"Brief: {news_article['description']}",
            from_='+1 979 985 2763',
            to='*****'
        )
        print(message.status)

