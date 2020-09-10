from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
import os

load_dotenv()
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

EMAIL_ADDRESS = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("PASSWORD")

# TEST CASES TEST DATA
DELIVERY_ADDRESS_LABEL = 'Home address'
DELIVERY_ADDRESS_LABEL2 = 'Office Address'
ORDER_COMMENT = 'Please leave package on the front porch.'
HOME_ADDRESS1 = '345 MAIN ST.'
HOME_ADDRESS2 = 'APT 1'
HOME_CITY = 'Nashville'
HOME_STATE = 'Tennessee'
HOME_PHONE = '800-555-1111'
POSTAL_CODE = '37000'
OFFICE_ADDRESS1 = '345 SECOND ST.'
OFFICE_ADDRESS2 = 'SUITE 501'
OFFICE_CITY = 'Nashville'
OFFICE_STATE = 'Tennessee'
OFFICE_PHONE = '800-555-1111'
MOBILE_PHONE = '555-111-4444'
OFFICE_POSTAL_CODE = '37000'
HOME_ADDITIONAL_INFO = 'Email Address johndoe@test.com'
ITEM1_DESCRIPTION = 'Blouse'
ITEM1_PRICE = '$27.00'
ITEM1_SIZE = 'S'
ITEM1_COLOR = 'Black'
ITEM2_DESCRIPTION = 'Faded Short Sleeve T-shirts'
ITEM2_PRICE = '$16.51'
ITEM2_SIZE = 'L'
ITEM2_COLOR = 'Blue'
ITEM3_DESCRIPTION = 'Faded Short Sleeve T-shirts'
ITEM3_PRICE = '$16.51'
ITEM3_SIZE = 'S'
ITEM3_COLOR = 'Orange'
