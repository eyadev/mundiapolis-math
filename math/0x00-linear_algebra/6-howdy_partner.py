#!/usr/bin/env python3

import numpy as np
def cat_arrays(arr1, arr2):
    arr = np.concatenate((arr1, arr2))
    return arr.tolist()
