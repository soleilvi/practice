'''
https://www.hackerrank.com/challenges/2d-array/problem

By Soleil Vivero
2021
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    d_sum = 0
    l = []
    
    for c in range(0, 4):
        for r in range(0, 4):
            d_sum = sum([arr[c][r], arr[c][r + 1], arr[c][r + 2],
                    arr[c + 1][r + 1],
                    arr[c + 2][r], arr[c + 2][r + 1], arr[c + 2][r + 2]])
            l.append(d_sum)
    return max(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()