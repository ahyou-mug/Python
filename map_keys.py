#!/usr/bin/env python

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
