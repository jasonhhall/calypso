import os
import sys
import time
import unittest
from project import settings
from selenium import webdriver
from project.scripts.pages import page

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
        auth_page.email_address_input_element = settings.EMAIL_ADDRESS
        auth_page.email_password_input_element = settings.EMAIL_PASSWORD
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
        auth_page.email_address_input_element = "bademail@email.com"
        auth_page.email_password_input_element = "badpassword"
        auth_page.click_signin_button()
        assert 'Authentication failed.' == auth_page.get_banner_alert_message()

    def test_log_in_with_valid_username_and_empty_password(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.click_signin_menu()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.email_address_input_element = settings.EMAIL_ADDRESS
        auth_page.email_password_input_element = ""
        auth_page.click_signin_button()
        assert 'Password is required.' == auth_page.get_banner_alert_message()

    def test_log_in_with_empty_username_and_empty_password(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.click_signin_menu()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.email_address_input_element = ""
        auth_page.email_password_input_element = ""
        auth_page.click_signin_button()
        assert 'An email address required.' == auth_page.get_banner_alert_message()

    def test_log_in_handles_case_sensitive(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches_main_page()
        main_page.click_signin_menu()
        auth_page = page.AuthenticationPage(self.driver)
        assert auth_page.is_title_matches_auth_page()
        auth_page.email_address_input_element = settings.EMAIL_ADDRESS
        auth_page.email_password_input_element = settings.EMAIL_PASSWORD.swapcase()
        auth_page.click_signin_button()
        assert 'Authentication failed.' == auth_page.get_banner_alert_message()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

