from random import randint

nums = [randint(1, 500) for _ in range(0, 2)]

a = max(nums)
b = min(nums)
print(f'a: {a}')
print(f'b: {b}')

r = 0
while a % b > 0:
   r = a % b 
   a = b
   b = r

print(f'{nums}')
print(f'maior divisor: {b}')

    

