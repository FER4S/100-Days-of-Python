import csv

from bs4 import BeautifulSoup
import requests


URL = 'https://steamcharts.com/top'

response = requests.get(URL)

soup = BeautifulSoup(response.content, 'lxml')

fields = ['Rank', 'Name', 'Current Players', 'Peak Players', 'Hours Played']

names = [name.get_text().strip() for name in soup.find_all(class_='game-name')]
numbers = [num.get_text() for num in soup.find_all(class_='num')]
current_players = numbers[::3]
peak_players = numbers[1::3]
hours_played = numbers[2::3]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(fields)
    for i in range(25):
        writer.writerow([i+1, names[i], current_players[i], peak_players[i], hours_played[i]])
