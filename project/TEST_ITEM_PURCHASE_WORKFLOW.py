import os
import sys
import time
import unittest
# import pytest
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
        shopping_cart_summary_page.increaseQuanityByOne(settings.ITEM1_DESCRIPTION)
        # shopping_cart_summary_page.click_checkout_button()
        # auth_page = page.AuthenticationPage(self.driver)
        # assert auth_page.is_title_matches_auth_page()
        # auth_page.email_address_input_element = settings.EMAIL_ADDRESS
        # auth_page.email_password_input_element = settings.EMAIL_PASSWORD
        # auth_page.click_signin_button()
        # address_page = page.AddressPage(self.driver)
        # address_page.chooseDeliveryAddress(settings.DELIVERY_ADDRESS_LABEL)
        # address_page.useDeliveryAddressAsBillingAddress(True)
        # address_page.add_order_comment = settings.ORDER_COMMENT
        # address_page.proceedToCheckout()
        # shipping_page = page.ShippingPage(self.driver)
        # shipping_page.click_terms_of_service()
        # shipping_page.click_checkout_button()
        # payment_page = page.PaymentPage(self.driver)
        # payment_page.payByBankWire()
        # order_summary_page = page.OrderSummaryPage(self.driver)
        # order_summary_page.confirmOrder()
        # order_confirmation_page = page.OrderConfirmationPage(self.driver)
        # order_reference_id = order_confirmation_page.getOrderReferenceForBankWire()
        # order_confirmation_page.backToOrders()
        # order_history_page = page.OrderHistoryPage(self.driver)
        # assert order_history_page.findOrder(order_reference_id)

    # def test_add_item_to_cart_and_checkout_using_bank_check(self):
    #     main_page = page.MainPage(self.driver)
    #     assert main_page.is_title_matches_main_page()
    #     main_page.addItemToCart(settings.ITEM2_DESCRIPTION)
    #     main_page.proceedToCheckout()
    #     shopping_cart_summary_page = page.ShoppingCartSummaryPage(self.driver)
    #     shopping_cart_summary_page.click_checkout_button()
    #     auth_page = page.AuthenticationPage(self.driver)
    #     assert auth_page.is_title_matches_auth_page()
    #     auth_page.email_address_input_element = settings.EMAIL_ADDRESS
    #     auth_page.email_password_input_element = settings.EMAIL_PASSWORD
    #     auth_page.click_signin_button()
    #     address_page = page.AddressPage(self.driver)
    #     address_page.chooseDeliveryAddress(settings.DELIVERY_ADDRESS_LABEL)
    #     address_page.useDeliveryAddressAsBillingAddress(True)
    #     address_page.add_order_comment = settings.ORDER_COMMENT
    #     address_page.proceedToCheckout()
    #     shipping_page = page.ShippingPage(self.driver)
    #     shipping_page.click_terms_of_service()
    #     shipping_page.click_checkout_button()
    #     payment_page = page.PaymentPage(self.driver)
    #     payment_page.payByBankWire()
    #     payment_page.chooseDifferntMethodOfPayment()
    #     payment_page.payByCheck()
    #     order_summary_page = page.OrderSummaryPage(self.driver)
    #     order_summary_page.confirmOrder()
    #     order_confirmation_page = page.OrderConfirmationPage(self.driver)
    #     order_reference_id = order_confirmation_page.getOrderReferenceForCheck()
    #     order_confirmation_page.backToOrders()
    #     order_history_page = page.OrderHistoryPage(self.driver)
    #     assert order_history_page.findOrder(order_reference_id)

    def tearDown(self):
        time.sleep(5)
        self.driver.close()
