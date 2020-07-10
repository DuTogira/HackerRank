# problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    top = max(arr)
    while max(arr) == top:
        arr.remove(max(arr))
    print(max(arr))
