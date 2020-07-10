# problem: https://www.hackerrank.com/challenges/queens-attack-2/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0
    # We now have a set of tuples representing obstacles for O(1) lookup
    # on whether or not a square contains an obstacle
    obs = set(tuple(ob) for ob in obstacles)
    # Handle moving North
    for i in range(r_q + 1, n + 1):
        if (i, c_q) in obs:
            break
        count += 1
    # Handle moving South
    for i in range(r_q - 1, 0, -1):
        if (i, c_q) in obs:
            break
        count += 1
    # Handle moving East
    for i in range(c_q + 1, n + 1):
        if (r_q, i) in obs:
            break
        count += 1
    # Handle moving West
    for i in range(c_q - 1, 0, -1):
        if (r_q, i) in obs:
            break
        count += 1
    # Handle moving North-East
    i = r_q + 1
    j = c_q + 1
    while i <= n and j <= n:
        if (i, j) in obs:
            break
        count += 1
        i += 1
        j += 1
    # Handle moving South-East
    i = r_q + 1
    j = c_q - 1
    while i <= n and j >= 1:
        if (i, j) in obs:
            break
        count += 1
        i += 1
        j -= 1
    # Handle moving South-West
    i = r_q - 1
    j = c_q - 1
    while i >= 1 and j >= 1:
        if (i, j) in obs:
            break
        count += 1
        i -= 1
        j -= 1
    # Handle moving North-West
    i = r_q - 1
    j = c_q + 1
    while i >= 1 and j <= n:
        if (i, j) in obs:
            break
        count += 1
        i -= 1
        j += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
