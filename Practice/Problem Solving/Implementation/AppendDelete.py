# problem: https://www.hackerrank.com/challenges/append-and-delete/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    substring = s[0]
    i = 1
    while i < len(s) and substring + s[i] == t[:i + 1]:
        substring += s[i]
        i += 1
    if k < (len(s) + len(t)) - (2 * len(substring)):
        return 'No'
    elif k % 2 == ((len(s) + len(t)) - 2 * len(substring)) % 2:
        return 'Yes'
    elif 0 > len(s) + len(t) - k:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
