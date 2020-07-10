# problem: https://www.hackerrank.com/challenges/bon-appetit/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = 0
    for i, item in enumerate(bill):
        if i != k:
            total += item
    total = total/2
    diff = abs(b - total)
    if diff == 0:
        print('Bon Appetit')
    else:
        print(int(diff))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
