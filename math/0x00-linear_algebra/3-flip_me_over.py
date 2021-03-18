#!/usr/bin/env python3
'''
Function that takes a matrix and return its transpose
'''
def matrix_transpose(matrix):
    trans = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 
    return trans
