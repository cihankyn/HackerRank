# Q Url : https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input("Count :"))
student_marks = {}
for _ in range(n):
    if 1 <= n <= 10:
        name, *line = input("Enter :").split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input("Query : ")
result = student_marks[query_name]
print(f"{sum(result)/len(result):.2f}")
