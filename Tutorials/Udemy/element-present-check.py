import os

from SeleniumUsingPython.HandyWrappers import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementPresentCheck():

    def test(self):

        baseUrl = "https://letskodeit.teachable.com/pages/practice"

        driverLocation_windows = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium\\chromedriver.exe"
        driverLocation_mac = "anmolparida\OneDrive\Code\Selenium_Python\chromedriver.exe"

        # Update based on the System you are using
        driverLocation = driverLocation_windows

        # Important Steps
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation);
        driver.implicitly_wait(10)

        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresenceCheck("//input[@id='name1']", By.XPATH)
        print(str(elementResult2))


ff = ElementPresentCheck()
ff.test()


