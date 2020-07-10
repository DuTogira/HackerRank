# problem: https://www.hackerrank.com/challenges/permutation-equation/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the permutationEquation function below.
def permutationEquation(p):
    dic = dict()
    for i, num in enumerate(p):
        print(num)
        dic[num] = i + 1
    result = []
    for i in sorted(dic.keys()):
        result.append(dic[dic[i]])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
