# problem: https://www.hackerrank.com/challenges/non-divisible-subset/problem


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
def nonDivisibleSubset(k, s):
    # Write your code here
    r_dict = dict()
    subset = []
    for elem in s:
        if elem % k not in r_dict.keys():
            r_dict[elem % k] = [elem]
        else:
            r_dict[elem % k].append(elem)
    if 0 in r_dict.keys():
        subset.append(r_dict.pop(0)[0])
    for i in sorted(r_dict.keys()):
        j = k - i
        if i in r_dict:
            if i == j:
                subset.append(r_dict.pop(i)[0])
            elif j not in r_dict or len(r_dict[i]) >= len(r_dict[j]):
                subset += r_dict.pop(i)
                if j in r_dict:
                    r_dict.pop(j)
            else:
                subset += r_dict.pop(j)
                r_dict.pop(i)
    return len(subset)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
