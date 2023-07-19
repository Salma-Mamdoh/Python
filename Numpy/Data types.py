# -------------------------------------------
# -- Numpy => Data Types And Control Array --
# -------------------------------------------
# '?' boolean
# 'b' (signed) byte
# 'B' unsigned byte
# 'i' (signed) integer
# 'u' unsigned integer
# 'f' floating-point
# 'c' complex-floating point
# 'm' timedelta
# 'M' datetime
# 'O' (Python) objects
# 'S', 'a' zero-terminated bytes (not recommended)
# 'U' Unicode string
# 'V' raw data (void)
# ------------------------------------------------
import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([1.5,2.5,12.5])
arr3=np.array(["Sal","ma","Khokha"])

print(arr1.dtype) # int32
print(arr2.dtype) # float64
print(arr3.dtype) # <U6 6 num of chars in longest string in arr

arr4=np.array([1,2,3] , dtype="int") # int or i
arr5=np.array([1.5,2.5,12.5],dtype="float") # float or f
arr6=np.array(["Sal","ma","Khokha"],dtype="str")

print(arr4.dtype) # int32
print(arr5.dtype) # float64
print(arr6.dtype) # <U6

# change data type of existing array
arr7=np.array([1,2,3,5,6,0] )
print(arr7.dtype) # int32

arr7=arr7.astype(float)
print(arr7.dtype) # float64
print(arr7) # 1. 2. 3. 5. 6.]

arr7=arr7.astype(bool)
print(arr7.dtype) # bool
print(arr7) # [ True  True  True  True  True False]

my_arr=np.array([100,200,300],dtype='f')
print(my_arr.dtype) # float32
print(my_arr[0].itemsize) # 4 byte

my_arr=my_arr.astype(float)
print(my_arr.dtype) # float64
print(my_arr[0].itemsize)  # 8 byte 
