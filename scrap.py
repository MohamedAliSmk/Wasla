import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

# log in to Microsoft login
driver.get('https://login.microsoftonline.com/')
email_input = driver.find_element('i0116')
email_input.send_keys('karimelanbry@paymob.com')
next_button = driver.find_element_by_id('idSIButton9')
next_button.click()
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'i0118')))
password_input.send_keys('KoKo.2010')
signin_button = driver.find_element_by_id('idSIButton9')
signin_button.click()
time.sleep(1500) # wait for the page to load

# navigate to the URL
url = 'https://accept-reporting.paymobsolutions.com/anotherpanel/payment_methods/transaction/'
driver.get(url)

# parse the HTML with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)
