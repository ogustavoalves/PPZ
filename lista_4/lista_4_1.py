from random import randint

array_nums = [randint(0, 101) for _ in range(0, 10)]

min_value = array_nums[0]
max_value = 0
for x in array_nums:
    if x > max_value: max_value = x
    if x < min_value: min_value = x

print(array_nums)
print(f'menor valor: {min_value}; maior valor: {max_value}')