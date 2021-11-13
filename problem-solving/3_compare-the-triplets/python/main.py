def compareTriplets(a, b):
    # constraints
    a = [i for i in a if 1 <= i <= 100]
    b = [i for i in b if 1 <= i <= 100]

    alice = 0
    bob = 0

    if len(a) == len(b):
        for i in range(0, len(a)):
            if a[i] > b[i]:
                alice += 1
            elif a[i] < b[i]:
                bob += 1
    return [alice, bob]


# test
print(compareTriplets([5, 6, 7], [3, 6, 10]))
