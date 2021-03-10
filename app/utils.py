import uuid

from .extensions import cache


def gen_id():
    return int(str(uuid.uuid4().int)[:8])


def clear_cache(key_prefix):
    keys = [key for key in cache.cache._cache.keys() if key.startswith(key_prefix)]
    cache.delete_many(*keys)


def clear_redis_cache(pattern):
    binary_keys = cache.cache._read_clients.keys(pattern)
    keys = [k.decode("utf-8", errors="ignore") for k in binary_keys if k]
    if keys:
        cache.cache._write_client.delete(*keys)
