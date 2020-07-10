# problem: https://www.hackerrank.com/challenges/python-lists/problem


if __name__ == '__main__':
    N = int(input())
    i = 0
    l = []
    while i < N:
        dat = input().split(' ')
        name = dat[0]
        if name == 'insert':
            l.insert(int(dat[1]), int(dat[2]))
        elif name == 'append':
            l.append(int(dat[1]))
        elif name == 'remove':
            l.remove(int(dat[1]))
        elif name == 'sort':
            l.sort()
        elif name == 'reverse':
            l.reverse()
        elif name == 'pop':
            l.pop()
        elif name == 'print':
            print(l)
        i += 1
