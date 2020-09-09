from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
import os

load_dotenv()
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

EMAIL_ADDRESS = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("PASSWORD")

## TEST CASES TEST DATA
ITEM1_DESCRIPTION = 'Blouse'
ITEM1_PRICE = '$27.00'
ITEM1_SIZE = 'S'
ITEM1_COLOR = 'Black'
DELIVERY_ADDRESS_LABEL = 'Home Address'
ORDER_COMMENT = 'Please leave package on the front porch.'
