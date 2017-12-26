# https://www.hackerrank.com/challenges/write-a-function/problem

import calendar

def is_leap1(year):
    return calendar.isleap(year)

def is_leap(year):
    leap = False
    
    # If divisible by 4, leap year
    if (year >= 1990 and year%4 is 0):
        # Divisible by 100, not leap year
        # Unless divisible by 400
        if (year%100 is not 0 or year%400 is 0):
            leap = True
    
    return leap

print(is_leap(1992))