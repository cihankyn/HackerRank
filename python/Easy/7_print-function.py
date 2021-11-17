# Q Url : https://www.hackerrank.com/challenges/python-print/problem
n = 5
result = ""
if 1 <= n <= 150:
    for i in range(1, n+1):
        result += str(i)
print(result)
