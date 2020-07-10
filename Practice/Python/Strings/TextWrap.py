# problem: https://www.hackerrank.com/challenges/text-wrap/problem


import textwrap


def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    s, m_w = input(), int(input())
    result = wrap(s, m_w)
    print(result)
