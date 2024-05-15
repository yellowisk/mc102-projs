number1 = int(input())
number2 = int(input())

def printOdds(firstNumber, secondNumber):
    listSum = 0
    for i in range(firstNumber,secondNumber+1,1):
        if i % 2 == 0:
            continue
        if i == number1 or i == number2:
            continue
        else:
            listSum = listSum + i
            continue
    print(listSum)

if number2 < number1:
    printOdds(number2, number1)
else:
    printOdds(number1, number2)
