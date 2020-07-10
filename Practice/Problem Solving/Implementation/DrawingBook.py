# problem: https://www.hackerrank.com/challenges/drawing-book/problem


# !/bin/python3

import os
import sys
import math


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    forwards = math.floor(p/2)
    backwards = 0
    if n % 2 == 0:
        backwards = math.ceil((n-p)/2)
    else:
        backwards = math.floor((n-p)/2)
    return min(forwards, backwards)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
