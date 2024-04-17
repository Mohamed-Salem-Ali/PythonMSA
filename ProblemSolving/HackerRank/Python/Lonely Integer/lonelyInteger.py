#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    arr = Counter(a)
    for k, v in arr.items():
        if v == 1:return k

#My mathematical approach: 
#If u take every unique number in the array and sum it 
#then double the sum u will have also doubled the lonely number. 
#So when you then subtract the sum of the array from it you will be left with the only number that has not been twice in the array. python:

def lonelyintegerMath(a):
   sum_of_set = sum(set(a))
   sum_of_list = sum(a)
   return sum_of_set*2-sum_of_list

def lonelyintegerShort(a): for x in a: if a.count(x) == 1 : return x
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
