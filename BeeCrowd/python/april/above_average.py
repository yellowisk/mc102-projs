def getStudentsAboveAverage(grades):
    students = grades.pop(0)
    totalGrades = 0
    count = 0
    for i in grades:
        totalGrades += i
    average = totalGrades/students
    for i in grades:
        if i > average:
            count += 1
    return "{:.3f}%".format(count/students * 100)

cases = int(input())
for i in range(cases):
    studentsAndGrades = list(map(int, input().split()))
    print(getStudentsAboveAverage(studentsAndGrades))