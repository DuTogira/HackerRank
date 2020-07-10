# problem: https://www.hackerrank.com/challenges/sock-merchant/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = set()
    i = 0
    pairs = 0
    while i < n:
        if ar[i] not in colors:
            colors.add(ar[i])
        else:
            colors.remove(ar[i])
            pairs += 1
        i += 1
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
