import os
import sys
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def addItemToCart(self, itemName ):
        
        elements = self.driver.find_elements(By.XPATH, '//*[@id="homefeatured"]/li')

        for element in elements:
            # print(element)
            product_name = element.find_element(By.CLASS_NAME, 'product-name').text
           
            if itemName == product_name:
                 addToCartButton = wait(element, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ajax_add_to_cart_button')))
                 addToCartButton.click()

    def proceedToCheckout(self):
        proceed_to_checkout_button = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')))
        proceed_to_checkout_button.click()

class ShoppingCartSummaryPage(BasePage):

    def click_proceed_to_checkout_button(self):
        element = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="center_column"]/p[2]/a[1]')))
        element.click()

    def getUnitPrice(self):
        price = self.driver.find_element(By.XPATH, '//*[@id="cart_summary"]/tbody/tr[1]/td[4]/span').text
        return price

    def getTotal(self):
        driver = self.driver
        element = wait(driver, 100).until(
            lambda driver: driver.find_element((By.XPATH,'//*[@id="cart_summary"]/tbody/tr[1]/td[6]/span')))
        
        return element.text

        # return wait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="cart_summary"]/tbody/tr[1]/td[6]/span'))).text
        # return self.driver.find_element(By.XPATH, '//*[@id="cart_summary"]/tbody/tr[1]/td[6]/span').text

    def getQTY(self):
        qty = self.driver.find_element(By.XPATH, '//*[@id="cart_summary"]/tbody/tr[1]/td[5]/input[1]').get_attribute("value")
        return qty

    def increaseQuanityByOne(self):
        plus_sign_icon = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cart_summary"]/tbody/tr[1]/td[5]/div/a[2]')))
        plus_sign_icon.click()

    def reduceQuanityByOne(self):
        minus_sign = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cart_summary"]/tbody/tr[1]/td[5]/div/a[1]')))
        minus_sign.click()


    def removeItem(self):
        delete = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cart_summary"]/tbody/tr[1]/td[7]/div/a')))
        delete.click()
        alert = wait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="center_column"]/p'))).text
        if alert != 'Your shopping cart is empty.':
            raise Exception("Error removing item")



WEB_DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "webdrivers")

driver = webdriver.Chrome(os.path.join(WEB_DRIVER_PATH, "chromedriver.exe"))
driver.get("http://automationpractice.com")

main_page = MainPage(driver)
main_page.addItemToCart('Faded Short Sleeve T-shirts')
main_page.proceedToCheckout()

shopping_cart_page = ShoppingCartSummaryPage(driver)
# shopping_cart_page.click_proceed_to_checkout_button()
print(shopping_cart_page.getUnitPrice())
print(shopping_cart_page.getTotal())
shopping_cart_page.increaseQuanityByOne()
print(shopping_cart_page.getTotal())

# shopping_cart_page.removeItem()
# shopping_cart_page.click_proceed_to_checkout_button()

time.sleep(10)
driver.close()