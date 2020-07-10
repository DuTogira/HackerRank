# problem: https://www.hackerrank.com/challenges/find-digits/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the findDigits function below.
def findDigits(n):
    divisors = 0
    for digit in [int(d) for d in str(n)]:
        divisors += 1 if digit != 0 and n % digit == 0 else 0
    return divisors


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
