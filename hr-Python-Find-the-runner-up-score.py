# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    # Represents the number of scores
    n = int(input())

    # An array with the score results
    arr = map(int, input().split())
    sorted_array = sorted(list(arr), reverse=True)

    # Return the second to highest number
    # Check if multiple max values, if so, loop back until the next highest value is found
    max_value, runner_up = sorted_array[0], sorted_array[0]
    for item in sorted_array:
        if item < max_value:
            runner_up = item
            break

    print(runner_up)
