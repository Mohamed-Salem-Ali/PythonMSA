#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    x=n
    for i in range(1,n+1):
        if i==n:
            print('#'*i)
        else:
            print(' '*(x-i-1),'#'*(i))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
