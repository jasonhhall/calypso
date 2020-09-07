from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SIGN_IN_MENU = (By.CLASS_NAME, 'login')
    SIGN_OUT_MENU = (By.CLASS_NAME, 'logout')

class AuthenticationPageLocators(object):
    SIGN_IN_BUTTON = (By.ID, 'SubmitLogin')
    ALERT_BANNER = (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')
    SIGN_OUT_MENU = (By.CLASS_NAME, 'logout')
    USER_ACCOUNT = (By.CLASS_NAME, 'account')