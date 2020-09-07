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

    def test_log_in_with_valid_username_and_valid_password(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.click_signin_menu()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.emailAddressInputElement = settings.EMAIL_ADDRESS
        auth_page.emailPasswordInputElement = settings.EMAIL_PASSWORD
        auth_page.click_signin_button()
        assert auth_page.is_signout_visible()
        assert auth_page.is_user_account_visible()
        auth_page.click_signout_button()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

