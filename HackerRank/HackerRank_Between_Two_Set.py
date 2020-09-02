#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    smallN = a[-1]
    bigN = b[0]
    checker = True
    result = 0
    for i in range(bigN,smallN-1,-1):
        for j in a:
            if checker == True:
                if i%j == 0:
                    checker = True
                else:
                    checker = False
        if checker == True:
            for k in b:
                if checker == True:
                    if k%i == 0:
                        checker = True
                    else:
                        checker = False
        if checker == True:
            result += 1
        else:
            checker = True
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
