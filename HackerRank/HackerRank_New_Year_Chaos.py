#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count=0 #initiate count variable
    for i in range(n):
        if(q[i]-(i+1) >= 3): # check if the q[i] > it's index+3
            print("Too chaotic")
            return
        for j in range(max(0,q[i]-2),i): #max is needed because it could go to negative number.
                                         #q[i]-2 means we don't have to look up more than 2 ahead of q[i]'s original position
            if q[j]> q[i]:
                count += 1
    print(count)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
