#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    count = 0
    oddN = 0
    for i in B:
        if(i%2==1):
            oddN +=1
    if len(B)==2 and sum(B)%2 ==1:
        return "NO"
    elif oddN%2 ==1:
        return "NO"
    else:
        for i in range(1,len(B)-1):
            a,b,c = B[i-1],B[i], B[i+1]
            if a%2==1:
                B[i-1]+=1
                B[i]+=1
                count+=2
            elif b%2==1:
                count+=2
                B[i]+=1
                B[i+1]+=1
    if count==0:
        return 0
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
