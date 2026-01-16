from selenium import webdriver
from selenium.common import ElementNotVisibleException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://practice.expandtesting.com/')

print(driver.title)

driver.maximize_window()
'''
Locators
1. In-built locators - 
id - driver.find_elements(BY.ID,'value')
name - driver.find_element(By.NAME,'value')
linked text - driver.find_element(BY.LINK_TEXT,'value') 
partial linked text -  driver.find_element(By.PARTIAL_LINK_TEXT,'value')
Class name - variable_name = driver.find_elements(By.CLASS_NAME,'value') : returns list of same locator name
tag name - variable_name = driver.find_elements(By.TAG_NAME,'value') : returns list of same locator name
2. customised locators (combination of in-built locators) 
CSS - 
combination of Tag & ID
driver.find_element(By.CSS_SELECTOR,'input#email')  tagname#IDvalue 
combination of Tag & Classname
driver.find_element(By.CSS_SELECTOR,'input.email')   tagname.classvalue
combination of Tag & Attribute
driver.find_element(By.CSS_SELECTOR,'input[data-testid=royal_email]')   tagname[attribute name = attribute value]
combination of Tag & class & attribute
driver.find_element(By.CSS_SELECTOR,'input.email[data-testid=royal_email]')   tagname.classvalue[attribute name = attribute value]

XPATH
'''
def xpath_classification():
    try:
        driver.find_element(By.ID, 'search-input').send_keys('sample test cases')
        time.sleep(10)
    except ElementNotVisibleException as e:
        print('element not found')
