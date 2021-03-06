from scripts.element import BasePageElement
from scripts.locators import MainPageLocators, AuthenticationPageLocators, ShoppingCartSummaryPageLocators, AddressPageLocators 
from scripts.locators import ShippingPageLocators, PaymentPageLocators, OrderConfirmationPageLocators, OrderHistoryPageLocators, OrderSummaryPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC



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

    def was_item_successfully_added_to_cart(self):
        popup_window = self.driver.find_element(*MainPageLocators.POPUP_PANEL)
        text = popup_window.find_element(*MainPageLocators.POPUP_PANEL_CONFIRMATION).get_attribute("innerHTML")
        data = [item.strip() for item in text.split("</i>")]
        return "Product successfully added to your shopping cart" in data[1]

    def proceed_to_checkout(self):
        proceed_to_checkout_button = wait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.PROCEED_TO_CHECKOUT_BUTTON))
        proceed_to_checkout_button.click()

    def continue_shopping(self):
        continue_shopping = wait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.CONTINUE_SHOPPING))
        continue_shopping.click()

    def add_item_to_cart(self, item_name):
        products = self.driver.find_elements(*MainPageLocators.ITEM_LIST)
        for product in products:
            if item_name == product.find_element(*MainPageLocators.PRODUCT_NAME).get_attribute('title'):
                action = ActionChains(self.driver)
                action.move_to_element(product).perform()
                wait(product, 10).until(EC.element_to_be_clickable(MainPageLocators.ADD_TO_CART_BUTTON)).click()

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
        wait(self.driver, 10).until(EC.element_to_be_clickable(AuthenticationPageLocators.SIGN_IN_BUTTON)).click()

    def click_signout_button(self):
        self.driver.find_element(*AuthenticationPageLocators.SIGN_OUT_MENU).click()

    def get_banner_alert_message(self):
        element = self.driver.find_element(*AuthenticationPageLocators.ALERT_BANNER)
        return element.text


class ShoppingCartSummaryPage(BasePage):

    def is_title_matches_shopping_cart_summary_page(self):
        return "Order - My Store" in self.driver.title

    def get_product_from_summary_page(self, product_name):
        products = self.driver.find_elements(*ShoppingCartSummaryPageLocators.PRODUCTS)
        for product in products:
            product_description = product.find_element(*ShoppingCartSummaryPageLocators.PRODUCT_NAME).text
            if product_description == product_name:
                return product
        return None

    def get_unit_price(self, product_name):
        product_element = self.get_product_from_summary_page(product_name)
        if product_element:
            return product_element.find_element(*ShoppingCartSummaryPageLocators.UNIT_PRICE).text
        else:
            return "Product was not found"

    def get_sub_total(self, product_name):
        product_element = self.get_product_from_summary_page(product_name)
        if product_element:
            return product_element.find_element(*ShoppingCartSummaryPageLocators.SUBTOTAL).text
        else:
            return "Product was not found"

    def click_checkout_button(self):
        self.driver.find_element(*ShoppingCartSummaryPageLocators.PROCEED_TO_CHECKOUT_BUTTON).click()

    def increase_quantity_by_one(self, product_name):
        product_element = self.get_product_from_summary_page(product_name)
        if product_element:
            wait(product_element, 10).until(EC.element_to_be_clickable(ShoppingCartSummaryPageLocators.INCREASE_QTY)).click()

    def delete_item_from_cart(self, product_name):
        product_element = self.get_product_from_summary_page(product_name)
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

    def proceed_to_checkout(self):
        self.driver.find_element(*AddressPageLocators.PROCEED_TO_CHECKOUT_BUTTON).click()

    def has_choose_billing_address_drop_down_menu(self):
        self.driver.implicitly_wait(3)
        billing_address = self.driver.find_element(*AddressPageLocators.BILLING_ADDRESS_FORM)
        if billing_address.get_attribute("style") == 'display: none;':
            return False
        else:
            return True

    def choose_delivery_address(self, address_label):
        select = Select(self.driver.find_element(*AddressPageLocators.DELIVERY_ADDRESS_DROP_DOWN))  
        select.select_by_visible_text(address_label)

    def new_address_state(self, state_name):
        select = Select(self.driver.find_element(*AddressPageLocators.NEW_ADDRESS_STATE))  
        select.select_by_visible_text(state_name)

    def use_delivery_address_as_billing_address(self, bool_flag):
        checkbox = self.driver.find_element(*AddressPageLocators.USE_SAME_ADDRESS)
        if checkbox.get_attribute("checked") == "true":
            if not bool_flag:
                checkbox.click()
    
    def click_add_new_address_button(self):
        self.driver.find_element(*AddressPageLocators.ADD_NEW_ADDRESS).click()

    def save_address(self):
        self.driver.find_element(*AddressPageLocators.SAVE_ADDRESS).click()

    def click_update_delivery_address(self):
        self.driver.find_element(*AddressPageLocators.UPDATE_DELIVERY_ADDRESS).click()

    def click_update_billing_address(self):
        self.driver.find_element(*AddressPageLocators.UPDATE_BILLING_ADDRESS).click()

    def verify_delivery_address(self, address1, address2, city, state, postal_code, h_phone, m_phone):
        result = True
        address_info = self.driver.find_elements(*AddressPageLocators.DELIVERY_ADDRESS_BOX)
        full_street_address = address1 + " " + address2
        if address_info[2].text != full_street_address.strip():
            result = False
        if address_info[3].text != city + ", " + state + " " + postal_code:
            result = False
        if address_info[5].text != h_phone:
            result = False
        if address_info[6].text != m_phone:
            result = False
        return result

    def verify_billing_address(self, address1, address2, city, state, postal_code, h_phone, m_phone):
        result = True
        address_info = self.driver.find_elements(*AddressPageLocators.BILLING_ADDRESS_BOX)
        full_street_address = address1 + " " + address2
        if address_info[2].text != full_street_address.strip():
            result = False
        if address_info[3].text != city + ", " + state + " " + postal_code:
            result = False
        if address_info[5].text != h_phone:
            result = False
        if address_info[6].text != m_phone:
            result = False
        return result


