'''
Challenge Analyze The Northwind Dataset using pandas
'''

import pandas as pd

### 1) Get the names and the quantities in stock for each product.
# Read the products data
products = pd.read_csv('data/products.csv')
products[['productName', 'unitsInStock']]


### 2) Get a list of current products (Product ID and name).
products[products['discontinued']==0][['productID', 'productName']]


### 3) Get a list of the most and least expensive products (name and unit price).
most_expensive_product = products['unitPrice'] == products['unitPrice'].max()
least_expensive_product = products['unitPrice'] == products['unitPrice'].min()
condition = (most_expensive_product | least_expensive_product)
products[condition]


### 4) Get products that cost less than $20.
less_than_twenty = products['unitPrice'] < 20
products[less_than_twenty][['productName', 'unitPrice']]


### 5) Get products that cost between $15 and $25.
between_fifteen_twentyfive = products['unitPrice'].between(15, 25)
products[between_fifteen_twentyfive][['productName', 'unitPrice']]


### 6) Get products above average price.
average_price = products['unitPrice'].mean()
above_average_price = products['unitPrice'] > average_price
products[above_average_price][['productName', 'unitPrice']]


### 7) Find the ten most expensive products.
products.sort_values(by='unitPrice', ascending=False).head(10)


### 8) Get a list of discontinued products (Product ID and name).
products[products['discontinued']==1][['productID', 'productName']]


### 9) Count current and discontinued products.
products.groupby('discontinued').size()


### 10) Find products with less units in stock than the quantity on order.
# Herefore we will need the order_details data as well
order_details = pd.read_csv('data/order_details.csv')
order_details.head()

# Sum up the quantity of orders by product
orders_per_product = order_details.groupby('productID')['quantity'].sum()

# Join the products DataFrame with the orders_per_product
products_orders = products.join(orders_per_product)
products_orders['excess_orders'] = products_orders['quantity'] - products_orders['unitsInStock']

products_orders[products_orders['excess_orders'] < 0]


### 11) Find the customer who had the highest order amount
# For this wee need the customer data and the order data
customers = pd.read_csv('data/customers.csv')
customers.head()

orders = pd.read_csv('data/orders.csv')
orders.head()

# Join orders and customers
join_orders_customers = orders.merge(customers, on='customerID', how='left')

# Join orders_customers and order_details
join_orders_customers_details = order_details.merge(join_orders_customers, on='orderID')

# Create column order amount
join_orders_customers_details['order_amount'] = join_orders_customers_details['quantity'] * \
                                                    join_orders_customers_details['unitPrice'] * \
                                                    (1-join_orders_customers_details['discount'])

# Sum by customer
join_orders_customers_details.groupby('customerID')[['companyName', 'order_amount']]\
    .agg({'companyName': 'max', 'order_amount': 'sum'}).sort_values(by='order_amount', ascending=False)


### 12) Get orders for a given employee and the according customer
# We need the employees data
employees = pd.read_csv('data/employees.csv')
employees.head()
employees.shape

# Join employees and orders
join_orders_employees = orders.merge(employees, on='employeeID')
join_orders_employees[join_orders_employees['employeeID']==1]


### 13) Find the hiring age of each employee
employees.head()

employees['hiring_age'] = ((pd.to_datetime(employees['hireDate']) - pd.to_datetime(employees['birthDate'])).\
                            values/1000/1000/1000/60/60/24/365).astype(int)
                            # nano-to-micro/-to-milli/-to-seconds/-to-minutes/-to-hours
employees