# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    string_length = len(string)
    substring_length = len(sub_string)

    loop_times = (string_length-substring_length+1)
    times_found = 0

    for start in range(loop_times):
        the_slice = string[start:substring_length+start]
        if the_slice == sub_string:
            times_found += 1

    return times_found


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
