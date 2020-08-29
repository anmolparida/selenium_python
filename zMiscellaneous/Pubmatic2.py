from selenium import webdriver

driverpath = r"C:\Users\aparida\OneDrive\Code\Selenium\Selenium_Python\Drivers\chromedriver.exe"


driver = webdriver.Chrome(driverpath)
driver.get("http://edition.cnn.com/ads.txt")
driver.maximize_window()
driver.implicitly_wait(5)

content = driver.find_element_by_xpath('//pre[@style="word-wrap: break-word; white-space: pre-wrap;"]').text

with open("output.txt", "w") as fp:
    fp.writelines(content)

driver.close()
driver.quit()


