#!/usr/bin/env python3

import numpy as np 

def cat_matrices2D(mat1, mat2, axis=0):
    if (len(mat1[0]) == len(mat2[0])) and axis == 0:
        new_mat=np.concatenate((mat1,mat2),axis=0)
        return new_mat.tolist()
    elif (len(mat1) == len(mat2)) and axis == 1:
        new_mat=np.concatenate((mat1,mat2),axis=1)
        return new_mat.tolist()
    else:
        return None

