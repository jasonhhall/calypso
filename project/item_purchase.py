import os
import sys
import time
import unittest
import pytest
import settings
from selenium import webdriver
from scripts.pages import page

WEB_DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "webdrivers")
sys.path.append(WEB_DRIVER_PATH)

class ItemPurchaseWorkFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(os.path.join(WEB_DRIVER_PATH, "chromedriver.exe"))
        self.driver.get("http://automationpractice.com")

    def test_item_purchase(self):

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.addItemToCart('Faded Short Sleeve T-shirts')
        main_page.proceedToCheckout()

        shopping_cart_summary_page = page.ShoppingCartSummaryPage(self.driver)
        assert shopping_cart_summary_page.is_title_matches_shopping_cart_summary_page()
        item_name = shopping_cart_summary_page.getItemsDescription()
        print(item_name.text)
        # shopping_cart_summary_page.click_checkout_button()

        # auth_page = page.AuthenticationPage(self.driver)
        # assert auth_page.is_title_matches_auth_page()
        # auth_page.emailAddressInputElement = settings.EMAIL_ADDRESS
        # auth_page.emailPasswordInputElement = settings.EMAIL_PASSWORD
        # auth_page.click_signin_button()

        # address_page = page.AddressPage(self.driver)
        # address_page.click_checkout_button()

        # shipping_page = page.ShippingPage(self.driver)
        # shipping_page.click_terms_of_service()
        # shipping_page.click_checkout_button()

        # payment_page = page.PaymentPage(self.driver)
        # payment_page.payByBankWire()
        # payment_page.chooseDifferntMethodOfPayment()
        # payment_page.payByCheck()
        # payment_page.confirmOrder()

        # order_confirmation_page = page.OrderConfirmationPage(self.driver)
        # order_confirmation_page.backToOrders()
    





        # main_page.continueShopping()
        # main_page.click_signin_menu()
        # auth_page = page.AuthenticationPage(self.driver)
        # assert auth_page.is_title_matches_auth_page()
        # auth_page.emailAddressInputElement = settings.EMAIL_ADDRESS
        # auth_page.emailPasswordInputElement = settings.EMAIL_PASSWORD
        # auth_page.click_signin_button()
        # assert auth_page.is_signout_visible()
        # assert auth_page.is_user_account_visible()
        # auth_page.click_signout_button()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

