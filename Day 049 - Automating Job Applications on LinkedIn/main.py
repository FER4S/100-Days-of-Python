from selenium import webdriver
import os
from selenium.common.exceptions import NoSuchElementException
import time

url = 'https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101165590&keywords=python%20developer&location=United%20Kingdom&locationId=&sortBy=R'
chrome_diver_path = r'C:\Users\Feras\Downloads\chromedriver_win32\chromedriver.exe'
email = os.environ['EMAIL']
password = os.environ['PASSWORD']

driver = webdriver.Chrome(executable_path=chrome_diver_path)

driver.get(url)

sign_in = driver.find_element_by_link_text('Sign in')
sign_in.click()

email_log_in = driver.find_element_by_id('username')
email_log_in.send_keys(email)

password_log_in = driver.find_element_by_id('password')
password_log_in.send_keys(password)

login = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login.click()

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys('123456789')

        submit_button = driver.find_element_by_css_selector("footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

driver.quit()
