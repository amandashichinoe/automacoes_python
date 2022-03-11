from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

url_website = 'http://www.rpachallenge.com/'
file = 'input-forms\\challenge.xlsx'
tabela_registros = pd.read_excel(file)

# Open browser
driver = webdriver.Chrome(executable_path=r'C:\\Users\\amand\\anaconda3\\chromedriver.exe')
driver.get(url_website)
driver.maximize_window()

# Startando desafio
btn_start = driver.find_element(By.XPATH, "//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']")
btn_start.click()

# Preenchendo o formulário
for row, column in tabela_registros.iterrows():
    first_name = column['First Name']
    last_name = column['Last Name']
    company_name = column['Company Name']
    role_in_company = column['Role in Company']
    address = column['Address']
    email = column['Email']
    phone_number = column['Phone Number']

    txt_name = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelFirstName"]')
    txt_name.clear()
    txt_name.send_keys(first_name)

    txt_last_name = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelLastName"]')
    txt_last_name.clear()
    txt_last_name.send_keys(last_name)

    txt_company = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelCompanyName"]')
    txt_company.clear()
    txt_company.send_keys(company_name)

    txt_role = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelRole"]')
    txt_role.clear()
    txt_role.send_keys(role_in_company)

    txt_address = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelAddress"]')
    txt_address.clear()
    txt_address.send_keys(address)

    txt_email = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelEmail"]')
    txt_email.clear()
    txt_email.send_keys(email)

    txt_phone = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelPhone"]')
    txt_phone.clear()
    txt_phone.send_keys(phone_number)

    #click submit
    btn_submit = driver.find_element(By.XPATH,"//input[@value='Submit']")
    btn_submit.click()

# aguardando o resultado
time.sleep(10)

# fechando o navegador
driver.close()





