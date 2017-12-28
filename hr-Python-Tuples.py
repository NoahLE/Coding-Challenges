# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    # number of integers
    n = int(input())

    # integer list
    integer_list = map(int, input().split())

    # create tuple of integers
    tuple_list = tuple(integer_list)

    # compute and print hash
    print(tuple_list.__hash__())
