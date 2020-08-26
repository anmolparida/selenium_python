from selenium import webdriver
import time
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from AutomationStepBySetp.PyTest.Pages.HomePage import HomePage
from AutomationStepBySetp.PyTest.Pages.loginPage import LoginPage

def test_setup():
    global driver
    driverLocation_windows = "C:/Users/aparida/OneDrive/Code/Selenium/Drivers/chromedriver.exe"
    driver = webdriver.Chrome(driverLocation_windows)
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():
    baseURL = 'https://opensource-demo.orangehrmlive.com/'
    driver.get(baseURL)

    login = LoginPage(driver)
    login.enter_username('Admin')
    login.enter_password('admin123')
    login.click_login()

    homepage = HomePage(driver)
    homepage.click_welcome()
    time.sleep(2)
    homepage.click_logout()

def test_teardown():
    time.sleep(2)
    driver.close()
    driver.quit()



print('Test Completed')



