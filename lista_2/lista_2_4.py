from random import randint

list_num = [randint(1, 1000) for _ in range(4)]

max_num = 0
for x in list_num:
    if x > max_num: max_num = x

print(f'Lista = {list_num}')
print(f'Maior número = {max_num}')