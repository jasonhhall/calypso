from scripts.element import BasePageElement
from scripts.locators import MainPageLocators, AuthenticationPageLocators, ShoppingCartSummaryPageLocators, AddressPageLocators 
from scripts.locators import ShippingPageLocators, PaymentPageLocators, OrderConforimationPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


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

    def click_signin_menu(self):
        element = self.driver.find_element(*MainPageLocators.SIGN_IN_MENU)
        element.click()

    def click_signout_menu(self):
        element = self.driver.find_element(*MainPageLocators.SIGN_OUT_MENU)
        element.click()

    def is_signout_visible(self):
        if self.driver.find_element(*MainPageLocators.SIGN_OUT_MENU):
            return True
        else:
            return False

    def proceedToCheckout(self):
        popupWindow = self.driver.find_element(*MainPageLocators.POPUP_PANEL)
        proceed_to_checkout_button = wait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PROCEED_TO_CHECKOUT_BUTTON))
        proceed_to_checkout_button.click()

    def continueShopping(self):
        popupWindow = self.driver.find_element(*MainPageLocators.POPUP_PANEL)
        continue_shopping = wait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.CONTINUE_SHOPPING))
        continue_shopping.click()
        

    def addItemToCart(self, itemName ):
        products = self.driver.find_elements(*MainPageLocators.ITEM_LIST)
        for product in products:

            if itemName == product.get_attribute("title"):  
                action=ActionChains(self.driver)
                action.move_to_element(product).perform()
                addToCartButton = wait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.ADD_TO_CART_BUTTON))
                addToCartButton.click()


class AuthenticationPage(BasePage):
    emailAddressInputElement = EmailAddressInputElement()
    emailPasswordInputElement = EmailPasswordInputElement()

    def is_title_matches_auth_page(self):
        return "Login - My Store" in self.driver.title

    def is_signin_visible(self):
        if self.driver.find_element(*AuthenticationPageLocators.SIGN_IN_MENU):
            return True
        else:
            return False

    def is_signout_visible(self):
        if self.driver.find_element(*AuthenticationPageLocators.SIGN_OUT_MENU):
            return True
        else:
            return False

    def is_user_account_visible(self):
        if self.driver.find_element(*AuthenticationPageLocators.SIGN_OUT_MENU):
            return True
        else:
            return False

    def did_email_error_banner(self):
        return "An email address required." in self.driver.page_source

    def click_signin_button(self):
        element = self.driver.find_element(*AuthenticationPageLocators.SIGN_IN_BUTTON)
        element.click()

    def click_signout_button(self):
        element = self.driver.find_element(*AuthenticationPageLocators.SIGN_OUT_MENU)
        element.click()

    def get_banner_alert_message(self):
        element = self.driver.find_element(*AuthenticationPageLocators.ALERT_BANNER)
        return element.text

class ShoppingCartSummaryPage(BasePage):

    def is_title_matches_shopping_cart_summary_page(self):
        return "Order - My Store" in self.driver.title

    def getItemsDescription(self):
        elements = self.driver.find_elements(*ShoppingCartSummaryPageLocators.ITEMS_DESC)
        for element in elements:
            name = element.find_element(By.CLASS_NAME, 'product-name')
            if name.text =='Faded Short Sleeve T-shirts':
                return name

    def click_checkout_button(self):
        element = self.driver.find_element(*ShoppingCartSummaryPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        element.click()

class AddressPage(BasePage):

    def click_checkout_button(self):
        element = self.driver.find_element(*AddressPageLocators.PROCEED_TO_CHECKOUT_BUTTON)
        element.click()

class ShippingPage(BasePage):

    def click_checkout_button(self):
        element = self.driver.find_element(*ShippingPageLocators.PROCEED_TO_CHECKOUT_BUTTON).click()

    def click_terms_of_service(self):
        element = self.driver.find_element(*ShippingPageLocators.TOS)
        element.click()

class PaymentPage(BasePage):
    
    def payByBankWire(self):
        self.driver.find_element(*PaymentPageLocators.PAY_BY_BANK_WIRE).click()

    def payByCheck(self):
        self.driver.find_element(*PaymentPageLocators.PAY_BY_CHECK).click()

    def chooseDifferntMethodOfPayment(self):
        self.driver.find_element(*PaymentPageLocators.OTHER_PAYMENTS_METHODS).click()

    def confirmOrder(self):
        element = self.driver.find_element(*PaymentPageLocators.CONFIRM_ORDER).click()

class OrderConfirmationPage(BasePage):
    
    # def getOrderReference(self):
    #     element = self.driver.find_element(*OrderConforimationPageLocators.ORDER_CONFRIMATION_MESSAGE)
    #     return element.text

    def backToOrders(self):
        element = self.driver.find_element(*OrderConforimationPageLocators.BACK_TO_ORDERS).click()

