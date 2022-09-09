from django.conf import settings

redis = settings.REDIS_CONNECTION


def set_cache(key, value):
    redis.set(key, value)


def hmset_cache(key, value):
    redis.hmset(key, value)


def hmget_cache(name, keys):
    return redis.hmget(name, keys)


def hash_increase_field(key, field, n):
    redis.hincrby(key, field, n)


def get_cache(key):
    value = redis.get(key)
    return value if value else None


def get_dict_cache(key):
    value = redis.hgetall(key)
    return value if value else None


def incr_counter(key):
    new_value = redis.incr(key)
    return new_value


def delete_cache(key):
    redis.delete(key)


def last_from_list(key):
    return redis.rpop(key)


def add_in_set(key, value):
    return redis.sadd(key, value)


def fetch_members_in_set(key):
    return redis.smembers(key)


def check_key_cache(key):
    return redis.exists(key)


def set_cache_expiration(key, timeout):
    return redis.expire(key, timeout)


def cache_setnx(key, value):
    return redis.setnx(key, value)


def set_cache_ttl(key, value, ttl=600):
    redis.set(key, value, ttl)


def setnx_cache_ttl(key, value, ex=200, nx=False):
    return redis.set(key, value, ex=ex, nx=nx)
