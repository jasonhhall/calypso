from scripts.element import BasePageElement
from scripts.locators import MainPageLocators, AuthenticationPageLocators


class EmailAddressInputElement(BasePageElement):
    locator = 'email'


class EmailPasswordInputElement(BasePageElement):
    locator = 'passwd'

class AlertBanner(BasePageElement):
    locator = '#center_column > div.alert.alert-danger > p'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matches_main_page(self):
        return "My Store" in self.driver.title

    def click_sign_menu(self):
        element = self.driver.find_element(*MainPageLocators.SIGN_IN_MENU)
        element.click()


class AuthenticationPage(BasePage):

    emailAddressInputElement = EmailAddressInputElement()
    emailPasswordInputElement = EmailPasswordInputElement()

    def is_title_matches_auth_page(self):
        return "Login - My Store" in self.driver.title

    def did_email_error_banner(self):
        return "An email address required." in self.driver.page_source

    def click_sign_in_button(self):
        element = self.driver.find_element(*AuthenticationPageLocators.SIGN_IN_BUTTON)
        element.click()

    def get_banner_alert_message(self):
        element = self.driver.find_element(*AuthenticationPageLocators.ALERT_BANNER)
        return element.text
