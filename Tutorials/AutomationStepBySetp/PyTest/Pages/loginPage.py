from AutomationStepBySetp.PyTest.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.userName_textbox_id = Locators.userName_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id

    def enter_username(self, userName):
        self.driver.find_element_by_id(self.userName_textbox_id).clear()
        self.driver.find_element_by_id(self.userName_textbox_id ).send_keys(userName)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id ).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
