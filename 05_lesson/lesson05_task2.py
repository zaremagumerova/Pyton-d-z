from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")

button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
sleep(1)
button.click()

sleep(3)

driver.quit()