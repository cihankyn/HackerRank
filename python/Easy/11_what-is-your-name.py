# Q Url : https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(first, last):
    if len(first) <= 10 and len(last) <= 10:
        print(f"Hello {first} {last}! You just delved into python.")


# test
print(print_full_name("cihan", "koyun"))
