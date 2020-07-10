# problem: https://www.hackerrank.com/challenges/py-set-union/problem


n1 = int(input())
s1 = set(input().split(" "))
n2 = int(input())
s2 = set(input().split(" "))
s1 = s1.union(s2)
i = 0
for elem in s1:
    i += 1
print(i)
