# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    # Get values from the user and save in a nested list
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])

    # Sort the list of students based on score
    sorted_list = sorted(student_list, key=lambda x: x[1])

    # Loop through results and return the second lowest score(s)
    lowest_score = sorted_list[0][1]
    second_lowest_score = 0
    second_lowest_students = []

    for name, score in sorted_list:
        # Sets the second to second lowest score when it finds it
        if score > lowest_score and second_lowest_score is 0:
            second_lowest_score = score
            second_lowest_students.append(name)
        # Checks if any other students have the lowest score
        elif score == second_lowest_score:
            second_lowest_students.append(name)
        # Break when third lowest score reached
        elif score > second_lowest_score:
            break
        else:
            pass

    # Print the students with the second lowest scores in the class
    for student in sorted(second_lowest_students):
        print(student)
