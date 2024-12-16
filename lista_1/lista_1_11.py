# 11.Sabendo que str( ) converte valores numéricos para string, 
# calcule quantos dígitos há em 2 elevado a um milhão.

  # para remover o limite de caracteres que se pode converter de int para str:
import sys
sys.set_int_max_str_digits(0)

  # resolução do problema:
print(len(str(2**1000000)))