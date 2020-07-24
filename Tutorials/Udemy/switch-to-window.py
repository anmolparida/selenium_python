import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SwitchToWindow():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"

        driverLocation_windows = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium_Python\\chromedriver.exe"
        driverLocation_mac = "anmolparida/OneDrive/Code/Selenium_Python/chromedriver.exe"

        # Update based on the System you are using
        driverLocation = driverLocation_windows

        # Important Steps
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation);
        # driver = webdriver.firefox
        driver.maximize_window()
        driver.get(baseUrl)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)
        driver.get(baseUrl)
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)

ff = SwitchToWindow()
ff.test()