# problem: https://www.hackerrank.com/challenges/cut-the-sticks/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr = sorted(arr)
    result = []
    while True:
        result.append(len(arr))
        smallest = arr[0]
        arr = list(filter((smallest).__ne__, arr))
        if len(arr) == 0:
            break
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
