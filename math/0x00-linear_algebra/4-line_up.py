#!/usr/bin/env python3
'''
function that calculate the sum of 2 arrays
'''
def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return "None"
    else:  
        return [(arr1[i] + arr2[i]) for i in range(len(arr1))]
