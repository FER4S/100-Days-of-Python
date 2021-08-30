from selenium import webdriver
import time

chrome_diver_path = r'C:\Users\Feras\Downloads\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_diver_path)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id('cookie')

timeout = time.time() + 60 * 5
five_sec = time.time() + 5
while True:
    cookie.click()

    if time.time() > five_sec:
        five_sec = time.time() + 5
        cursor = driver.find_element_by_css_selector('#buyCursor b')
        grandma = driver.find_element_by_css_selector('#buyGrandma b')
        factory = driver.find_element_by_css_selector('#buyFactory b')
        mine = driver.find_element_by_css_selector('#buyMine b')
        shipment = driver.find_element_by_css_selector('#buyShipment b')
        alchemy = driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]/b')
        portal = driver.find_element_by_css_selector('#buyPortal b')
        time_machine = driver.find_element_by_xpath('//*[@id="buyTime machine"]/b')
        money = int(driver.find_element_by_id('money').text)

        cursor_cost = int(cursor.text.split('-')[1].strip().replace(',', ''))
        grandma_cost = int(grandma.text.split('-')[1].strip().replace(',', ''))
        factory_cost = int(factory.text.split('-')[1].strip().replace(',', ''))
        mine_cost = int(mine.text.split('-')[1].strip().replace(',', ''))
        shipment_cost = int(shipment.text.split('-')[1].strip().replace(',', ''))
        alchemy_cost = int(alchemy.text.split('-')[1].strip().replace(',', ''))
        portal_cost = int(portal.text.split('-')[1].strip().replace(',', ''))
        time_machine_cost = int(time_machine.text.split('-')[1].strip().replace(',', ''))

        if time_machine_cost <= money:
            time_machine.click()
        elif portal_cost <= money:
            portal.click()
        elif alchemy_cost <= money:
            alchemy.click()
        elif shipment_cost <= money:
            shipment.click()
        elif mine_cost <= money:
            mine.click()
        elif factory_cost <= money:
            factory.click()
        elif grandma_cost <= money:
            grandma.click()
        elif cursor_cost <= money:
            cursor.click()

    if time.time() > timeout:
        cps = driver.find_element_by_id('cps').text
        print(f'cookies/sec: {cps}')
        break
