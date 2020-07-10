# problem: https://www.hackerrank.com/challenges/equality-in-a-array/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the equalizeArray function below.
def equalizeArray(arr):
    count_nums = dict()
    for i in range(0, len(arr)):
        if arr[i] in count_nums:
            count_nums[arr[i]] += 1
        else:
            count_nums[arr[i]] = 1
    return len(arr) - max(count_nums.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
