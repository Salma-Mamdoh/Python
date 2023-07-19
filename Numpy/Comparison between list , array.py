# --------------------
# -- Numpy => Intro --
# --------------------
# - NumPy Is A Python Third-Party Module To Deal With Arrays & Matrices
# - NumPy Stand For Numerical Python
# - NumPy Is Open Source
# - NumPy Support Dealing With Large Multidimensional Arrays & Matrices
# - NumPy Has Many Mathematical Functions To Deal With This Elements
# ------------------------------------------------------------
# * Why We Use NumPy Array
# - Consume Less Memory
# - Very Fast Compared To Python List
# - Easy To Use
# - Support Element Wise Operation
# - Elements Are Stored Contiguous
# -------------------------------------------
# * Python Lists
# ---- Homogeneous => Can Contains The Same Type of Objects
# ---- Heterogeneous => Can Contains Different Types of Objects.
# --------------------------------------------------------------
# - The Items in The Array Have to Be Of The Same Type
# - You Can Be Sure Whats The Storage Size Needed for The Array
# - NumPy Arrays Are Indexed From 0
# --------------------------------------------------------------
# - NumPy On Github => https://github.com/numpy/numpy
# ---------------------------------------------------

import numpy as np
my_list=[1,2,3,4,5]
my_array=np.array(my_list)
print(my_list) # [1, 2, 3, 4, 5]
print(my_array) # [1 2 3 4 5]

# Accessing elements
print(my_array[0]) # 1
# one dimensional array
a=np.array(10)
b=np.array([10,20])
# two dimensional array
c=np.array([[1,2],[3,4]])
print(c[0]) # [1 2]
# tree dimensional array
d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d[0]) # [[1 2] [3 4]]
print(d[0][1]) # [3 4]
print(d[0][1][0]) # 3
print(d[0,1,0]) # 3

print(d.ndim) # 3

print(c.ndim) # 2

# custom dimensional
my_custom_arr=np.array([1,2,3], ndmin=3)
print(my_custom_arr) # [[[1 2 3]]]
print(my_custom_arr[0,0,1]) # 2
print(my_custom_arr.ndim) # 3


# compare data location and type
# id ---> get memory address
print(id(my_list[0]))
print(id(my_list[1]))

print(id(my_array[0]))
print(id(my_array[1]))

my_li=[1,2,5,True,'SALMA']
my_arr=np.array(my_li)

print(my_li) # [1, 2, 5, True, 'SALMA']
print(my_arr) # ['1' '2' '5' 'True' 'SALMA'] ---> convert all data to strings

print(type(my_li[0])) # <class 'int'>
print(type(my_arr[0])) # <class 'numpy.str_'>

# performance & memory use for numpy

import time
import sys
ele=10000000;
my_lis1=range(ele)
my_lis2=range(ele)

my_ar1=np.arange(ele)
my_ar2=np.arange(ele)

lis_start=time.time()

lis_res=[(n1+n2) for n1,n2 in zip(my_lis1,my_lis2)]
print(f"excecution time for list {time.time()-lis_start}") # excecution time for list  0.8561112880706787
arr_start=time.time()
arr_res=my_ar1+my_ar2
print(f"excecution time for array {time.time()-arr_start}") # excecution time for array 0.015799283981323242



arr=np.arange(100)
print(arr.itemsize) # 4
print(arr.size) # 100
print(f"All Bytes {arr.itemsize*arr.size}") # All Bytes 400

lastlist=range(100)
print(len(lastlist)) # 100
print(sys.getsizeof(1)) # 28
print(f"All Bytes {sys.getsizeof(1)*len(lastlist)}") # All Bytes 2800