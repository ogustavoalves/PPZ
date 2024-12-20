from random import randint

def is_triangulo(x, y, z):
    if x > y + z:
        return False
    elif y > x + z:
        return False
    elif z > x + y:
        return False
    return tipo_triangulo(x, y, z)

def tipo_triangulo(x, y, z):
    if x == y and x == z:
        return "Equilátero"
    elif x != y and y != z and x != z:
        return "Escaleno"
    return "Isóceles"


lado_1 = randint(1, 10)
lado_2 = randint(1, 10)
lado_3 = randint(1, 10)

print(f'Valores dos lados: {lado_1}, {lado_2}, {lado_3}')
if not is_triangulo(lado_1, lado_2, lado_3):
    print("não é um triângulo")
else:
    print(is_triangulo(lado_1, lado_2, lado_3))