from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SIGN_IN_MENU = (By.CLASS_NAME, 'login')
    SIGN_OUT_MENU = (By.CLASS_NAME, 'logout')
    ITEM_LIST = (By.XPATH, '//*[@id="homefeatured"]/li')
    PRODUCT_NAME = (By.CLASS_NAME, 'product-name')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'ajax_add_to_cart_button')
    POPUP_PANEL = (By.ID, 'layer_cart')
    POPUP_PANEL_CONFIRMATION = (By.XPATH, 'div[1]/div[1]/h2')
    # CONFIRMATION = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/h2')
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
    PRODUCTS = (By.XPATH, '//*[@id="cart_summary"]/tbody/tr')
    PRODUCT_NAME = (By.XPATH, 'td[2]/p/a')
    UNIT_PRICE = (By.CLASS_NAME, 'price')
    SUBTOTAL = (By.XPATH, 'td[6]/span')
    DELETE = (By.XPATH, 'td[7]/div/a')
    INCREASE_QTY = (By.XPATH, 'td[5]/div/a[2]')


class AddressPageLocators(object):
    PROCEED_TO_CHECKOUT_BUTTON = (By.NAME, 'processAddress')
    DELIVERY_ADDRESS_DROP_DOWN = (By.ID, 'id_address_delivery')
    BILLING_ADDRESS_DROP_DOWN = (By.ID, 'id_address_invoice')
    BILLING_ADDRESS_FORM = (By.ID, 'address_invoice_form')
    USE_SAME_ADDRESS = (By.ID, 'addressesAreEquals')
    ORDER_MESSAGE = (By.XPATH, '//*[@id="ordermsg"]/textarea')
    ADD_NEW_ADDRESS = (By.XPATH, '//*[@id="center_column"]/form/div/p/a')
    SAVE_ADDRESS = (By.ID, 'submitAddress')
    NEW_ADDRESS_STATE = (By.ID, 'id_state')
    UPDATE_DELIVERY_ADDRESS = (By.CSS_SELECTOR, '#address_invoice li.address_update a')
    UPDATE_BILLING_ADDRESS = (By.CSS_SELECTOR, '#address_invoice  li.address_update a')
    DELIVERY_ADDRESS_BOX = (By.XPATH, '//*[@id="address_delivery"]/li')
    BILLING_ADDRESS_BOX = (By.XPATH, '//*[@id="address_invoice"]/li')
   

class ShippingPageLocators(object):
    PROCEED_TO_CHECKOUT_BUTTON = (By.NAME, 'processCarrier')
    TOS = (By.ID, 'cgv')


class PaymentPageLocators(object):
    PAY_BY_BANK_WIRE = (By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a')
    PAY_BY_CHECK = (By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a')
    ORDERS = (By.XPATH, '//*[@id="cart_summary"]/tbody/tr')
    ORDER_DESCRIPTION = (By.XPATH, 'td[2]/p/a')
    ORDER_UNIT_PRICE = (By.XPATH, 'td[4]/span/span')
    ORDER_QTY = (By.XPATH, 'td[5]/span')
    ORDER_TOTAL = (By.XPATH, 'td[6]/span')




class OrderSummaryPageLocators(object):
    CONFIRM_ORDER = (By.XPATH, '//*[@id="cart_navigation"]/button')
    OTHER_PAYMENTS_METHODS = (By.XPATH, '//*[@id="cart_navigation"]/a')


class OrderConfirmationPageLocators(object):
    BACK_TO_ORDERS = (By.XPATH, '//*[@id="center_column"]/p/a')
    ORDER_BOX = (By.XPATH, '//*[@id="center_column"]/div')


class OrderHistoryPageLocators(object):
    ORDERS_REF_LIST = (By.XPATH, '//*[@id="order-list"]/tbody/tr/td[1]/a')

