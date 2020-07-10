# problem: https://www.hackerrank.com/challenges/extra-long-factorials/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    # The point of this problem is to give people a challenge in memory management in languages which can't handle
    # huge numbers gracefully. Based on the constraints of any product however, developers should be selecting
    # languages which best handle the problem at hand. For massive numbers, Python does that best.
    print(math.factorial(n))


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
