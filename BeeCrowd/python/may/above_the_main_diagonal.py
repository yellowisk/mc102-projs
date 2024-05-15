def formLines():
    line = []
    for _ in range(12):
        line.append(float(input()))
    return line

def getArea(matrix):
    area = []
    for _ in range(0,11):
        area.append(matrix[_][_+1:])
    return area

def sumArea(area):
    sumArea = 0
    for i in area:
        sumArea += sum(i)
    return sumArea

def averageArea(area):
    length = 0 
    for i in area:
        length += len(i)
    averageArea = sumArea(area) / length
    return averageArea

op = input() #Sum (S) or Average (M)
matrix = []

for _ in range(12):
    matrix.append(formLines())
    
if op == 'S':
    print('{:.1f}'.format(sumArea(getArea(matrix))))
else:
    print('{:.1f}'.format(averageArea(getArea(matrix))))