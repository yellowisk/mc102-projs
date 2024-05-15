def sumMatrix(matrix, target):
    result = 0
    for j in range(len(matrix[target])):
        result += matrix[target][j]
    return result

def averageMatrix(matrix, target):
    result = 0
    for j in range(len(matrix[target])):
        result += matrix[target][j]
    return sumMatrix(matrix, target) / len(matrix[target])

def formLines():
    line = []
    for _ in range(12):
        line.append(float(input()))
    return line

target = int(input())
op = input() #Sum (S) or Average (M)
matrix = []

for _ in range(12):
    matrix.append(formLines())
if op == 'S':
    print(sumMatrix(matrix, target))
else:
    print(averageMatrix(matrix, target))