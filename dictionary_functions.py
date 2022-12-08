#!/usr/bin/env python

# Recursively maps keys of nested
# dictionaries. Upon reaching bottom
# layer, returns number of values
# in that layer.         
def map_keys(obj):
    keys = {}
    if isinstance(obj,dict):
        for key in obj.keys():
            if all(type(value)==str for value in obj.values()):
                return (str(len(obj))+" string values in dictionary")
            elif any(type(value)==dict for value in obj.values()):
                keys[key] = map_keys(obj[key])
    #return keys
    return keys

# Returns the recursive depth
# of the specified dictionary.
# Tthe number of levels that
# the dictionary is nested to
def depth(d):
     if isinstance(d, dict):
         return 1 + (max(map(depth, d.values())) if d else 0)
     return 0
