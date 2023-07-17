mport math
import os
import random
import re
import sys
from datetime import datetime 
# Complete the time_delta function below.
def time_delta(t1_str, t2_str):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1_str, fmt)
    t2 = datetime.strptime(t2_str, fmt)
    diff = abs(t1 - t2)
    return str(int(diff.total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
