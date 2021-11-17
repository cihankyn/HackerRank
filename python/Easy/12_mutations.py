# Q Url : https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    return f"{string[:position]}{character}{string[position+1:]}"


# test
print(mutate_string("abracadabra", 5, "k"))
