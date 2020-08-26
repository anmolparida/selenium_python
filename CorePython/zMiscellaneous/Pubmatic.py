from selenium import webdriver
# import


driverpath = r"C:\Users\aparida\OneDrive\Code\Selenium_Python\Drivers\chromedriver.exe"


driver = webdriver.Chrome(driverpath)


driver.get("http://edition.cnn.com/ads.txt")
driver.maximize_window()

content = driver.find_element_by_xpath("//*[@style='word-wrap: break-word; white-space: pre-wrap;']").text

with open("test_page_text.txt", "w") as fp:
	fp.writelines(content)
driver.close()
driver.quit()


import pdb

with open("test_page_text.txt", "r") as fp:
	lines = fp.readlines()
	new_list =[]
	for line in lines:
		# pdb.set_trace()
		if line[0] not in [" ", " #"]:
			new_list.append(line)


with open("new_file2.txt", "w") as fpw:
	# fpw.flush()
	fpw.writelines(new_list)







