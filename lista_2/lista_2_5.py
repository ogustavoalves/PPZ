from random import randint

list_nums = [randint(1, 10000) for _ in range(4)]

min_num = list_nums[0]
max_num = 0
for x in list_nums:
    if x > max_num: max_num = xb 
    if x < min_num: min_num = x

print(f'List: {list_nums}')
print(f'Menor número: {min_num}')
print(f'Maior número: {max_num}')