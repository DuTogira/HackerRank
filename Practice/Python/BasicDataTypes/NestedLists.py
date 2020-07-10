# problem: https://www.hackerrank.com/challenges/nested-list/problem


if __name__ == '__main__':
    record = []
    runners = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([score, name])
    low = min(record)
    while min(record)[0] == low[0]:
        record.remove(min(record))
    low = min(record)
    while record and min(record)[0] == low[0]:
        runners.append(min(record))
        record.remove(min(record))
    for runner in runners:
        print(runner[1])
