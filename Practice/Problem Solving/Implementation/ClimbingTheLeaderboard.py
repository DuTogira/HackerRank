# problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    results = []
    rank = {}
    i = 1
    for score in scores:
        if score not in rank:
            rank[score] = i
            i += 1
    # print(rank)
    high = len(scores) - 1
    mid = 0
    for game in alice:
        # print(results)
        low = 0
        while low <= high:
            mid = (high + low) // 2
            # print('Game: ', game, ' Mid: ', mid)
            if (mid == 0 and scores[mid] < game) or game == scores[mid] or \
                    (scores[mid - 1] > game > scores[mid]):
                results.append(rank[scores[mid]])
                break
            elif mid == high:
                results.append(rank[scores[mid]] + 1)
                break
            elif scores[mid] > game:
                low = mid + 1
            else:
                high = mid - 1
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
