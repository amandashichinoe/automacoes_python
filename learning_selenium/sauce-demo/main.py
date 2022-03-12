from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url_website = 'https://www.saucedemo.com/'

driver = webdriver.Chrome(service=Service('C:\\Users\\amand\\anaconda3\\chromedriver.exe'))
driver.get(url_website)
driver.maximize_window()

username = 'standard_user'
password = 'secret_sauce'

shopping_list = [
                    'add-to-cart-sauce-labs-backpack',
                    'add-to-cart-sauce-labs-bolt-t-shirt',
                    'add-to-cart-sauce-labs-onesie',
                    'add-to-cart-sauce-labs-bike-light',
                    'add-to-cart-sauce-labs-fleece-jacket',
                    'add-to-cart-test.allthethings()-t-shirt-(red)'
                ]

first_name = 'João'
last_name = 'Silva'
postal_code = '12345678'

def login(username, password):
    driver.find_element(By.XPATH,'//input[@id="user-name"]').send_keys(username)
    driver.find_element(By.XPATH,'//input[@id="password"]').send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH,'//input[@id="login-button"]').click()

def add_to_chart(shopping_list):
    for item in shopping_list:
        driver.find_element(By.ID,item).click()
        time.sleep(1)

def checkout(first_name, last_name, postal_code):
    driver.find_element(By.CSS_SELECTOR,'a[class="shopping_cart_link"]').click()
    time.sleep(1)
    driver.find_element(By.NAME,'checkout').click()
    time.sleep(1)
    driver.find_element(By.ID, 'first-name').send_keys(first_name)
    driver.find_element(By.ID, 'last-name').send_keys(last_name)
    driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
    driver.find_element(By.ID, 'continue').click()
    time.sleep(1)
    driver.find_element(By.ID,'finish').click()
    time.sleep(3)



login(username, password)

add_to_chart(shopping_list)

checkout(first_name, last_name, postal_code)

driver.close()

