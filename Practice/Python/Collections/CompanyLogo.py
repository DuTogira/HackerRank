# problem: https://www.hackerrank.com/challenges/most-commons/problem


#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    cdict = {}
    for c in s:
        if c not in cdict:
            cdict.update({c: 1})
        else:
            cdict[c] += 1
    cdict = {k: v for k, v in sorted(cdict.items())}
    cdict = {k: v for k, v in sorted(cdict.items(), key=lambda item: item[1], reverse=True)}
    i = 0
    for k, v in cdict.items():
        if i > 2:
            break
        print(k, v)
        i += 1
