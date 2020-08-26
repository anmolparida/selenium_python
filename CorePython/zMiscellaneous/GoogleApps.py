from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

# from Selenium.Drivers.DriverPath import driverLocation

browserName = 'Chrome'
driverLocation_chrome = "C:/Users/aparida/OneDrive/Code/Selenium/Selenium/Drivers/chromedriver.exe"

driver = webdriver.Chrome(driverLocation_chrome)
# driver = webdriver.Chrome(driverLocation(browserName))
baseURL = 'https://www.google.com'

driver.get(baseURL)
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_xpath("//a[@class='gb_D gb_zc']").click()

try:
    element_app = driver.find_element_by_xpath("(//a[@class='tX9u1b']/span[@class='Rq5Gcb'])[4]")
    element_app.click

except NoSuchElementException:
    print("NoSuchElementException - Before switching Frame")

# Finding the list of Google Apps
# element_apps = driver.find_elements_by_xpath("//a[@class='tX9u1b']/span[?@class='Rq5Gcb']")


# Element is present inside a frame
count_frame = driver.find_elements_by_tag_name('iframe')
print("No of frames present in the web page are: ", len(count_frame))

frame1 = driver.find_element_by_xpath("//iframe[@role='presentation'][1]")

driver.switch_to.frame(frame1)
driver.implicitly_wait(30)

count = 0
path_output = "C:\\Users\\aparida\\Desktop\\Output"

element_apps = driver.find_elements_by_xpath("(//span[@class='Rq5Gcb'])")

f = open('googleApps.txt', 'w+')

for apps in element_apps:
    count = count + 1
    print(count, apps.text)

    f.write(str(count) + ". " + apps.text + '\n')

f.close()


# Highlight the contents of the iframe
driver.find_element_by_tag_name('a').send_keys(Keys.CONTROL, 'a')
time.sleep(2)

app_to_select = 'Blogger'

try:
    element_YouTube = driver.find_element_by_xpath("//span[contains(text(),'" + app_to_select+ "')]")
    element_YouTube.click()

except NoSuchElementException:
    print("NoSuchElementException - after switching Frame")

driver.switch_to.default_content()


if driver.title == app_to_select:
    print(app_to_select, 'loaded successfully')
elif driver.title.find(app_to_select) != -1:
    print(driver.title,'loaded successfully')
else:
    print(app_to_select, 'Did not Load successfully. Recheck')

