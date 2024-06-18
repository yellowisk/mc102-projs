def get_z(X: int) -> int:
    Z = int(input())
    if Z <= X:
        return get_z(X)
    else:
        return Z

def min_sum(X: int, Z: int, current_sum: int = 0, count: int =0) -> int:
    if current_sum > Z:
        return count
    else:
        return min_sum(X + 1, Z, current_sum + X, count + 1)

X = int(input())

Z = get_z(X)

result = min_sum(X, Z)
print(result)
