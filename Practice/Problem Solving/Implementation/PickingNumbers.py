# problem: https://www.hackerrank.com/challenges/picking-numbers/problem


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(a):
    # Write your code here
    biggest = a[0]
    smallest = a[0]
    for num in a:
        if num > biggest:
            biggest = num
        if num < smallest:
            smallest = num
    count_nums = {i: 0 for i in range(smallest, biggest + 1)}
    for num in a:
        count_nums[num] += 1
    big_sum = count_nums[smallest]
    print(count_nums)
    for i in range(smallest, biggest):
        lSum = count_nums[i] + count_nums[i + 1]
        if lSum > big_sum:
            big_sum = lSum
        i += 1
    return big_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
