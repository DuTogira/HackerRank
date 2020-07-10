# problem: https://www.hackerrank.com/challenges/apple-and-orange/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #s thru t are the location of the house.
    #a is loc of apple tree.
    #b is loc of orange tree.
    results = [0] * 2
    for apple in apples:
        if ((a + apple) >= s) and ((a + apple) <= t):
            results[0] += 1
    for orange in oranges:
        if ((b + orange) >= s) and ((b + orange) <= t):
            results[1] += 1
    print(results[0])
    print(results[1])


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
