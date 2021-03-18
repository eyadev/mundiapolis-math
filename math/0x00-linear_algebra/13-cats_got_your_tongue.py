#!/usr/bin/env python3
'''
concatenate 2 matrices with numpy
'''
def np_cat(mat1, mat2, axis=0):
    return np.concatenate((mat1,mat2),axis=axis)
