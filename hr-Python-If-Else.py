# https://www.hackerrank.com/challenges/py-if-else/problem

if __name__ == '__main__':
    n = int(input())
    if (n >= 1 and n <= 100):
        # if n is odd print weird
        if(n%2 is not 0):
            print('Weird')
        # n is even
        else:
            # n between 2 and 5 (Not Weird)
            if (n >= 2 and n <= 5):
                print('Not Weird')
            # n between 6 and 20 (Weird)
            elif (n >= 6 and n <= 20):
                print('Weird')
            # n > 20 (Not Weird)
            else:
                print('Not Weird')