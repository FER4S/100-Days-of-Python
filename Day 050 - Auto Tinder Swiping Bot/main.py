from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
import time

url = 'https://tinder.com/'
chrome_diver_path = r'C:\Users\Feras\Downloads\chromedriver_win32\chromedriver.exe'
email = os.environ['EMAIL']
password = os.environ['PASSWORD']

driver = webdriver.Chrome(executable_path=chrome_diver_path)
driver.get(url)

log_in = driver.find_element_by_link_text('LOG IN')
log_in.click()
time.sleep(10)

fb = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb.click()
time.sleep(30)

base_window = driver.window_handles[0]
fb_log_in_window = driver.window_handles[1]
driver.switch_to.window(fb_log_in_window)

email_log_in = driver.find_element_by_id('email')
email_log_in.send_keys(email)

password_log_in = driver.find_element_by_id('pass')
password_log_in.send_keys(password)
password_log_in.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
time.sleep(60)

allow = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div/div/div[3]/button[1]')
allow.click()

not_interested = driver.find_element_by_xpath('//*[@id="q545960529"]/div/div/div/div/div[3]/button[2]')
not_interested.click()

accept = driver.find_element_by_xpath('//*[@id="q-2020625691"]/div/div[2]/div/div/div[1]/button/span')
accept.click()
time.sleep(20)

while True:
    try:
        like = driver.find_element_by_xpath('//*[@id="q-2020625691"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like.click()
        time.sleep(2)
    except NoSuchElementException:
        print('still loading...')
        time.sleep(2)

    except ElementClickInterceptedException:
        print('matched')
        break
