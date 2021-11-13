import math


def aVeryBigSum(ar):
    ar = [i for i in ar if 0 <= i <= math.pow(10, 10)]
    total = 0
    for i in ar:
        total += i
    return total


# test
print(aVeryBigSum([3, 4, 5]))
