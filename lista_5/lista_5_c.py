count = 0
for num in range(1067, 3628):
    if (num % 7 == 0) and (num % 2 == 0): count += 1

print(f'Resposta: {count}')