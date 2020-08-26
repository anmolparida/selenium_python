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

        # Important Steps
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation);

        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()


        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")
        if elementByXpath is not None:
            print('elementByXpath - We have a match')
        else:
            print('elementByXpath - We Dont have a match')

        elementByCSS = driver.find_element_by_css_selector(".btn-style.class1.class2")
        if elementByXpath is not None:
            print('elementByCSS - We have a match')
        else:
            print('elementByCSS - We Dont have a match')


        # using contains
        # //tag[contains(attribute,'value')]
        # //tag[starts-with(attribute,'value')]
        # //tag[ends-with(attribute,'value')]




        elementByXpath = driver.find_element_by_xpath("//div[@class='homepage-hero']//a[text()='Enroll now']")
        elementByXpath = driver.find_element_by_xpath("//div[@id='navbar']//a[contains(text(),'Login')]")
        elementByXpath = driver.find_element_by_xpath("//div[@id='navbar']//a[contains(@class,'navbar-link fedora') and contains(@href,'sign_in')]")

        # Syntax: xpath - to - some - element // parent:: < tag >
        # Syntax: xpath - to - some - element // preceding - sibling:: < tag >
        # Syntax: xpath - to - some - element // following - sibling:: < tag >

        elementByXpath = driver.find_element_by_xpath("//a[@href='/sign_in']//parent::li")
        elementByXpath = driver.find_element_by_xpath("//a[@href='/sign_in']//parent::li//following-sibling::li")
        elementByXpath = driver.find_element_by_xpath("//a[@href='/sign_in']//parent::li//preceding-sibling::li")
        elementByXpath = driver.find_element_by_xpath("//a[@href='/sign_in']//parent::li//preceding-sibling::li//following-sibling::li[2]")


        if elementByXpath is not None:
            print('elementByXpath - We have a match')
        else:
            print('elementByXpath - We Dont have a match')



        time.sleep(2);
        driver.quit();



oFindElement = FindElementBy()
oFindElement.testFindElement()
