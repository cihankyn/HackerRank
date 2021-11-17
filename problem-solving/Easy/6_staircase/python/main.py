# URL : https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    if 0 < n <= 100:
        for i in range(n, 0, -1):
            string = ""
            for j in range(1, n+1):
                if j < i:
                    string += " "
                else:
                    string += "#"
            print(string)


# test
staircase(6)
