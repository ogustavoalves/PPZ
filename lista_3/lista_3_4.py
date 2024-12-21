from random import randint

fibonacci_list = [1, 1,]

user_number = randint(3, 50)
sum_ = 0
for x in range(user_number):
    sum_ = fibonacci_list[x-1] + fibonacci_list[x]
    fibonacci_list.append(sum_)

print(f'número do usuário: {user_number}')
print(f'Fibonacci lista: {fibonacci_list}')
print(fibonacci_list[user_number])

