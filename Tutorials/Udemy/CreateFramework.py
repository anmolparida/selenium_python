
import os
import time

from selenium import webdriver


class SeleniumFramework:

        def newTest(self):

            driverLocation = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium\\chromedriver.exe"

            os.environ["webdrive.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)

            baseURL = "https://www.microsoft.com/en-in"
            driver.get(baseURL)
            driver.maximize_window()
            time.sleep(5)
            driver.quit()


objSeleniumFramework = SeleniumFramework()
objSeleniumFramework.newTest()