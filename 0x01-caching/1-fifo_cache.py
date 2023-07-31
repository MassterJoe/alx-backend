#!/usr/bin/python3
"""
Create a class FIFOCache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ It inherits from the parent class BaseCaching  """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ it puts values into the dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            key, value = self.cache_data.popitem()
            print("DISCARD: {}".format(key))

    def get(self, key):
        """ gets the value of the dict key"""
        if key is not None:
            value = self.cache_data.get(key)
            return value
