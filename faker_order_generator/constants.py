# Constants for Black Friday logic
BLACK_FRIDAY_MONTH = 11
BLACK_FRIDAY_START_DAY = 1
BLACK_FRIDAY_WEEK = 4

# Constants for product data generation
WEIGHTS_COUPON_APPLIED = [0.7, 0.3]
WEIGHTS_PAYMENT_METHODS = [0.75, 0.05, 0.05, 0.05, 0.05, 0.05]
WEIGHTS_SHIPPING_METHOD = [0.7, 0.2, 0.1]
WEIGHTS_SUBSCRIBER_USER = [0.5, 0.5]

# Constants for order data generation
MAX_DELAY_EVENTS = 1
MIN_DELAY_EVENTS = 0.1
MAX_NUM_ITEMS_PER_USER = 10
MAX_NUMBER_USERS = 50
PRODUCTS_JSON_FILE = (
    'faker_order_generator/faker_order_generator/products.json'
)
TOTAL_ORDERS = 1000
