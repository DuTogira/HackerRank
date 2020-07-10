# problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0
    num_scores = 0
    for score in student_marks[query_name]:
        total += score
        num_scores += 1
    print("{:.2f}".format(total/num_scores))
