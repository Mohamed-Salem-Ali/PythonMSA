#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    x=s.split(":")
    y= x[-1][2:].lower()
    if y =="pm":
        if(x[0]!="12"):
            x[0]=str(int(x[0])+12)
    elif y=="am":
        if(x[0]=="12"):
            x[0]="00"
    z=x[0]+":"+x[1]+":"+x[2][:2]
    print(z)
if __name__ == '__main__':

    s = input("enter time: ")

    result = timeConversion(s)

