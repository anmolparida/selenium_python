import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class By(object):

    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"


class ByDemo():

    def FindBy(self):

        driverLocation_windows = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium_Python\\chromedriver.exe"
        driverLocation_mac = "anmolparida\OneDrive\Code\Selenium_Python\chromedriver.exe"

        # Update based on the System you are using
        driverLocation = driverLocation_windows

        # Important Steps
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation);

        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()


        elementById = driver.find_element(By.ID, "name")
        if elementById is not None:
            print("elementById - Match Found")
        else:
            print("elementByLinkText - Match NOT Found")

        elementByXpath = driver.find_element(By.XPATH,"//input[@id='displayed-text']")
        if elementByXpath is not None:
            print("elementByXpath - Match Found")
        else:
            print("elementByLinkText - Match NOT Found")

        time.sleep(5);

        driver.quit();


oFindElement = ByDemo()
oFindElement.FindBy()