# Notes from Kaggle Numpy Tutorial For Beginners [ Data Science]
# zeros and ones Generate arrays of zeros or ones
import numpy as np
import random
arr1=np.zeros(3)
print(arr1) # [0. 0. 0.]

print(np.zeros((2,3))) # [[0. 0. 0.] [0. 0. 0.]]

print(np.ones(5)) # [1. 1. 1. 1. 1.]

print(np.ones((2,3))) # [[1. 1. 1.] [1. 1. 1.]]

# linspace Return evenly spaced numbers over a specified interval.
# linespace (startof interval, endof interval , # numbers should return )
print(np.linspace(0,10,3)) # [ 0.  5. 10.]
print(np.linspace(0,10,5)) # [ 0.   2.5  5.   7.5 10. ]
print(np.linspace(0,10,20)) # [ 0.          0.52631579  1.05263158  1.57894737  2.10526316  2.631578953.15789474  3.68421053  4.21052632  4.73684211  5.26315789  5.789473686.31578947  6.84210526  7.36842105  7.89473684  8.42105263  8.94736842 9.47368421 10.        ]


# eye Creates an identity matrix
print(np.eye(4))
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

print(np.eye(10))
# [[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]]

# Random
# Numpy also has lots of ways to create random number arrays
# rand Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1]

print(np.random.rand(2)) # [0.58694264 0.73733327]
print(np.random.rand(7)) # [0.10565398 0.93681359 0.66698678 0.75221535 0.7739529  0.440737880.23677379]

# randn Return a sample (or samples) from the "standard normal" distribution. Unlike rand which is uniform
print(np.random.randn(5)) # [ 0.04486326 -0.08420179 -0.99265227  0.47453869  1.17303173]

print(np.random.randn(5,5))
# [[ 2.33391508  1.75233911  2.00747029  1.58537575 -0.98300216]
#  [ 0.29757727 -0.15199059 -0.2373573   0.89817105 -0.58129517]
#  [ 0.69098584 -0.65052768 -1.65858446 -0.5010776  -1.43200763]
#  [-0.98244181 -0.23643808  0.03352574 -0.30563513  1.7427127 ]
#  [ 0.24709609 -0.70657563 -1.64213792 -0.24631005  0.70883798]]

# randint Return random integers from low (inclusive) to high (exclusive).

print(np.random.randint(1,1000)) # 213

print(np.random.randint(1,1000,10)) # [628 599 559 958 102 208  62 456 724  63]

arr2=np.array([ 1,  9, 12, 33, 10, 13, 24, 10, 36, 33])
print(arr2.max()) # 36
print(arr2.argmax()) # 8 index of 36
print(arr2.min()) # 1
print(arr2.argmin()) # 0 index of 1

# Broadcasting Numpy arrays differ from a normal Python list because of their ability to broadcas
arr2[0:4]=700
print(arr2) # [700 700 700 700  10  13  24  10  36  33]


# Fancy Indexing Fancy indexing allows you to select entire rows or columns out of order,to show this,
arr2d = np.zeros((10, 10))
# Length of array
arr_length = arr2d.shape[1]

for i in range(arr_length):
    arr2d[i] = i

print(arr2d)
#[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
# [2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]
# [3. 3. 3. 3. 3. 3. 3. 3. 3. 3.]
# [4. 4. 4. 4. 4. 4. 4. 4. 4. 4.]
# [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
# [6. 6. 6. 6. 6. 6. 6. 6. 6. 6.]
# [7. 7. 7. 7. 7. 7. 7. 7. 7. 7.]
# [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
# [9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]]

print(arr2d[[2,4,3,5,6]])
#[[2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]
# [4. 4. 4. 4. 4. 4. 4. 4. 4. 4.]
# [3. 3. 3. 3. 3. 3. 3. 3. 3. 3.]
# [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
# [6. 6. 6. 6. 6. 6. 6. 6. 6. 6.]]

print(arr2d[[4,5,2,1]])
#[[4. 4. 4. 4. 4. 4. 4. 4. 4. 4.]
# [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
# [2. 2. 2. 2. 2. 2. 2. 2. 2. 2.]
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]

#Selection how to use brackets for selection based off of comparison operators
arr5=np.arange(1,11)
arr6=arr5>4
print(arr6) # [False False False False  True  True  True  True  True  True]
print(arr5[arr6]) # [ 5  6  7  8  9 10]
print(arr5[arr5<=6]) # [1 2 3 4 5 6]

print(np.sqrt(arr5))
# [1.         1.41421356 1.73205081 2.         2.23606798 2.44948974
#  2.64575131 2.82842712 3.         3.16227766]
print(np.exp(arr5))  #Calcualting exponential (e^)
# [1.         1.41421356 1.73205081 2.         2.23606798 2.44948974
#  2.64575131 2.82842712 3.         3.16227766]

print(np.sin(arr5))
# [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427 -0.2794155
#   0.6569866   0.98935825  0.41211849 -0.54402111]
print(np.log2(arr5))
# [0.         1.         1.5849625  2.         2.32192809 2.5849625
#  2.80735492 3.         3.169925   3.32192809]

