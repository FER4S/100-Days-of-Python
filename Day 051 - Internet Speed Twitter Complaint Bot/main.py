from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep

PROMISED_DOWN = 1
PROMISED_UP = 0.5
chrome_diver_path = r'C:\Users\Feras\Downloads\chromedriver_win32\chromedriver.exe'
email = os.environ['EMAIL']
password = os.environ['PASSWORD']
speed_test_url = 'https://www.speedtest.net/'
twitter_url = 'https://twitter.com/login'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_diver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(speed_test_url)
        start_btn = self.driver.find_element_by_css_selector('.start-button a')
        start_btn.click()
        sleep(60)
        self.down = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

    def tweet_at_provider(self):
        self.driver.get(twitter_url)

        user = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        user.send_keys(email)

        pw = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)
        sleep(10)

        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        msg = f'Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up ' \
                     f'when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?'
        tweet.send_keys(msg)


obj = InternetSpeedTwitterBot()
obj.get_internet_speed()
obj.tweet_at_provider()
