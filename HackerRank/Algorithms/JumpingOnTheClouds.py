'''
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

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
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    count = 0
    current = 0

    if len(c) > 2:
        for i in range(len(c) - 2):
            if i == current:
                if c[i + 2] == 0:
                    current += 2
                    if i == len(c) - 4:
                        count += 1
                else:
                    current += 1
                count += 1
    elif len(c) == 2:
        count += 1
        
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
