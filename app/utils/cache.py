import json
from app.utils.redis_client import r

def get_cache(key):
    value = r.get(key)
    if value:
        return json.loads(value)
    return None

def set_cache(key, value, ttl=60):
    r.set(key, json.dumps(value), ex=ttl)