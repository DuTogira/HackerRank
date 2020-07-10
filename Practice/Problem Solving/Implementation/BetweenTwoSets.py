# problem: https://www.hackerrank.com/challenges/between-two-sets/problem


#!/bin/python3

import math
import os
import random
import re
import sys


def getTotalX(a, b):
    largest = b[0]
    smallest = a[0]
    total = 0
    for num in a:
        if num > smallest:
            smallest = num
    for num in b:
        if num < largest:
            largest = num
    i = smallest
    while i <= largest:
        print(i)
        inc = True
        for num in a:
            if i % num != 0:
                inc = False
                break
        for num in b:
            if num % i != 0:
                inc = False
                break
        if inc:
            total += 1
        i += smallest
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