class ShippingPage(BasePage):

    def click_checkout_button(self):
        self.driver.find_element(*ShippingPageLocators.PROCEED_TO_CHECKOUT_BUTTON).click()

    def click_terms_of_service(self):
        self.driver.find_element(*ShippingPageLocators.TOS).click()

    def did_term_of_service_error_display(self):
        return "You must agree to the terms of service before continuing." in self.driver.page_source


class PaymentPage(BasePage):
    def pay_by_bank_wire(self):
        self.driver.find_element(*PaymentPageLocators.PAY_BY_BANK_WIRE).click()

    def pay_by_check(self):
        wait(self.driver, 10).until(EC.element_to_be_clickable(PaymentPageLocators.PAY_BY_CHECK)).click()

    def verify_order_details(self, item_name, item_price, item_qty, item_index):
        result = True

        orders = self.driver.find_elements(*PaymentPageLocators.ORDERS)
        order = orders[item_index]
        description = order.find_element(*PaymentPageLocators.ORDER_DESCRIPTION).text
        unit_price = order.find_element(*PaymentPageLocators.ORDER_UNIT_PRICE).text
        qty = order.find_element(*PaymentPageLocators.ORDER_QTY).text
        total = order.find_element(*PaymentPageLocators.ORDER_TOTAL).text
        # This produces a float number as a string rounded to two decimal points.
        calculated_total = format(float(item_price.strip("$")) * int(item_qty), '.2f')

        if item_name != description:
            result = False
        if item_price.strip("$") != unit_price.strip("$"):
            result = False
        if int(item_qty) != int(qty):
            result = False
        if calculated_total != total.strip("$"):
            result = False
        return result


class OrderSummaryPage(BasePage):
    def confirm_order(self):
        self.driver.find_element(*OrderSummaryPageLocators.CONFIRM_ORDER).click()

    def choose_different_method_of_payment(self):
        self.driver.find_element(*PaymentPageLocators.OTHER_PAYMENTS_METHODS).click()


class OrderConfirmationPage(BasePage):
    
    def get_order_reference_for_bank_wire(self):
        temp = self.driver.find_element(*OrderConfirmationPageLocators.ORDER_BOX).get_attribute("innerHTML")
        data = [item.strip() for item in temp.split("<br>")]
        return data[5].split()[-8]

    def get_order_reference_for_check(self):
        temp = self.driver.find_element(*OrderConfirmationPageLocators.ORDER_BOX).get_attribute("innerHTML")
        data = [item.strip() for item in temp.split("<br>")]
        return data[3].split()[-1].strip('.')

    def back_to_orders(self):
        self.driver.find_element(*OrderConfirmationPageLocators.BACK_TO_ORDERS).click()


class OrderHistoryPage(BasePage):

    def find_order(self, order_reference):
        found = False
        orders_reference = self.driver.find_elements(*OrderHistoryPageLocators.ORDERS_REF_LIST)
        for order in orders_reference:
            if order_reference == order.text:
                found =  True
        return found



