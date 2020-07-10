# problem: https://www.hackerrank.com/challenges/circular-array-rotation/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    n = len(a)
    a1 = []
    for i in range(0, n):
        a1.append(a[(i+n-(k%n))%n])
    result = []
    for query in queries:
        result.append(a1[query])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
