# problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


# !/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    small = scores[0]
    big = scores[0]
    output = [0, 0]
    for score in scores:
        if score < small:
            output[1] += 1
            small = score
        if score > big:
            output[0] += 1
            big = score
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
