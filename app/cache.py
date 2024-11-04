# cache.py
import redis

# Initialize Redis client
redis_client = redis.StrictRedis(host="your_redis_host", port=your_redis_port, password="your_redis_password")

def get_cached_data(key):
    return redis_client.get(key)

def set_cached_data(key, value, expiration=60):
    redis_client.setex(key, expiration, value)
