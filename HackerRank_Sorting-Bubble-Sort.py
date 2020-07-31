#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    exchangeN = 0
    for i in range(n):
        for j in range(n-1):
            if(a[j]> a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                exchangeN += 1
    print("Array is sorted in "+str(exchangeN)+" swaps.\n"+\
    "First Element: "+str(a[0])+\
    "\nLast Element: "+str(a[-1]))
    
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
