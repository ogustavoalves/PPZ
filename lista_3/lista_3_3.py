from math import floor
pop_pais_A = 80000
tax_crescimento_pais_A = 0.03
pop_pais_B = 200000
tax_crescimento_pais_B = 0.015

anos = 0
while (pop_pais_A <= pop_pais_B):
    pop_pais_A += pop_pais_A * tax_crescimento_pais_A
    pop_pais_B += pop_pais_B * tax_crescimento_pais_B
    anos += 1

pop_pais_A = floor(pop_pais_A)
pop_pais_B = floor(pop_pais_B)
print(f'Demorará {anos} anos para a população do país A será igual à do país B')
print(f'População país A: {pop_pais_A}; População país B: {pop_pais_B}')