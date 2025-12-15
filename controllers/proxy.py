from fastapi import FastAPI
from utils.cache import get_cache, set_cache
import requests

app = FastAPI()

@app.get("/products")
def get_products():

    cache_key = "products"

    cached = get_cache(cache_key)

    if cached:
        print("🟢 CACHE HIT")
        return cached
    
    print("🔴 CACHE MISS")

    api_url = 'https://dummyjson.com/products'
    response= requests.get(api_url).json()

    set_cache(cache_key, response, ttl=60)

    return response