#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 


if __name__ == '__main__':
    s = input()
    cnt=dict(Counter(s))
    final= dict(sorted(cnt.items(), key=lambda x: (-x[1], x[0])))
    for i, (key, value) in enumerate(final.items()):
        print(key, value)
        if i == 2:
            break
