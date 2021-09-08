import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


CHROME_DRIVER_PATH = r'C:\Users\Feras\Downloads\chromedriver_win32\chromedriver.exe'
FORM_URL = 'https://forms.gle/JkBjvYkSJ245DMgG9'
ZILLOW_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    "Accept-Language": 'en-US,en;q=0.5',
}


# driver = webdriver.Chrome(CHROME_DRIVER_PATH)
# driver.get(ZILLOW_URL)
# web_page = driver.page_source

response = requests.get(ZILLOW_URL, headers=headers)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

links = soup.select('li .list-card-info a')
links = [a['href'] for a in links]
new_links = []
for link in links:
    if link[0] == '/':
        new_link = f'https://www.zillow.com{link}'
        new_links.append(new_link)
    else:
        new_links.append(link)
links = new_links

prices = soup.select('li .list-card-price')
prices = [price.get_text()[:6] for price in prices]


addresses = soup.select('li address')
addresses = [address.get_text() for address in addresses]

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(FORM_URL)
sleep(20)

for i in range(len(links)):
    form_address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_address.send_keys(addresses[i])

    form_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_price.send_keys(prices[i])

    form_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_link.send_keys(links[i])

    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    submit.click()

    again = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    again.click()

    sleep(5)
