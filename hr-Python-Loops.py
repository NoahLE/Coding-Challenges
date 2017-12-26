# https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(input())
    # n is not negative
    # n is between 1 and 20
    if (n > 0 and n < 20):
        # for all integers(i) less than n, print i**2
        [print(n*n) for n in range(n)]