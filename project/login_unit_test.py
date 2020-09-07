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

class LoginWorkFlow(unittest.TestCase):

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
        

    def test_log_in_with_incorrect_username_and_incorrect_password(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.click_signin_menu()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.emailAddressInputElement = "bademail@email.com"
        auth_page.emailPasswordInputElement = "badpassword"
        auth_page.click_signin_button()
        assert 'Authentication failed.' == auth_page.get_banner_alert_message()

    def test_log_in_with_valid_username_and_empty_password(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.click_signin_menu()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.emailAddressInputElement = settings.EMAIL_ADDRESS
        auth_page.emailPasswordInputElement = ""
        auth_page.click_signin_button()
        assert 'Password is required.' == auth_page.get_banner_alert_message()

    def test_log_in_with_empty_username_and_empty_password(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.click_signin_menu()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.emailAddressInputElement = ""
        auth_page.emailPasswordInputElement = ""
        auth_page.click_signin_button()
        assert 'An email address required.' == auth_page.get_banner_alert_message()

    def test_log_in_handles_case_sensitive(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.click_signin_menu()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.emailAddressInputElement = settings.EMAIL_ADDRESS
        auth_page.emailPasswordInputElement = settings.EMAIL_PASSWORD.swapcase()
        auth_page.click_signin_button()
        assert 'Authentication failed.' == auth_page.get_banner_alert_message()

    # def test_log_in_authentication(self):
    #     main_page = page.MainPage(self.driver)
    #     assert main_page.is_title_matches_main_page()
    #     main_page.click_signin_menu()
    #     auth_page = page.AuthenticationPage(self.driver)
    #     assert auth_page.is_title_matches_auth_page()
    #     auth_page.emailAddressInputElement = settings.EMAIL_ADDRESS
    #     auth_page.emailPasswordInputElement = settings.EMAIL_PASSWORD
    #     auth_page.click_signin_button()
    #     assert auth_page.is_signout_visible()
    #     assert auth_page.is_user_account_visible()
    #     auth_page.click_signout_button()
    #     self.driver.back()
    #     self.driver.implicitly_wait(3)
    #     # assert auth_page.is_signin_visible()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

