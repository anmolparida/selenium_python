import os

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

        # driver.find_element_by_class_name()
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing the Element")
        if elementByClassName is not None:
            print("elementByClassName - Match Found")
        else:
            print("elementByClassName - Match NOT Found")


        # driver.find_element_by_tag_name()
        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text

        if elementByTagName is not None:
            print("elementByTagName - Match Found with Header Value : " + text )
        else:
            print("elementByTagName - Match NOT Found")

        # Delay execution for 5 sec. as to view the maximize browser
        # time.sleep(5);

        # Close the browser
        # driver.quit();



oFindElement = FindElementBy()
oFindElement.testFindElement()