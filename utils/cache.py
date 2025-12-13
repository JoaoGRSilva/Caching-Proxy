import redis
from redis.cache import CacheConfig
from controllers import get_products

def check_cache():

    r = redis.Redis(host='localhost', port="6379", decode_responses = True)

    value = r.exists("products")

    if value == False:
        print("X-Cache: MISS")
        r.set(get_products())

        return ()