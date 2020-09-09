import os
import sys
import time
import settings
from scripts.pages import page
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait as wait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WEB_DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "webdrivers")
driver = webdriver.Chrome(os.path.join(WEB_DRIVER_PATH, "chromedriver.exe"))
driver.get("http://automationpractice.com")

ITEM_TO_PURCAHSE = 'Printed Summer Dress'
main_page = page.MainPage(driver)
main_page.addItemToCart(ITEM_TO_PURCAHSE)
main_page.proceedToCheckout()
        
shopping_cart_summary_page = page.ShoppingCartSummaryPage(driver)
shopping_cart_summary_page.increaseQuanityByOne(ITEM_TO_PURCAHSE)
# price = shopping_cart_summary_page.getUnitPrice(ITEM_TO_PURCAHSE)
# print(price)
# total = shopping_cart_summary_page.getSubTotal(ITEM_TO_PURCAHSE)
# print(total)
# shopping_cart_summary_page.deleteItem(ITEM_TO_PURCAHSE)
shopping_cart_summary_page.click_checkout_button()

auth_page = page.AuthenticationPage(driver)
auth_page.emailAddressInputElement = settings.EMAIL_ADDRESS
auth_page.emailPasswordInputElement = settings.EMAIL_PASSWORD
auth_page.click_signin_button()

address_page = page.AddressPage(driver)
address_page.chooseDeliveryAddress('Office Address')
address_page.useDeliveryAddressAsBillingAddress(True)
# print(address_page.hasChooseBillingAddressMenu())
address_page.add_order_comment = "Please leave package on the porch"
address_page.addNewAddress("FN", "LN", "C","123", address2="", city="City", state="Tennessee", zip="37013",homePhone="555-444-3333", mobilePhone="800-555-0000", AdditionalInfo="ADD", addressTitle="My Address")
# address_page.click_checkout_button()

# shipping_page = page.ShippingPage(driver)
# shipping_page.click_terms_of_service()
# shipping_page.click_checkout_button()

# payment_page = page.PaymentPage(driver)
# payment_page.payByBankWire()
# payment_page.chooseDifferntMethodOfPayment()
# payment_page.payByCheck()
# payment_page.confirmOrder()

# order_confirmation_page = page.OrderConfirmationPage(driver)
# conf_num = order_confirmation_page.getOrderReference()
# print(conf_num)

# order_confirmation_page.backToOrders()

# order_history_page = page.OrderHistoryPage(driver)
# print(order_history_page.findOrder(conf_num))





time.sleep(10)
driver.close()