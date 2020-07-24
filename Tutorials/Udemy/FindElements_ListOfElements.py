import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementBy:

    def testFindElement(self):

        driverLocation_windows = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium_Python\\chromedriver.exe"
        driverLocation_mac = "anmolparida\OneDrive\Code\Selenium_Python\chromedriver.exe"

        # Update based on the System you are using
        driverLocation = driverLocation_windows

        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation);

        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()
        # ------------------------------------------------------------------
        #
        # elementListByClassName = driver.find_elements_by_class_name("inputs")
        # length1 = len(elementListByClassName)
        # if elementListByClassName is not None:
        #     print("Size of the List by CLASS is : " + str(length1))
        # else:
        #     print("elementByLinkText - Match NOT Found")

        elementListByTagName = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elementListByTagName)
        if elementListByTagName is not None:
            print("Size of the List by TAG is : " + str(length2))

            for elements in list(elementListByTagName):
                print(elements.text)
        else:
            print("elementByLinkText - Match NOT Found")

        #----------------------------------------------------------------------

        time.sleep(5);
        driver.quit();



oFindElement = FindElementBy()
oFindElement.testFindElement()