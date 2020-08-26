# driver.find_element_by_id()
# driver.find_element_by_name()
# driver.find_element_by_xpath()
# driver.find_element_by_link_text()
# driver.find_element_by_partial_link_text()
# driver.find_element_by_tag_name()
# driver.find_element_by_class_name()
# driver.find_element_by_css_selector()

# drive.find_element(By.XPATH. "xpath expression")


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

        # driver.find_element_by_id
        elementById = driver.find_element_by_id("name")
        if elementById is not None:
            print("We found an element by id")

        # driver.find_element_by_name
        elementByName = driver.find_element_by_name("show-hide")
        if elementByName is not None:

            print("We found an element By Name")

        # for dynamic elements  the id might change after page refresh
        # driver.get("https://in.yahoo.com/")


        # elementById = driver.find_element_by_id("yui_3_18_0_3_1580391779111_781")
        # if elementById is not None:
        #     print("We found an element by id")
        # else:
        #     print("We did NOT found an element by id")

        # Delay execution for 5 sec. as to view the maximize browser
        time.sleep(5);

        # Close the browser
        driver.quit();



oFindElement = FindElementBy()
oFindElement.testFindElement()