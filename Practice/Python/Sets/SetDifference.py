# problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem


_ = input()
s1 = set(input().split(" "))
_ = input()
s2 = set(input().split(" "))
print(len(s1.difference(s2)))
