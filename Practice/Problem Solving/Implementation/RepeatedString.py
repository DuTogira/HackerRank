# problem: https://www.hackerrank.com/challenges/repeated-string/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    size = len(s)
    a_s = s.count('a')
    a_s *= n//size
    for i in range(n % size):
        if s[i] == 'a':
            a_s += 1
    return a_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
