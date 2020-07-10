# problem: https://www.hackerrank.com/challenges/a-very-big-sum/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    result = 0
    for num in ar:
        result += num
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
