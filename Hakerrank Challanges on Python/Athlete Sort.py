#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=lambda x: x[k])

    # Print the sorted array
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
