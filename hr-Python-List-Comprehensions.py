# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Return arrays of all coordinates which don't add up to n (x + y + z != n)
    print([[x_coordinate, y_coordinate, z_coodinate]
           for x_coordinate in range(0, x + 1)
           for y_coordinate in range(0, y + 1)
           for z_coodinate in range(0, z + 1)
           if ((x_coordinate + y_coordinate + z_coodinate) != n)
           ])
