# Selenium hybrid framework(python,selenium,pytest,page object mode,HTML reports)

#nop e-commerece

import time
from selenium import webdriver
# from selenium.webdriver.common.By import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

start_time = time.time()
print(start_time)
# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.nopcommerce.com/en")
driver.implicitly_wait(10)
# Click on the Register link
driver.find_element(By.LINK_TEXT, "Register").click()
# Wait for the registration form to load
