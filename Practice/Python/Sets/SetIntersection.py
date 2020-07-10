# problem: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


_ = input()
s1 = set(input().split(" "))
_ = input()
s2 = set(input().split(" "))
s1 = s1.intersection(s2)
print(len(s1))
