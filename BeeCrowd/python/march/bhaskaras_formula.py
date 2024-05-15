import math

A, B, C = map(float,input().split())
squareRoot = 0

if (((B**2)-(4*A*C))<0):
    print('Impossivel calcular')
    exit()
else:
    squareRoot = math.sqrt((B**2)-(4*A*C))

if(2*A == 0):
    print('Impossivel calcular')
    exit()

R1cima = -B+squareRoot
R2cima = -B-squareRoot

print(f'R1 = {R1cima/(2*A):.5f}')
print(f'R2 = {R2cima/(2*A):.5f}')