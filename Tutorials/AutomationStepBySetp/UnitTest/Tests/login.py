from selenium import webdriver
import time
import unittest
import sys
import os


driverLocation_windows = "C:/Users/aparida/OneDrive/Code/Selenium/Drivers/chromedriver.exe"


sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from AutomationStepBySetp.UnitTest.Pages.HomePage import HomePage
from AutomationStepBySetp.UnitTest.Pages.loginPage import LoginPage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        driverLocation_windows = "C:/Users/aparida/OneDrive/Code/Selenium/Drivers/chromedriver.exe"
        cls.driver = webdriver.Chrome(driverLocation_windows)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):

        baseURL = 'https://opensource-demo.orangehrmlive.com/'
        driver = self.driver
        driver.get(baseURL)

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        time.sleep(2)
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):

        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()

        print('Test Completed')



