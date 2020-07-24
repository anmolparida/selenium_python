# driver.find_element_by_xpath()
# drive.find_element(By.XPATH. "xpath expression")
# id, name, xpath, css_selector, tag_name, class_name, link_text, partial_link_text

import os
import time

from Selenium.Udemy.HandyWrappers import HandyWrappers
from selenium import webdriver
from selenium.webdriver.support.select import Select

# Global Variables

driverLocation_windows = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium_Python\\chromedriver.exe"
driverLocation_mac = "anmolparida\OneDrive\Code\Selenium_Python\chromedriver.exe"

# Update based on the System you are using
driverLocation = driverLocation_windows

# Important Steps
os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation);
# driver = webdriver.firefox

# baseURL = "http://letskodeit.teachable.com"
# baseURL = "http://letskodeit.teachable.com/p/practice"
# baseURL = "https://dhtmlx.com/docs/products/dhtmlxGrid/"

class BrowserInteractions:

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


    # Implicit and Explicit Wait
    # element_to_be_clickable
    # element_to_be_selected
    #
    #
    #
    #

    def LogIn(self):
        driver.find_element_by_xpath("//a[@href='/sign_in']").click()

        userId = driver.find_element_by_xpath("//input[@id='user_email']")
        if userId is not None:
            userId.send_keys("user_test")
        else:
            print("userid does not exist")

        pwd = driver.find_element_by_xpath("//input[@id='user_password']")

        if pwd is not None:
            pwd.send_keys("password_test")
        else:
            print("pwd does not exist")

        time.sleep(5)


    def ElementState_isEnabled(self):

        baseURL = "http://www.google.com"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(3)
        e1 = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")

        print(e1.is_displayed())
        print(e1.is_enabled())
        print(e1.is_selected())

        e1.click()
        e1.send_keys("letskodeit")



    def RadioButtons_CheckBoxes(self):

        baseURL = "http://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(3)

        c1 = driver.find_element_by_id("bmwradio")
        print("bmwradio")
        print(c1.is_enabled())
        print(c1.is_displayed())
        print(c1.is_selected())
        c1.click()
        print(c1.is_selected())
        time.sleep(2)
        c1 = driver.find_element_by_id("hondaradio")
        c1.click()
        time.sleep(2)
        c1 = driver.find_element_by_id("benzradio")
        c1.click()

        # CheckBox
        c1 = driver.find_element_by_id("benzcheck")
        c1.click()
        c1 = driver.find_element_by_id("bmwcheck")
        c1.click()
        c1 = driver.find_element_by_id("hondacheck")
        c1.click()


    def DropDown_List_ComboBox(self):

        baseURL = "http://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(3)

        element = driver.find_element_by_id("carselect")
        sel = Select(element) #BMW, Benz, Honda
        print(sel.options)

        print("Select by Value")
        sel.select_by_value("benz")
        time.sleep(2)

        print("Select Honda by Index")
        sel.select_by_index(0) # starts
        #  with 0
        time.sleep(1)
        sel.select_by_index(1)  # starts with 0
        time.sleep(1)
        sel.select_by_index("2")  # starts with 0
        time.sleep(1)

        print("Select by visible text")
        sel.select_by_visible_text("BMW")
        time.sleep(1)


    def HiddenElements(self):

        baseURL = "https://www.expedia.com/"
        driver.get(baseURL)
        driver.maximize_window()


    def GetAttribue(self):

        baseURL = "http://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()

        element = driver.find_element_by_id("name")
        result = element.get_attribute("class") # return the attribute value attribute='value'

        print(result)


    def UsingWrappers(self):

        baseURL = "http://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()

        hw = HandyWrappers

        textfield = hw.getElement("name", "id")
        textfield.send_keys("Test")
        time.sleep(2)

        textfield2 = hw.getElement("[//input[@id='name']", locatorType= "xpath")
        textfield2.clear
        time.sleep(2)






# time.sleep(2)
# driver.close()
# driver.quit()



oBrowserInteractions = BrowserInteractions()


oBrowserInteractions.UsingWrappers()
# oBrowserInteractions.GetAttribue()
# oBrowserInteractions.HiddenElements()
# oBrowserInteractions.DropDown_List_ComboBox()
# oBrowserInteractions.RadioButtons_CheckBoxes()
# oBrowserInteractions.ElementState_isEnabled()
# oBrowserInteractions.LogIn()
