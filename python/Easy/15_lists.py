# Q Url : https://www.hackerrank.com/challenges/python-lists/problem

l = []
N = int(input())
for i in range(N):
    command = input().split()
    commandText = command[0]
    commandParameters = [int(i) for i in command[1:] if i.isdigit()]

    if commandText == "print":
        print(l)
    elif commandText == "remove":
        l.remove(commandParameters[0])
    elif commandText == "append":
        l.append(commandParameters[0])
    elif commandText == "insert":
        l.insert(commandParameters[0], commandParameters[1])
    elif commandText == "sort":
        l.sort()
    elif commandText == "pop":
        l.pop()
    elif commandText == "reverse":
        l.reverse()
