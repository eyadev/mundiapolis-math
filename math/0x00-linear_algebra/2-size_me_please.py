#!/usr/bin/env python3
'''
function that takes a matrix and return its shape
'''
def matrix_shape(matrix):
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])
