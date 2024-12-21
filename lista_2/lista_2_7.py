from random import randint
from math import ceil

area_metros_quadrados =  randint(1, 500)
litros_necessarios = ceil(area_metros_quadrados / 3)
custo_tinta = litros_necessarios * 80

print(f'area printada: {area_metros_quadrados} m²; tinta necessária: {litros_necessarios} l; custo  R${custo_tinta:.2f}')