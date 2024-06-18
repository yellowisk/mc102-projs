def find_sums(n):
    def recursor(target, current_sum, start, path):
        if current_sum == target:
            print('+'.join(map(str, path)) + '=' + str(target))
            return
        for i in range(start, target - current_sum + 1):
            recursor(target, current_sum + i, i, path + [i])

    recursor(n, 0, 1, [])

find_sums(int(input()))