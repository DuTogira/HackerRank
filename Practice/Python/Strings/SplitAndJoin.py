# problem: https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line):
    # write your code here
    l = line.split(" ")
    line = "-".join(l)
    return line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
