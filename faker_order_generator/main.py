import sys

from constants import (
    MAX_NUM_ITEMS_PER_USER,
    MAX_NUMBER_USERS,
    PRODUCTS_JSON_FILE,
    TOTAL_ORDERS,
)
from order_data_source import OrderDataSource

if __name__ == '__main__':
    try:
        # Create an instance of OrderDataSource with specified numbers of total orders, users and items
        source = OrderDataSource(
            TOTAL_ORDERS,
            MAX_NUMBER_USERS,
            MAX_NUM_ITEMS_PER_USER,
            PRODUCTS_JSON_FILE,
        )
        for order_data in source.source_random_order_data():
            print(order_data)
    except KeyboardInterrupt:
        print('\n\n\nGracefully stopping generating order data...\n\n\n')
        sys.exit(0)
