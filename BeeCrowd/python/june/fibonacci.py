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

for _ in range(cases):
    number = int(input())
    print(f'Fib({number}) = {fibonacci(number)}')
