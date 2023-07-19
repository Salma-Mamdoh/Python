# ---------------------------------------------
# -- Numpy => Arithmetic & Useful Operations --
# ---------------------------------------------
# - Addition
# - Subtraction
# - Multiplication
# - Dividation
# ----------------
# - min
# - max
# - sum
# - ravel => Returns Flattened Array 1 Dimension With Same Type
# ----------------------------------------------
import numpy as np

arr1=np.array([10,20,30])
arr2=np.array([5,2,4])

print(arr1+arr2) # [15 22 34]

print(arr1-arr2) # [ 5 18 26]

print(arr1*arr2) # [ 50  40 120]

print(arr1/arr2) # [ 2.  10.   7.5]
# 2 arrays must be in same size
arr3=np.array([[1,4],[5,9]])
arr4=np.array([[2,7],[10,5]])

print(arr3+arr4) # [[ 3 11] [15 14]]

print(arr3-arr4) # [[-1 -3] [-5  4]]

print(arr3*arr4) # [[ 2 28] [50 45]]

print(arr3/arr4) # [[0.5        0.57142857] [0.5        1.8       ]]


arr5=np.array([20,30,-2,0,12,16])
print(arr5.min()) # -2
print(arr5.max()) # 30
print(arr5.sum()) # 76

arr6=np.array([[2,7],[10,5]])

print(arr6.min()) # 2
print(arr6.max()) # 10
print(arr6.sum()) # 24

# Raval convert n -dimensional array to one dimensional array

print(arr6) # [[ 2  7] [10  5]]
print(arr6.ndim) # 2
arr6=arr6.ravel()
print(arr6) # [ 2  7 10  5]
print(arr6.ndim) # 1
