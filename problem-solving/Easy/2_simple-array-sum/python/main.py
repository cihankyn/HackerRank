# URL : https://www.hackerrank.com/challenges/simple-array-sum/problem
def simpleArraySum(ar):
    constraint = [i for i in ar if 0 < i <= 1000]
    total = 0
    for i in constraint:
        total += i
    return total


# test
print(simpleArraySum([3, 4, 5, 0, 2]))
