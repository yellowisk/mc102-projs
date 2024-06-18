def quick_sort(v):
    if len(v) <= 1:
        return v
    
    pivot = v[len(v) // 2]
    l = [x for x in v if x < pivot]
    r = [x for x in v if x > pivot]
    mid = [x for x in v if x == pivot]
    
    return quick_sort(l) + mid + quick_sort(r)

sequence = quick_sort(list(map(int, input().split())))
print(*sequence)
