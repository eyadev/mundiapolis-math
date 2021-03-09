alexa@ubuntu-xenial:0x00-linear_algebra$ cat 8-main.py
#!/usr/bin/env python3

mat_mul = __import__('8-ridin_bareback').mat_mul
import numpy as np

def mat_mul(mat1, mat2):
        array = np.matmul(mat1, mat2)
        return  array.tolist()
    

mat1 = [[1, 2],
        [3, 4],
        [5, 6]]
mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8]]
print(mat_mul(mat1, mat2))
alexa@ubuntu-xenial:0x00-linear_algebra$ ./8-main.py
[[11, 14, 17, 20], [23, 30, 37, 44], [35, 46, 57, 68]]
alexa@ubuntu-xenial:0x00-linear_algebra$ 