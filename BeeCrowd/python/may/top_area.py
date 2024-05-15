def formLines():
    line = []
    for _ in range(12):
        line.append(float(input()))
    return line

def getArea(matrix):
    area = []
    for _ in range(0,5):
        area.append(matrix[_][_+1:11-_])
    return area

def sumArea(area):
    sumArea = 0
    for i in area:
        sumArea += sum(i)
    return sumArea

def averageArea(area):
    averageArea = sumArea(area) / 30
    return averageArea

op = input() #Sum (S) or Average (M)
matrix = []

for _ in range(12):
    matrix.append(formLines())
    
if op == 'S':
    print('{:.1f}'.format(sumArea(getArea(matrix))))
else:
    print('{:.1f}'.format(averageArea(getArea(matrix))))