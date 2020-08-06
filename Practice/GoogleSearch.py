from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time


driverLocation_windows = "C:/Users/aparida/OneDrive/Code/Selenium_Python/Drivers/chromedriver83_win32.exe"

driver = webdriver.Chrome(driverLocation_windows)

url = 'https://www.google.com/'

driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()


# Search Box
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys('Blaize ')
time.sleep(2)

# [Optional] Capture all the suggested search results
searchSuggestions = driver.find_elements_by_xpath("//div[@class='sbl1']/span/b")

for x in searchSuggestions:
    print(x.text)

# [Optional] Click on Suggestion - careers
input_suggestion = 'hyderabad'
input_suggestion_element = driver.find_element_by_xpath("//div[@class='sbl1']/span/b[contains(text(),'" + input_suggestion + "')]")

# [Optional] Move Cursor to the Element
action = ActionChains(driver)
action.move_to_element(input_suggestion_element).perform()

input_suggestion_element.click()

# submenu = wait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Introduction")))

# [Optional] Click Directly On Search Button
try:
    if driver.find_element_by_xpath("(//input[@class='gNO89b'])[2]").size() != 0:
        print('Click on Default Search Button')
    elif driver.find_element_by_xpath("(//input[@class='gNO89b'])[2]").size() != 0:
            print('Click on Suggestions Search Button')
    element_present = True

# except InvalidSelectorException:
#     print('InvalidSelectorException')

except:
    print('Exception Not Defined, Both Search Buttons are unavailable')
    element_present = False




# driver.quit()
# driver.close()






















