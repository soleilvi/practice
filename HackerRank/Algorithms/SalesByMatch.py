'''
https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/problem?h_r=internal-search

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
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    count = 0
    n = 0
    assessed_nums = []
    times_repeated = []
    
    for i in ar:
        if i not in assessed_nums:
            for j in ar:
                if j / i == 1:
                    count += 1
            assessed_nums.append(i)
            times_repeated.append(count)
            count = 0
            
            
    for i in times_repeated:
        pee = math.floor((i / 2))
        times_repeated[n] = pee
        n += 1
    
    return sum(times_repeated)

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
