# !/usr/bin/env python3

import numpy as np
def add_matrices(mat1, mat2):
    if(np.shape(mat1) == np.shape(mat2)):
        array=np.add(mat1,mat2)
        return array.tolist()
    else:
        return "None"

