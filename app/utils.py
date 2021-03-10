import uuid

from .extensions import cache


def gen_id():
    return int(str(uuid.uuid4().int)[:8])


def clear_cache(key_prefix):
    keys = [key for key in cache.cache._cache.keys() if key.startswith(key_prefix)]
    cache.delete_many(*keys)
