# Q Url : https://www.hackerrank.com/challenges/string-validators/problem

s = "qA2"
if 0 < len(s) < 1000:
    hasAlphaNumeric = hasAlpha = hasDigit = hasLower = hasUpper = False

    for i in s:
        if i.isalnum() and hasAlphaNumeric == False:
            hasAlphaNumeric = True
        if i.isalpha() and hasAlpha == False:
            hasAlpha = True
        if i.isdigit() and hasDigit == False:
            hasDigit = True
        if i.islower() and hasLower == False:
            hasLower = True
        if i.isupper() and hasUpper == False:
            hasUpper = True

    print(hasAlphaNumeric)
    print(hasAlpha)
    print(hasDigit)
    print(hasLower)
    print(hasUpper)
