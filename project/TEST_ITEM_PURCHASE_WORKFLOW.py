import os
import sys
import time
import unittest
from selenium import webdriver
import settings
from scripts.pages import page

WEB_DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "webdrivers")
sys.path.append(WEB_DRIVER_PATH)


class ItemPurchaseWorkFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(os.path.join(WEB_DRIVER_PATH, "chromedriver.exe"))
        self.driver.get("http://automationpractice.com")

    def test_add_item_to_cart_and_checkout_using_bank_wire(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.add_item_to_cart(settings.ITEM1_DESCRIPTION)
        assert main_page.was_item_successfully_added_to_cart()
        main_page.proceed_to_checkout()
        shopping_cart_summary_page = page.ShoppingCartSummaryPage(self.driver)
        shopping_cart_summary_page.increase_quantity_by_one(settings.ITEM1_DESCRIPTION)
        shopping_cart_summary_page.click_checkout_button()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.email_address_input_element = settings.EMAIL_ADDRESS
        auth_page.email_password_input_element = settings.EMAIL_PASSWORD
        auth_page.click_signin_button()
        address_page = page.AddressPage(self.driver)
        address_page.choose_delivery_address(settings.DELIVERY_ADDRESS_LABEL)
        address_page.use_delivery_address_as_billing_address(True)
        address_page.add_order_comment = settings.ORDER_COMMENT
        address_page.click_update_delivery_address()
        time.sleep(2)
        address_page.new_address_address1 = settings.HOME_ADDRESS1
        address_page.new_address_address2 = settings.HOME_ADDRESS2
        address_page.new_address_city = settings.HOME_CITY
        address_page.new_address_state(settings.HOME_STATE)
        address_page.new_address_postal_code = settings.POSTAL_CODE
        address_page.new_address_home_phone = settings.HOME_PHONE
        address_page.new_address_mobile_phone = settings.MOBILE_PHONE
        address_page.new_address_additional = settings.HOME_ADDITIONAL_INFO
        address_page.save_address()
        assert address_page.verify_delivery_address(settings.HOME_ADDRESS1, settings.HOME_ADDRESS2,
                                                    settings.HOME_CITY, settings.HOME_STATE, settings.POSTAL_CODE,
                                                    settings.HOME_PHONE, settings.MOBILE_PHONE)

        assert address_page.verify_billing_address(settings.HOME_ADDRESS1, settings.HOME_ADDRESS2,
                                                   settings.HOME_CITY, settings.HOME_STATE, settings.POSTAL_CODE,
                                                   settings.HOME_PHONE, settings.MOBILE_PHONE)
        address_page.proceed_to_checkout()
        shipping_page = page.ShippingPage(self.driver)
        shipping_page.click_terms_of_service()
        shipping_page.click_checkout_button()
        payment_page = page.PaymentPage(self.driver)
        assert payment_page.verify_order_details(settings.ITEM1_DESCRIPTION, settings.ITEM1_PRICE, "2", 0)
        payment_page.pay_by_bank_wire()
        order_summary_page = page.OrderSummaryPage(self.driver)
        order_summary_page.confirm_order()
        order_confirmation_page = page.OrderConfirmationPage(self.driver)
        order_reference_id = order_confirmation_page.get_order_reference_for_bank_wire()
        order_confirmation_page.back_to_orders()
        order_history_page = page.OrderHistoryPage(self.driver)
        assert order_history_page.find_order(order_reference_id)

    def test_add_item_to_cart_and_checkout_using_bank_check(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.add_item_to_cart(settings.ITEM1_DESCRIPTION)
        assert main_page.was_item_successfully_added_to_cart()
        main_page.continue_shopping()
        main_page.add_item_to_cart(settings.ITEM2_DESCRIPTION)
        assert main_page.was_item_successfully_added_to_cart()
        main_page.proceed_to_checkout()
        shopping_cart_summary_page = page.ShoppingCartSummaryPage(self.driver)
        shopping_cart_summary_page.delete_item_from_cart(settings.ITEM2_DESCRIPTION)
        shopping_cart_summary_page.click_checkout_button()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.email_address_input_element = settings.EMAIL_ADDRESS
        auth_page.email_password_input_element = settings.EMAIL_PASSWORD
        auth_page.click_signin_button()
        address_page = page.AddressPage(self.driver)
        address_page.choose_delivery_address(settings.DELIVERY_ADDRESS_LABEL2)
        address_page.use_delivery_address_as_billing_address(False)
        assert address_page.has_choose_billing_address_drop_down_menu()
        address_page.add_order_comment = settings.ORDER_COMMENT

        address_page.click_update_billing_address()
        time.sleep(2)
        address_page.new_address_address1 = settings.OFFICE_ADDRESS1
        address_page.new_address_address2 = settings.OFFICE_ADDRESS2
        address_page.new_address_city = settings.OFFICE_CITY
        address_page.new_address_state(settings.OFFICE_STATE)
        address_page.new_address_postal_code = settings.OFFICE_POSTAL_CODE
        address_page.new_address_home_phone = settings.OFFICE_PHONE
        address_page.new_address_mobile_phone = settings.MOBILE_PHONE
        address_page.save_address()
        assert address_page.verify_billing_address(settings.OFFICE_ADDRESS1, settings.OFFICE_ADDRESS2,
                                                   settings.OFFICE_CITY, settings.OFFICE_STATE, settings.OFFICE_POSTAL_CODE,
                                                   settings.OFFICE_PHONE, settings.MOBILE_PHONE)
        address_page.proceed_to_checkout()
        shipping_page = page.ShippingPage(self.driver)
        shipping_page.click_terms_of_service()
        shipping_page.click_checkout_button()
        payment_page = page.PaymentPage(self.driver)
        assert payment_page.verify_order_details(settings.ITEM1_DESCRIPTION, settings.ITEM1_PRICE, "1", 0)
        payment_page.pay_by_check()
        order_summary_page = page.OrderSummaryPage(self.driver)
        order_summary_page.confirm_order()
        order_confirmation_page = page.OrderConfirmationPage(self.driver)
        order_reference_id = order_confirmation_page.get_order_reference_for_check()
        order_confirmation_page.back_to_orders()
        order_history_page = page.OrderHistoryPage(self.driver)
        assert order_history_page.find_order(order_reference_id)

    def test_user_must_sign_in_to_complete_purchase(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.add_item_to_cart(settings.ITEM1_DESCRIPTION)
        assert main_page.was_item_successfully_added_to_cart()
        main_page.proceed_to_checkout()
        shopping_cart_summary_page = page.ShoppingCartSummaryPage(self.driver)
        shopping_cart_summary_page.increase_quantity_by_one(settings.ITEM1_DESCRIPTION)
        shopping_cart_summary_page.click_checkout_button()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()

    def test_user_must_accept_terms_of_service_to_complete_purchase(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.add_item_to_cart(settings.ITEM1_DESCRIPTION)
        assert main_page.was_item_successfully_added_to_cart()
        main_page.proceed_to_checkout()
        shopping_cart_summary_page = page.ShoppingCartSummaryPage(self.driver)
        shopping_cart_summary_page.increase_quantity_by_one(settings.ITEM1_DESCRIPTION)
        shopping_cart_summary_page.click_checkout_button()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.email_address_input_element = settings.EMAIL_ADDRESS
        auth_page.email_password_input_element = settings.EMAIL_PASSWORD
        auth_page.click_signin_button()
        address_page = page.AddressPage(self.driver)
        address_page.proceed_to_checkout()
        shipping_page = page.ShippingPage(self.driver)
        shipping_page.click_checkout_button()
        assert shipping_page.did_term_of_service_error_display()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()
