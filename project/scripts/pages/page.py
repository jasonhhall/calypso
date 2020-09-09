from scripts.element import BasePageElement
from scripts.locators import MainPageLocators, AuthenticationPageLocators, ShoppingCartSummaryPageLocators, AddressPageLocators 
from scripts.locators import ShippingPageLocators, PaymentPageLocators, OrderConforimationPageLocators, OrderHistoryPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class EmailAddressInputElement(BasePageElement):
    locator = 'email'

class EmailPasswordInputElement(BasePageElement):
    locator = 'passwd'

class OrderComment(BasePageElement):
    locator = 'message'

class NewAddressFirstName(BasePageElement):
    locator = 'firstname'

class NewAddressLastName(BasePageElement):
    locator = 'lastname'

class NewAddressCompany(BasePageElement):
    locator = 'company'

class NewAddressAddress1(BasePageElement):
    locator = 'address1'

class NewAddressAddress2(BasePageElement):
    locator = 'address2'

class NewAddressCity(BasePageElement):
    locator = 'city'

class NewAddressPostalCode(BasePageElement):
    locator = 'postcode'

class NewAddressHomePhone(BasePageElement):
    locator = 'phone'

class NewAddressMobilePhone(BasePageElement):
    locator = 'phone_mobile'

class NewAddressAdditional(BasePageElement):
    locator = 'other'

class NewAddressTitle(BasePageElement):
    locator = 'alias'

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
            if itemName == product.find_element(*MainPageLocators.PRODUCT_NAME).get_attribute('title'):
                action=ActionChains(self.driver)
                action.move_to_element(product).perform()
                addToCartButton = wait(product, 10).until(EC.element_to_be_clickable(MainPageLocators.ADD_TO_CART_BUTTON))
                addToCartButton.click()


class AuthenticationPage(BasePage):
    email_address_input_element = EmailAddressInputElement()
    email_password_input_element = EmailPasswordInputElement()

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
        element = wait(self.driver, 10).until(EC.element_to_be_clickable(AuthenticationPageLocators.SIGN_IN_BUTTON))
        # self.driver.find_element(*AuthenticationPageLocators.SIGN_IN_BUTTON)
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

    def getProductFromSummaryPage(self, productName):
        products = self.driver.find_elements(*ShoppingCartSummaryPageLocators.PRODUCTS)

        for product in products:
            product_description = product.find_element(*ShoppingCartSummaryPageLocators.PRODUCT_NAME).text
            if product_description == productName:
                return product
        return None

    def getUnitPrice(self, productName):
        product_element = self.getProductFromSummaryPage(productName)
        if product_element:
            return product_element.find_element(*ShoppingCartSummaryPageLocators.UNIT_PRICE).text
        else:
            return "Product was not found"

    def getSubTotal(self, productName):
        product_element = self.getProductFromSummaryPage(productName)
        if product_element:
            return product_element.find_element(*ShoppingCartSummaryPageLocators.SUBTOTAL).text
        else:
            return "Product was not found"

    def click_checkout_button(self):
        self.driver.find_element(*ShoppingCartSummaryPageLocators.PROCEED_TO_CHECKOUT_BUTTON).click()

    def increaseQuanityByOne(self, productName):
        product_element = self.getProductFromSummaryPage(productName)
        if product_element:
            wait(product_element, 10).until(EC.element_to_be_clickable(ShoppingCartSummaryPageLocators.INCREASE_QTY)).click()

    def deleteItem(self, productName):
        product_element = self.getProductFromSummaryPage(productName)
        if product_element:
            wait(product_element, 10).until(EC.element_to_be_clickable(ShoppingCartSummaryPageLocators.DELETE)).click()

