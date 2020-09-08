import os
import sys
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


WEB_DRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "webdrivers")

driver = webdriver.Chrome(os.path.join(WEB_DRIVER_PATH, "chromedriver.exe"))
driver.get("http://automationpractice.com")

def addItemToCart( driver, itemName):
    elements = driver.find_elements(By.XPATH, '//*[@id="homefeatured"]/li')
    for element in elements:
        if itemName == element.find_element(By.CLASS_NAME, 'product-name').text:
            action=ActionChains(driver)
            action.move_to_element(element).perform()
            addToCartButton = wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ajax_add_to_cart_button')))
            addToCartButton.click()
            proceed_to_checkout_button = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')))
            proceed_to_checkout_button.click()


# for element in elements:
#     element2 = element.find_element(By.CLASS_NAME, 'product-name')
#     print(element2.text)

# for element in elements:
#     button = element.find_element(By.CLASS_NAME, 'ajax_add_to_cart_button')
#     print(button.text)


addItemToCart(driver, 'Faded Short Sleeve T-shirts')
time.sleep(10)
driver.close()