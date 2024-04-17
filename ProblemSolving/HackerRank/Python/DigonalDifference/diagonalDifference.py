#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    x=y=0
    for i in range(len(arr)):       
        for j in range(len(arr)):
            if j==i:
                x+=arr[i][j]
            if j+i==len(arr)-1:
                y+=arr[i][j]
    return(abs(y-x))

def DiagonalDifference(arr):
    a,b = 0,0
    for ia in range(len(arr)):
        a += arr[ia][ia]
        b += arr[ia][-ia-1]
    return abs(a-b)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
