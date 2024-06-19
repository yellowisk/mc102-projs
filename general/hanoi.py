import time

def hanoi(n, i, j, k):
    if n >= 1:
        hanoi(n-1, i, k, j)
        print(f'Move disk {n} from rod {i} to rod {j}')
        hanoi(n-1, k, j, i)

def count_hanoi_moves(n):
    if n == 1:
        return 1
    return 2 * count_hanoi_moves(n-1) + 1

start = time.time()
n = 14
hanoi(n, 'A', 'C', 'B')
print(count_hanoi_moves(n))
print(f'Time: {time.time() - start}')