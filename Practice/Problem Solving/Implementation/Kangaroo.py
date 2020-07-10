# problem: https://www.hackerrank.com/challenges/kangaroo/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    leastS = x1
    leastJ = v1
    mostS = x2
    mostJ = v2
    if x2 < x1:
        leastS = x2
        leastJ = v2
        mostS = x1
        mostJ = v1
    if leastJ <= mostJ and leastS != mostS:
        return "NO"
    while(leastS <= mostS):
        if(leastS == mostS):
            return "YES"
        leastS += leastJ
        mostS += mostJ
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
