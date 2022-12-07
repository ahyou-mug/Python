#!/usr/bin/env python

"""
Function to recursively map dictionary keys in Python.
Maps all keys for each level, then returns number of
items in lowest level.
Designed with web scraping and other tasks in mind
where dictionaries may have large numbers of pairs
and need cleaning. End goal is to use it to present the
user with a menu to navigate the dictionary for cleaning
"""

def map_keys(obj):
    keys = {}
    if isinstance(obj,dict):
        for key in obj.keys():
            if all(type(value)==str for value in obj.values()):
                return (len(obj))
            elif any(type(value)==dict for value in obj.values()):
                keys[key] = map_keys(obj[key])
    #return keys
    return keys
