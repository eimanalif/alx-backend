#!/usr/bin/env python3
'''task 0 '''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''inherts from Base_Caching'''
    
    def put(self, key, item):
        '''assign value'''
        if key is None and item is None:
            return
        self.cache_data[key] = item

    def get(self,key):
        '''return value'''
        return self.cache_data.get(key, None)
