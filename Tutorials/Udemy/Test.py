import datetime
import time

print(round(time.time()))

print(datetime.date.date)
print(datetime.date.day)
print(datetime.date.fromtimestamp())

driverLocation_windows = "C:\\Users\\aparida\\OneDrive\\Code\\Selenium\\chromedriver.exe"
driverLocation_mac = "anmolparida\OneDrive\Code\Selenium_Python\chromedriver.exe"

# Update based on the System you are using
driverLocation = driverLocation_windows

# Important Steps
os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation);
# driver = webdriver.firefox