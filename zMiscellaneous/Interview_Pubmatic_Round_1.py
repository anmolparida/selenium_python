from selenium import  webdriver

class Pubmatic:

    def GetContent(self):

        url = "http://edition.cnn.com/ads.txt"

        macDriverLocation = "/Users/AnmolParida/OneDrive/Code/Python/Selenium/Drivers/chromedriver"

        driver = webdriver.Chrome(macDriverLocation)

        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        content = driver.find_element_by_xpath('//*[@style = "word-wrap: break-word; white-space: pre-wrap;"]').text

        # print(content)

        with open("pubmatic_raw.txt", mode='w', encoding='utf-8') as f:
            f.write(content)

        driver.close()
        driver.quit()


    def ContentCleanUp(self):

        with open("pubmatic_raw.txt", mode='r', encoding='utf-8') as f:
            print('records in raw file', len(f.readlines()))

        new_list = []
        with open("pubmatic_raw.txt", mode='r', encoding='utf-8') as f:
            for line in f.readlines():
                if line[0] not in [" ", " #"]:
                    new_list.append(line)

        # print(new_list)

        with open("pubmatic_cleaned.txt", mode='w', encoding='utf-8') as f:
            for line in new_list:
                f.write(line)
        print('records in cleaned file', len(new_list))


# instantiate and call
p = Pubmatic()
p.GetContent()
p.ContentCleanUp()