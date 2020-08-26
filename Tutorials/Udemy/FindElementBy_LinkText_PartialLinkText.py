import os
import time

from selenium import webdriver


class FindElementBy:

    def testFindElement(self):

        driverLocation_windows = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium\\chromedriver.exe"
        driverLocation_mac = "anmolparida\OneDrive\Code\Selenium_Python\chromedriver.exe"

        # Update based on the System you are using
        driverLocation = driverLocation_windows

        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation);

        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()
        # ------------------------------------------------------------------

        # driver.find_element_by_link_text()
        elementByLinkText = driver.find_element_by_link_text("Sign Up")
        if elementByLinkText is not None:
            print("elementByLinkText - Match Found")
        else:
            print("elementByLinkText - Match NOT Found")

        # driver.find_element_by_partial_link_text()
        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")
        if elementByPartialLinkText is not None:
            print("elementByPartialLinkText - Match Found")
        else:
            print("elementByPartialLinkText - Match NOT Found")

        #----------------------------------------------------------------------

        # Delay execution for 5 sec. as to view the maximize browser
        time.sleep(5);

        # Close the browser
        # driver.quit();



oFindElement = FindElementBy()
oFindElement.testFindElement()