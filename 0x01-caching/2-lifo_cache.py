#!/usr/bin/python3
"""
Create a class LIFOCache
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ It inherits from the parent class BaseCaching  """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ it puts values into the dictionary
        and evicts items based on the LIFO algorithm"""
        if key is None or item is None:
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            last_item = self.cache_data.popitem()[0]
            print("DISCARD: {}".format(last_item))
        self.cache_data[key] = item

    def get(self, key):
        """ gets the value of the dict key"""
        if key is not None:
            value = self.cache_data.get(key)
            return value