class AddressPage(BasePage):

    add_order_comment = OrderComment()
    new_address_firstname = NewAddressFirstName()
    new_address_lastname = NewAddressLastName()
    new_address_company = NewAddressCompany()
    new_address_address1 = NewAddressAddress1()
    new_address_address2 = NewAddressAddress2()
    new_address_city = NewAddressCity()
   
    new_address_postal_code = NewAddressPostalCode()
    new_address_home_phone = NewAddressHomePhone()
    new_address_mobile_phone = NewAddressMobilePhone()
    new_address_additional = NewAddressAdditional()
    new_address_title = NewAddressTitle()

    def proceedToCheckout(self):
        self.driver.find_element(*AddressPageLocators.PROCEED_TO_CHECKOUT_BUTTON).click()

    def hasChooseBillingAddressMenu(self):
        self.driver.implicitly_wait(3)
        billing_address = self.driver.find_element(*AddressPageLocators.BILLING_ADDRESS_FORM)
        if billing_address.get_attribute("style") == 'display: none;':
            return False
        else:
            return True

    def chooseDeliveryAddress(self, addressLabel):
        select = Select(self.driver.find_element(*AddressPageLocators.DELIVERY_ADDRESS_DROP_DOWN))  
        select.select_by_visible_text(addressLabel)

    def newAddressState(self, stateName):
        select = Select(self.driver.find_element(*AddressPageLocators.NEW_ADDRESS_STATE))  
        select.select_by_visible_text(stateName)

    def useDeliveryAddressAsBillingAddress(self, bool_flag):
        checkbox = self.driver.find_element(*AddressPageLocators.USE_SAME_ADDRESS)
        if checkbox.get_attribute("checked") == "true":
            if not bool_flag:
                checkbox.click()
    
    def clickAddNewAddressButton(self):
        self.driver.find_element(*AddressPageLocators.ADD_NEW_ADDRESS).click()

    def saveAddress(self):
        self.driver.find_element(*AddressPageLocators.SAVE_ADDRESS).click()

    def clickUpdateDeliveryAddress(self):
        self.driver.find_element(*AddressPageLocators.UPDATE_DELIVERY_ADDRESS).click()

    def clickUpdateBillingAddress(self):
        self.driver.find_element(*AddressPageLocators.UPDATE_BILLING_ADDRESS).click()
        
        

class ShippingPage(BasePage):

    def click_checkout_button(self):
        self.driver.find_element(*ShippingPageLocators.PROCEED_TO_CHECKOUT_BUTTON).click()

    def click_terms_of_service(self):
        self.driver.find_element(*ShippingPageLocators.TOS).click()

    def mustAgreeToTOSDisplay(self):
        return "You must agree to the terms of service before continuing." in self.driver.page_source

class PaymentPage(BasePage):
    
    def payByBankWire(self):
        self.driver.find_element(*PaymentPageLocators.PAY_BY_BANK_WIRE).click()

    def payByCheck(self):
        wait(self.driver, 10).until(EC.element_to_be_clickable(PaymentPageLocators.PAY_BY_CHECK)).click()

    def chooseDifferntMethodOfPayment(self):
        self.driver.find_element(*PaymentPageLocators.OTHER_PAYMENTS_METHODS).click()

    def confirmOrder(self):
        element = self.driver.find_element(*PaymentPageLocators.CONFIRM_ORDER).click()

class OrderConfirmationPage(BasePage):
    
    def getOrderReferenceForBankWire(self):
        temp = self.driver.find_element(*OrderConforimationPageLocators.ORDER_BOX).get_attribute("innerHTML")
        data = [item.strip() for item in temp.split("<br>")]
        return data[5].split()[-8]

    def getOrderReferenceForCheck(self):
        temp = self.driver.find_element(*OrderConforimationPageLocators.ORDER_BOX).get_attribute("innerHTML")
        data = [item.strip() for item in temp.split("<br>")]
        return data[3].split()[-1].strip('.')
    

    def backToOrders(self):
        element = self.driver.find_element(*OrderConforimationPageLocators.BACK_TO_ORDERS).click()

class OrderHistoryPage(BasePage):

    def findOrder(self, orderReference):
        found = False
        orders_reference = self.driver.find_elements(*OrderHistoryPageLocators.ORDERS_REF_LIST)
        for order in orders_reference:
            if orderReference == order.text:
                found =  True
        return found



