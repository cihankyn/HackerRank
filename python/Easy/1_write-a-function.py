# Q : Write a function
# Q Url : https://www.hackerrank.com/challenges/write-a-function/problem
import math


def is_leap(year):
    leap = False

    # Write your logic here
    if year >= 1900 and year <= 100000:
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        else:
            leap = year % 4 == 0
    return leap


# test
print(is_leap(1900))  # false
print(is_leap(2100))  # false
print(is_leap(2000))  # true
print(is_leap(2004))  # true
print(is_leap(1600))  # false (out of range)
print(is_leap(1000000))  # false (out of range)
