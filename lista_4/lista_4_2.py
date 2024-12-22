from random import randint

lista_nums = [randint(0, 101) for _ in range(20)]

lista_pares = []
lista_impares = []
for x in lista_nums:
    if x % 2 == 0: lista_pares.append(x)
    else: lista_impares.append(x)

print(f'lista de números: {lista_nums}')
print(f'lista de números pares: {lista_pares}')
print(f'lista de números ímpares: {lista_impares}') 

