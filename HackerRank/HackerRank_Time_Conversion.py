#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if "AM" in s:
        if "12" == s[:2]:
            hour = "00"
        else:
            hour = s[:2]
    if "PM" in s:
        if s[:2] != "12":
            hour = str(int(s[:2])+12)
        else:
            hour = s[:2]
    withoutAMPM = hour+s[2:8]
    return withoutAMPM

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
