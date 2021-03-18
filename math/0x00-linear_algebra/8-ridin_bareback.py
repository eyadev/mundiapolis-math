#!/usr/bin/env python3
"""
function that multiply 2 matrices
"""

def mat_mul(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        new_mat = []
        for x in range(len(mat1)):
            res = []
            for y in range(len(mat2[0])):
                number = 0
                for z in range(len(mat1[0])):
                    number += (mat1[x][z] * mat2[z][y])
                res.append(number)
            new_mat.append(res)
        return new_mat
    else:
        return None