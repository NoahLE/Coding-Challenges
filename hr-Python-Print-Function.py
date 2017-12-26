# https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    # Print all values from 1 to n (user input) without concatenation
    for i in range(1, n+1):
        print(i, end='')