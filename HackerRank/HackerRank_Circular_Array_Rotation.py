#!/bin/python3

import math
import os
import random
import re
import sys

def exc(aList):
    p = aList.pop()
    aList.insert(0,p)
    return aList

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    answer = []
    newA = a
    for _ in range(k):
        newA= exc(newA)
    for i in queries:
        answer.append(newA[i])
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
