# Q Url : https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count = 0
    if 1 <= len(string) <= 200:
        for i in range(len(string)):
            if string[i:i+len(sub_string)] == sub_string:
                count += 1
        return count


# test
print(count_substring("ABCDCDC", "CDC"))
