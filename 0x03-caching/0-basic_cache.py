#!/usr/bin/env python3
""" 0-basic_cache.py
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache System  that have no limit
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        set item to cache
        """
        if key or item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """
        get item from cache if it exists other none
        """
        if key:
            try:
                return self.cache_data[key]
            except Exception as e:
                return None
