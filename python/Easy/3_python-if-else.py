n = 3
result = ""
if 1 <= n <= 100:
    if n % 2 == 1:
        result = "Weird"
    elif n % 2 == 0 and 2 < n < 5:
        result = "Not Weird"
    elif n % 2 == 0 and 6 < n <= 20:
        result = "Weird"
    else:
        result = "Not Weird"

print(result)
