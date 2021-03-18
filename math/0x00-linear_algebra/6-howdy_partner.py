#!/usr/bin/env python3
"""
function that concatenate 2 arrays
"""

def cat_arrays(arr1, arr2):
    conc = arr1.copy()
    for i in arr2:
        conc.append(i)
    return conc