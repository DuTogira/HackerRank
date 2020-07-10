# problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


n = int(input())
s = set(map(int, input().split()))
numcoms = int(input())
for _ in range(numcoms):
    cmd = input().split(" ")
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))
total = 0
for item in s:
    total += item
print(total)
