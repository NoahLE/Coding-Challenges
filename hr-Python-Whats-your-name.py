# https://www.hackerrank.com/challenges/whats-your-name/problem


def print_full_name(a, b):
    # F-strings don't work :(
    print("Hello {a} {b}! You just delved into python.".format(a=a, b=b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
