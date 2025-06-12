from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_field.send_keys('Sky')
sleep(2)
input_field.clear()
input_field.send_keys('Pro')

sleep(2)
driver.quit()