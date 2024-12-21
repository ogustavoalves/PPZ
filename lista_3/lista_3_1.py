from random import randint

def is_number_valid(number):
    if number >= 1 and number <= 10:
        return True
    return False

user_number = randint(1, 1000)
while not is_number_valid(user_number):
    print(f'número {user_number} não é válido')
    user_number = randint(1, 1000)

print(f'número {user_number} é válido')




