# Slicing in array

import numpy as np
# Slicing => [start:end:steps] not including end

a=np.array(["A","B","C","D","E","F"])
print(a.ndim) # 1
print(a[1]) # B
print(a[:]) # ['A' 'B' 'C' 'D' 'E' 'F']
print(a[0:4]) # ['A' 'B' 'C' 'D']
print(a[:4]) # ['A' 'B' 'C' 'D']
print(a[2:]) # ['C' 'D' 'E' 'F']
print(a[1:4:2]) # ['B' 'D']

b=np.array([["A","B","C"],["D","E","F"],["L","M","N"]])
print(b.ndim) # 2

print(b[:]) # [['A' 'B' 'C']['D' 'E' 'F']['L' 'M' 'N']]
print(b[:2]) # [['A' 'B' 'C']['D' 'E' 'F']]
print(b[1:]) # [['D' 'E' 'F']['L' 'M' 'N']]
print(b[:3 , 0:2]) # [['A' 'B']['D' 'E']['L' 'M']]
print(b[2: , 0]) # ['L']

