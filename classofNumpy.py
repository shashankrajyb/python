"""
#Array operations Using Numpy
import numpy as np
from numpy.ma.core import reshape

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[1,2],[3,4],[5,6]])
res1 = np.matmul(arr1,arr2)
print(res1)

#invert Matrix
import numpy as np
arr3 = np.array([[2,1,3],[4,5,6],[7,8,9]])
res2 = np.invert(arr3)
print(res2)

#creating an array with value from 0 t0 9
import numpy as np
arr4 =np.arange(10)
print(arr4)

#Array Manipulation
import numpy as np
arra = np.arange(12)
reshaped_arra = np.reshape(arra,(3,4))
print(reshaped_arra)

#Mean of array
import numpy as np
arr5 = np.array([[1,2,3],
                 [4,5,6]])
row_mean = np.mean(arr5, axis=0) #by adding row values 1+2/2 = 2.5

col_mean = np.mean(arr5, axis=1)
print(row_mean)
print(col_mean)

#Addition of coloumns
import numpy as np
arr5 = np.array([[1,2,3],
                 [4,5,6]])
col_sum = np.sum(arr5,axis=1)
print(col_sum)
"""
#Random number Generation of Uniform distribution B/W (0,1) interval in float value
import numpy as np
rand_arr = np.random.rand(3)
print(rand_arr)