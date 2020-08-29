from Selenium.MakeMyTrip.Locators.makeMyTrip_locators import Locators


class HomePage():

    def __init__(self,driver):
        self.driver = driver

        # List of all Objects in the Page

        #Log In
        self.logInOrCreateAccount = Locators.logInOrCreateAccount
        self.googleLogin = Locators.googleLogin

        # Search Values
        fromCity_button = Locators.fromCity_button
        self.toCity_button = Locators.toCity_button
        self.fromCity_textBox = Locators.fromCity_textBox
        self.toCity_textBox = Locators.toCity_textBox
        self.departure_button = Locators.departure_button
        self.returnDate_button = Locators.returnDate_button
        self.departureDate_textBox = Locators.departureDate_textBox
        self.returnDate_textBox = Locators.returnDate_textBox
        self.search_button = Locators.search_button


    def LogIn_SignUp(self):
        self.driver.find_element_by_xpath(self.logInOrCreateAccount).click()
        self.driver.find_element_by_xpath(self.googleLogin).click()


    def SearchDetails(self):
        self.driver.find_element_by_xpath(self.fromCity_button).click()
        self.driver.find_element_by_xpath(self.fromCity_textBox).send_keys()
        self.driver.find_element_by_xpath(self.fromCity_button)
        self.driver.find_element_by_xpath(self.fromCity_button)
        self.driver.find_element_by_xpath(self.fromCity_button)
        self.driver.find_element_by_xpath(self.fromCity_button)
        self.driver.find_element_by_xpath(self.fromCity_button)
        self.driver.find_element_by_xpath(self.fromCity_button)
        self.driver.find_element_by_xpath(self.fromCity_button)






