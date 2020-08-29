
from selenium import webdriver
import time

# driverLocation_Mac = "/Users/AnmolParida/OneDrive/Code/Python/Selenium/Drivers/chromedriver"
driverLocation_Windows = "C:/Users/aparida/OneDrive/Code/Python/Selenium/Drivers/chromedriver.exe"



driver = webdriver.Chrome(driverLocation_Windows)

baseURL = "https://www.google.co.in/"

driver.get(baseURL)
driver.maximize_window()
time.sleep(5)

driver.close()
driver.quit()
