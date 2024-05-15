def evalutePerfection(number):
    for j in range(1,number):
        if number % j == 0:
            divisors.append(j)
    if sum(divisors) == number:
        print(number, "eh perfeito")
    else:
        print(number, "nao eh perfeito")

cases = int(input())
for i in range(cases):
    number = int(input())
    divisors = []
    evalutePerfection(number)