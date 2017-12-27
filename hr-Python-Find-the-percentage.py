# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Get the scores of the queried student
    students_scores = student_marks[query_name]

    # Print the average of their scores
    print("{0:.2f}".format((sum(students_scores))/students_scores.__len__()))
