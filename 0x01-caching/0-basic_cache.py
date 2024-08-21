#!/usr/bin/env python3
"""Basic caching systrm that inherits from BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """stores an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets an item by key from cache.
        """
        return self.cache_data.get(key, None)
