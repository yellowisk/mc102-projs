def get_total(ages: list, index: int) -> int:
    if index == len(ages) - 1:
        return ages[index]
    else:
        return ages[index] + get_total(ages, index + 1)


def average(nums: list) -> float:
    if not nums:
        return 0.0
    total = get_total(nums, 0)
    return total / len(nums)


numbers = []


while True:
    number = int(input())
    if number > 0:
        numbers.append(number)
    else:
        break
    

print(f'{average(numbers):.2f}')