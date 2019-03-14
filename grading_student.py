n = int(input().strip())
for i in range(0, n):
    grade = int(input().strip())
    if grade >= 38 and grade % 5 >= 3:
      grade = grade + (5 - (grade % 5))
    print(grade)
        