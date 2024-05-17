import math

def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def grade(n):
    grade = ""
    if n < 35:
        grade = "F"
    elif n>=35 and n<60:
        grade = "C"
    elif n>=60 and n<80:
        grade = "B"
    elif n>=80 and n<=100:
        grade = "A"
    return grade

marks = []
for i in range(6):
    marks.append(normal_round(float(input())))
grades = []
for i in range(6):
    grades.append(grade(marks[i]))
for i in range(6):
    print(grades[i])