# URL : https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    mini = sum(sorted(arr)[0:4])
    max = sum(sorted(arr, reverse=True)[0:4])
    print(mini, max)


# test
miniMaxSum([3, 5, 1, 9, 7])
