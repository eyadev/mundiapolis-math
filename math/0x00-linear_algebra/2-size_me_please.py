alexa@ubuntu-xenial:0x00-linear_algebra$ cat 2-main.py 
#!/usr/bin/env python3

matrix_shape = __import__('2-size_me_please').matrix_shape
import numpy as np 
def matrix_shape(matrix):
        return list (np.shape(matrix))

mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))
mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print(matrix_shape(mat2))
alexa@ubuntu-xenial:0x00-linear_algebra$ ./2-main.py 
[2, 2]
[2, 3, 5]
alexa@ubuntu-xenial:0x00-linear_algebra$ 