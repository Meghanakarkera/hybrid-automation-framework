import requests

BASE_URL = "https://fakestoreapi.com"

# GET products
def get_products():
    response = requests.get(f"{BASE_URL}/products")
    return response

# POST product
def create_product(payload):
    response = requests.post(f"{BASE_URL}/products", json=payload)
    return response