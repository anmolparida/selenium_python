import platform
import re


def driverLocation(browserName):
    # self.browserName = browserName
    if platform.system() == 'Darwin':
        if re.search(browserName, 'chrome', re.IGNORECASE):
            driverLocation_chrome = "/Users/Selenium/OneDrive/Code/Selenium/Drivers/chromedriver"
            return driverLocation_chrome

    elif platform.system() == 'Windows':
        if re.search(browserName, 'chrome', re.IGNORECASE):
            driverLocation_chrome = "C:/Users/aparida/OneDrive/Code/Selenium/Selenium/Drivers/chromedriver.exe"
            return driverLocation_chrome

    elif platform.system() == "Linux":
        print("Not available - To be Configured")

    else:
        print("Not Defined- Recheck - To be Configured")


print(driverLocation('chrome'))