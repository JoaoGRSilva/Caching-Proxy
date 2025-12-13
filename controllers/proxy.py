from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/products")
def get_products():

    api_url = 'https://dummyjson.com/products'
    all_products = requests.get(api_url).json()

    return all_products