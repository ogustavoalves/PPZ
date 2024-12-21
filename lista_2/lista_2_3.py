from random import randint

peso_peixe = randint(1, 100)

def calc_multa(peso):
    multa = 0
    excesso = 0

    if peso > 50:
        excesso = peso - 50
        multa = 4 * excesso
    else:
        excesso = 'ZERO'
        multa = 'ZERO'
    
    return excesso, multa
excesso, multa = calc_multa(peso_peixe)

print(f'peso: {peso_peixe}kg multa = R$ {multa}, excesso = {excesso} kg')