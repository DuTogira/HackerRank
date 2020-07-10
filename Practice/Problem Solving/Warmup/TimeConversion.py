# problem: https://www.hackerrank.com/challenges/time-conversion/problem


# !/bin/python3

import os
import sys
from datetime import datetime


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    newDate = datetime.strptime(str(s), "%I:%M:%S%p").strftime("%H:%M:%S")
    return newDate


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
