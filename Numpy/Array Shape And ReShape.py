# ------------------------------------
# -- Numpy => Array Shape & ReShape --
# ------------------------------------
# Shape Returns A Tuple Contains The Number Of Elements in Each Dimension
# ----------------------------------------------

import numpy as np

arr1=np.array([1,2,3,4])

print(arr1.ndim) # 1
print(arr1.shape) # (4,)


arr2=np.array([[1,2],[2,5],[7,8]])
print(arr2.ndim) # 2
print(arr2.shape) # (3, 2)

arr3=np.array([[[1,2],[2,5]],[[7,8],[10,11]]])
print(arr3.ndim) # 3
print(arr3.shape) # (2, 2, 2)


# Reshape

arr4=np.array([1,2,3,4,5,6,7,8])

print(arr4.ndim) # 1
print(arr4.shape) # (9,)

reshape_arr4=arr4.reshape(2,4)
print(reshape_arr4) # [[1 2 3 4] [5 6 7 8]]
print(reshape_arr4.ndim) # 2
print(reshape_arr4.shape)  # (2, 4)

reshape_arr5=arr4.reshape(4,2)
print(reshape_arr5) # [[1 2] [3 4] [5 6] [7 8]]
print(reshape_arr5.ndim) # 2
print(reshape_arr5.shape)  # (4, 2)
# flaten
reshape_arr6=arr4.reshape(-1)
print(reshape_arr6) # [1 2 3 4 5 6 7 8]
print(reshape_arr6.ndim) # 1
print(reshape_arr6.shape)  # (8,)

arr7=np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
reshape_arr7=arr7.reshape(2,5,2) 
print(reshape_arr7) # [[[ 1  2] [ 3  4] [ 5  6] [ 7  8] [ 9 10]] [[ 1  2] [ 3  4] [ 5  6] [ 7  8] [ 9 10]]]
print(reshape_arr7.ndim) #3 
print(reshape_arr7.shape) # (2, 5, 2)
