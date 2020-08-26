
from selenium import webdriver
import time

driverLocation = "/Users/Selenium/OneDrive/Code/Selenium/Selenium/Drivers/chromedriver"

driver = webdriver.Chrome(driverLocation)

baseURL = "https://www.google.co.in/"

driver.get(baseURL)
driver.maximize_window()
time.sleep(5)

driver.close()
driver.quit()
