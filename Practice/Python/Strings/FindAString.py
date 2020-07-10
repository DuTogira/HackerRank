# problem: https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    s = input().strip()
    s_s = input().strip()

    c = count_substring(s, s_s)
    print(c)
