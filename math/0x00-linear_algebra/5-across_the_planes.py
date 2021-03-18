#!/usr/bin/env python3
'''
function that calculates the sum of 2 matrices
'''
def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2) and len(mat1[0]) != len(mat2[0]):
        return None
    else:
        return [[mat1[j][i]+mat2[j][i] for i in range(len(mat1[0]))] 
                for j in range(len(mat1))]
