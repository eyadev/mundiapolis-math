# alexa@ubuntu-xenial:0x00-linear_algebra$ cat 100-main.py
#!/usr/bin/env python3

import numpy as np
# np_slice = __import__('100-slice_like_a_ninja').np_slice
def np_slice(matrix, axes={}):
    sliced = []
    max_key = max(axes)
    for i in range(max_key + 1):
        if i in axes.keys():
            sliced.append(slice(*axes.get(i)))
        else:
            sliced.append(slice(None, None, None))
    return matrix[tuple(sliced)]
    
mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np_slice(mat1, axes={1: (1, 3)}))
print(mat1)
mat2 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
                 [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])
print(np_slice(mat2, axes={0: (2,), 2: (None, None, -2)}))
print(mat2)
# alexa@ubuntu-xenial:0x00-linear_algebra$ ./100-main.py
# [[2 3]
#  [7 8]]
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
# [[[ 5  3  1]
#   [10  8  6]]

#  [[15 13 11]
#   [20 18 16]]]
# [[[ 1  2  3  4  5]
#   [ 6  7  8  9 10]]

#  [[11 12 13 14 15]
#   [16 17 18 19 20]]

#  [[21 22 23 24 25]
#   [26 27 28 29 30]]]
# alexa@ubuntu-xenial:0x00-linear_algebra$