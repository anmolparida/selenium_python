class Locators():


    # Home Page - Login
    logInOrCreateAccount = "//p[contains(text(),' Login or Create Account')]"
    googleLogin = "//div[@data-cy='googleLogin']"

    # Home Page - Search
    fromCity_button = "//label[@for='fromCity']"
    toCity_button = "//input[@data-cy='toCity']"
    fromCity_textBox = "//input[@c='From']"
    toCity_textBox = "//input[@placeholder='To']"
    departure_button = "//span[contains(text(),'DEPARTURE')]"
    returnDate_button = "//span[contains(text(),'RETURN')]"
    departureDate_textBox ="//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/div[6]/div/p[1]"
    returnDate_textBox    = "//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/div[6]/div/p[1]"
    search_button = "//a[contains(text(),'Search')]"