print("=== DUMMY JSON ASSIGNMENT ===")

import requests
import pandas as pd
#1). Fetch data from a public API and display it in a readable format.

# Products API from Dummy JSON
products_url = "https://dummyjson.com/products"
products_response = requests.get(products_url)
print(products_response.status_code)

#To get data, I used .json() method
products_data = products_response.json()
print(products_data)

products = products_data['products']
products_df = pd.DataFrame(products)
print(products_df)

#converting the data to a csv file
products_df.to_csv("products_data.csv", index=False)

#====================================

#Cart API from Dummy JSON

cart_url = "https://dummyjson.com/carts"
cart_response = requests.get(cart_url)
print(cart_response.status_code)

#To get data, I used .json() method
carts_data = cart_response.json()
print(carts_data)

carts = carts_data['carts']
carts_df = pd.DataFrame(carts)
print(carts_df)

#converting the data to a csv file
carts_df.to_csv("carts_data.csv", index=False)