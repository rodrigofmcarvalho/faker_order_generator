# Faker Order Generator

The `Faker Order Generator` module is designed to generate fake order data for e-commerce platforms. It simulates order details in a realistic manner, focusing on generating data specifically related to Black Friday sales.

![faker_order_generator](https://github.com/rodrigofmcarvalho/faker_order_generator/assets/96849660/5ec9b7b6-4ede-4c21-a992-d224edb41925)

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Components Description](#components-description)
    - [Constants](#constants)
    - [PaymentMethods Enum](#paymentmethods-enum)
    - [OrderDataSource Class](#orderdatasource-class)
- [Contributing](#contributing)
- [License](#license)

## Features

- Generates fake order data with realistic details.
- Focuses on Black Friday sales data generation.
- Allows specification of total orders, number of users, and maximum items per user.
- Outputs data in JSON format for ease of consumption.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10 or later.
- Install the required libraries: `Faker`, `dateutil`.

## Usage

To use the `faker_order_generator`, follow these steps:

1. Initialize the `OrderDataSource` class with the desired parameters.
2. Call the `source_random_order_data()` method on the initialized object to generate orders.

Example:

```python
source = OrderDataSource(
    TOTAL_ORDERS, MAX_NUMBER_USERS, MAX_NUM_ITEMS_PER_USER, PRODUCTS_JSON_FILE
)

for order_data in source.source_random_order_data():
    print(order_data)
```
## Configuration

Make sure to update the `constant.py` file according to your needs.

## Components Description

### Constants

The module contains constants that define aspects such as:

- Black Friday logic: Month, starting day, and the week it occurs.
- Weights for random choices like payment methods, shipping methods, etc.
- Max number of items per user, number of users, path to products' JSON file, and total orders to generate.

### PaymentMethods Enum

An enumeration representing various payment methods available for orders. It includes options like Credit Card, Debit Card, PayPal, etc.

### OrderDataSource Class

The primary class responsible for generating the order data. It offers methods to:

- Load product data from a JSON file.
- Calculate the next Black Friday date.
- Generate randomized product and shipping data based on order number and user ID.
- Produce the order data for each user in JSON format.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

## Author
Rodrigo Carvalho
