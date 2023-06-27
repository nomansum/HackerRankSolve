#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    negative = 0
    positive = 0
    zero     = 0 
    
    for i in arr:
        if i<0:
            negative += 1
            
        elif i>0:
            positive +=1
            
        else:
            zero +=1
            
    length = len(arr)
    
    length *= 1.00
    
    print("{0:.6f}".format(positive/length))
    print("{0:.6f}".format(negative/length))
    print("{0:.6f}".format(zero/length))
    
    
    
    

     
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
