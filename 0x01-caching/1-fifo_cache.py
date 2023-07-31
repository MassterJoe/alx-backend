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
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            first_item = next(iter(self.cache_data))
            self.cache_data.pop(first_item)
            print("DISCARD: {}".format(first_item))
        self.cache_data[key] = item

    def get(self, key):
        """ gets the value of the dict key"""
        if key is not None:
            value = self.cache_data.get(key)
            return value
