cases = int(input())
memory = {}

def fibonacci(n: int) -> int:
    if n in memory:
        return memory[n]
    if n < 2:
        return n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        memory[n] = result
        return result
    
    
def calls(n: int) -> int:
    if n < 2:
        return 1
    return calls(n-1) + calls(n-2) + 2

for _ in range(cases):
    number = int(input())
    print(f'Fib({number}) = {fibonacci(number)} & calls = {calls(number)}')

