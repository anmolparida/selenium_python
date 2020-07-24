import platform
import re

class DrivePathBasedOnOS:

    def pathToLocation(self, browserName):
        self.browserName = browserName
        if platform.system() == 'Darwin':
            if re.search(self.browserName,'chrome', re.IGNORECASE):
                driverLocation_chrome = "/Users/AnmolParida/OneDrive/Code/Selenium_Python/Drivers/chromedriver"
                return  driverLocation_chrome

        elif platform.system() == 'Windows':
            if re.search(self.browserName, 'chrome', re.IGNORECASE):
                driverLocation_chrome = "/Users/AnmolParida/OneDrive/Code/Selenium_Python/Drivers/chromedriver"
                return driverLocation_chrome

        elif platform.system() == "Linux":
            print("Not available - To be Configured")

        else:
            print("Not Defined- Recheck - To be Configured")


a = DrivePathBasedOnOS
print(a.pathToLocation('chrome'))
