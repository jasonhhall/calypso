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
            # button = element.find_element(By.CLASS_NAME, 'ajax_add_to_cart_button')
            # print(button.text)
            # button.click()
            # button.click()
            action=ActionChains(driver)
            action.move_to_element(element).perform()
            addToCartButton = wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ajax_add_to_cart_button')))
            addToCartButton.click()

        
            # proceed_to_checkout = driver.find_element(By.CLASS_NAME, 'button-container')
            # proceed_to_checkout_button  = wait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))


            # proceed_to_checkout_button  =  proceed_to_checkout.find_element(By.TAG_NAME, 'a')
            # addToCartPopup = wait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'layer_cart')))
            # addToCartPopup.find_element(By.CLASS_NAME, 'continue')
            # continue_shopping = addToCartPopup.find_element(By.CLASS_NAME, 'continue')
            # continue_shopping.click()
         
            # proceed_to_checkout_button.click()
          
            # message = addToCartPopup.find_element(By.TAG_NAME, 'h2')
            # print(message.text)
           
            
            # continue_shopping.click()

            # proceed_to_checkout = addToCartPopup.find_element(By.TAG_NAME, 'a')
            # proceed_to_checkout.click()






# for element in elements:
#     element2 = element.find_element(By.CLASS_NAME, 'product-name')
#     print(element2.text)

# for element in elements:
#     button = element.find_element(By.CLASS_NAME, 'ajax_add_to_cart_button')
#     print(button.text)


addItemToCart(driver, 'Faded Short Sleeve T-shirts')
time.sleep(10)
driver.close()