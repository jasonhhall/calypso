from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SIGN_IN_MENU = (By.CLASS_NAME, 'login')
    SIGN_OUT_MENU = (By.CLASS_NAME, 'logout')
   
    ITEM_LIST = (By.XPATH, '//*[@id="homefeatured"]/li/div/div[2]/h5/a')
    # ITEM_LIST = (By.CSS_SELECTOR, '#homefeatured li a.product_img_link')
    # ITEM_TITLE = (By.XPATH, '//div/div[2]/h5/a')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'ajax_add_to_cart_button')
    POPUP_PANEL = (By.ID, 'layer_cart')
    CONFIRMATION = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/h2')
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
    CONTINUE_SHOPPING = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span')


class AuthenticationPageLocators(object):
    SIGN_IN_BUTTON = (By.ID, 'SubmitLogin')
    ALERT_BANNER = (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')
    SIGN_OUT_MENU = (By.CLASS_NAME, 'logout')
    USER_ACCOUNT = (By.CLASS_NAME, 'account')

class ShoppingCartSummaryPageLocators(object):
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')
    DELETE_ITEM = (By.XPATH, '//*[@id="cart_summary"]/tbody/tr/td[7]')
    QTY = (By.XPATH, '//*[@id="cart_summary"]/tbody/tr/td[5]')
    ITEMS_DESC = (By.XPATH, '//*[@id="cart_summary"]/tbody/tr/td[2]')
    ITEM_NAME = (By.TAG_NAME, 'a')


class AddressPageLocators(object):
    PROCEED_TO_CHECKOUT_BUTTON = (By.NAME, 'processAddress')

class ShippingPageLocators(object):
    PROCEED_TO_CHECKOUT_BUTTON = (By.NAME, 'processCarrier')
    TOS = (By.ID, 'cgv')

class PaymentPageLocators(object):
    PAY_BY_BANK_WIRE = (By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')
    PAY_BY_CHECK = (By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a')
    OTHER_PAYMENTS_METHODS = (By.XPATH, '//*[@id="cart_navigation"]/a')
    CONFIRM_ORDER = (By.XPATH, '//*[@id="cart_navigation"]/button')

class OrderConforimationPageLocators(object):
    BACK_TO_ORDERS = (By.XPATH, '//*[@id="center_column"]/p/a')

