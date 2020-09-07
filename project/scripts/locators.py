from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SIGN_IN_MENU = (By.CLASS_NAME, 'login')

class AuthenticationPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    SIGN_IN_BUTTON = (By.ID, 'SubmitLogin')
    ALERT_BANNER = (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')