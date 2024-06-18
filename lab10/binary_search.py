def bin_search(v, target, left, right):
    if right >= left:
        mid = (right + left) // 2
        
        if v[mid] == target:
            return mid
        elif v[mid] > target:
            return bin_search(v, target, left, mid - 1)
        else:
            return bin_search(v, target, mid + 1, right)
    else:
        return -1

nums = list(map(int, input().split()))
target = int(input())

print(bin_search(nums, target, 0, len(nums) - 1))