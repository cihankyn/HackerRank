# Q Url : https://www.hackerrank.com/challenges/python-string-split-and-join/problem
def split_and_join(line):
    return "-".join(line.split(" "))


# test
print(split_and_join("this is a string"))
