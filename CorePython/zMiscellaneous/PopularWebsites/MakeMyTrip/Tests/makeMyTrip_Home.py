from selenium import webdriver
import unittest

from Selenium.MakeMyTrip.Pages import makeMyTrip_HomePage

class TestFlightBooking(unittest.TestCase):

    # setUp/tearDown : run before every test method
    # setUpClass/tearDownClass: runs only once before all the test methods

    @classmethod
    def setUpClass(cls):

        driverLocation_windows = "C:/Users/aparida/OneDrive/Code/Python/chromedriver.exe"

        cls.driver = webdriver.Chrome(driverLocation_windows)

    # test case name should start with test_.*
    def test_flightBooking(self):

        driver = self.driver
        baseURL = "https://www.makemytrip.com/"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        # Calling HomePage - Login

        print('Testing - Test Block')

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Test Completed")

if __name__== '__main__':
        unittest.main()