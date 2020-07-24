import os

from selenium import webdriver


class RunChromeTestWindows():
    def test(self):

        driverLocation_windows = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium_Python\\chromedriver.exe"
        driverLocation_mac = "anmolparida\OneDrive\Code\Selenium_Python\chromedriver.exe"

        # Update based on the System you are using
        driverLocation = driverLocation_windows

        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation);
        driver.get("https://www.letskodeit.com")


chromeTest = RunChromeTestWindows();
chromeTest.test();

# driver.find_element_by_id()
# driver.find_element_by_name()
# driver.find_element_by_xpath()
# driver.find_element_by_link_text()
# driver.find_element_by_partial_link_text()
# driver.find_element_by_tag_name()
# driver.find_element_by_class_name()
# driver.find_element_by_css_selector()

# drive.find_element(By.XPATH. "xpath expression")