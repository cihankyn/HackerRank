# URL : https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    positive = negative = zero = 0
    if 0 < len(arr) <= 100:
        for i in arr:
            if -100 <= i <= 100:
                if i < 0:
                    negative += 1
                elif i == 0:
                    zero += 1
                else:
                    positive += 1

    print(positive/len(arr))
    print(negative/len(arr))
    print(zero/len(arr))


# test
plusMinus([-4, 3, -9, 0, 4, 1])
