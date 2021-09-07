from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

CHROME_DRIVER_PATH = r'C:\Users\Feras\Downloads\chromedriver_win32\chromedriver.exe'
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
SIMILAR_ACCOUNT = 'python.learning'
LOG_IN_URL = 'https://www.instagram.com/accounts/login/'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(LOG_IN_URL)
        sleep(5)

        user = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.send_keys(EMAIL)

        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(10)

    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}')
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(5)

        followers_list = self.driver.find_element_by_class_name('isgrP')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
            sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector('li button')
        for button in follow_buttons:
            button.click()


obj = InstaFollower()
obj.login()
obj.find_followers()
obj.follow()
