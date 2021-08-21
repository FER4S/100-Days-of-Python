import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.empireonline.com/movies/features/best-movies-2/"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')

movies = [movie.get_text() for movie in soup.find_all('h3')]
movies.reverse()

with open('movies.txt', 'w') as file:
    for movie in movies:
        file.write(f'{movie}\n')
