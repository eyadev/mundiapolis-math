#!/usr/bin/env python3

import numpy as np
def np_cat(mat1, mat2, axis=0):
    if (len(mat1[0]) == len(mat2[0])) and axis == 0:
        return np.concatenate((mat1,mat2),axis=0)
    elif (len(mat1) == len(mat2)) and axis == 1:
        return np.concatenate((mat1,mat2),axis=1)
    else:
        return None

