# driver.find_element_by_xpath()
# drive.find_element(By.XPATH. "xpath expression")
# id, name, xpath, css_selector, tag_name, class_name, link_text, partial_link_text

import os
import time

from selenium import webdriver

# Global Variables

driverLocation_windows = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium_Python\\chromedriver.exe"
driverLocation_mac = "anmolparida\OneDrive\Code\Selenium_Python\chromedriver.exe"

# Update based on the System you are using
driverLocation = driverLocation_windows

# Important Steps
os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation);
# driver = webdriver.firefox

baseURL = "http://letskodeit.teachable.com"
# baseURL = "https://dhtmlx.com/docs/products/dhtmlxGrid/"

class ElementState:

    def testFindElement(self):

        driver.get(baseURL)
        driver.maximize_window()

        # print(driver.title)
        # print(driver.current_url)
        # print(driver.refresh())
        # driver.get(driver.current_url)
        # driver.back()
        # driver.forward()
        # print(driver.page_source)
        # driver.close() # closes the single window
        # driver.quit()  # closes all the window and the driver


        # using contains
        # //tag[contains(attribute,'value')]
        # //tag[starts-with(attribute,'value')]
        # //tag[ends-with(attribute,'value')]

        # elementByXpath = driver.find_element_by_xpath("//div[@class='homepage-hero']//a[text()='Enroll now']")
        # elementByXpath = driver.find_element_by_xpath("//div[@id='navbar']//a[contains(text(),'Login')]")
        # elementByXpath = driver.find_element_by_xpath("//div[@id='navbar']//a[contains(@class,'navbar-link fedora') and contains(@href,'sign_in')]")

        # Syntax: xpath - to - some - element // parent:: < tag >
        # Syntax: xpath - to - some - element // preceding - sibling:: < tag >
        # Syntax: xpath - to - some - element // following - sibling:: < tag >

        # elementByXpath = driver.find_element_by_xpath("//a[@href='/sign_in']//parent::li")
        # elementByXpath = driver.find_element_by_xpath("//a[@href='/sign_in']//parent::li//following-sibling::li")
        # elementByXpath = driver.find_element_by_xpath("//a[@href='/sign_in']//parent::li//preceding-sibling::li")
        # elementByXpath = driver.find_element_by_xpath("//a[@href='/sign_in']//parent::li//preceding-sibling::li//following-sibling::li[2]")


        # elemnentbyXpath = driver.find_elements_by_xpath("//div[@title='Catherine Johnson']//following-sibling::div[1]")
        # ListOwners = driver.find_elements_by_xpath("//div[@class='dhx_grid_data']/div/div[4]/div[text()]")
        # ListHours = driver.find_elements_by_xpath("//div[@class='dhx_grid_data']/div/div[5][text()]")


        driver.implicitly_wait(10) # implicitly waits for 10 seconds before failing the code

        driver.find_element_by_xpath("//a[@href='/sign_in']").click()


        userId = driver.find_element_by_xpath("//input[@id='user_email']")
        if userId is not  None:
            userId.send_keys("user_test")
        else:
            print("userid does not exist")


        pwd = driver.find_element_by_xpath("//input[@id='user_password']")
        if pwd is not None:
            pwd.send_keys("password_test")
        else:
            print("pwd does not exist")

        time.sleep(5)
        driver.find_element_by_xpath("//input[@id='user_email']").clear()

        time.sleep(2)
        driver.close()



oFindElement = FindElementBy()
oFindElement.testFindElement()
