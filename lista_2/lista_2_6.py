from random import random, randint

salario_info = {
    "horas trabalhadas no mês": 0,
    "salário bruto": 0,
    "salário líquido": 0,
    "imposto de renda": 0,
    "INSS": 0,
    "sindicato": 0
}

# para arredondar os valores em só duas casas decimais
# xx[...],xx
def arredonda(sal_):
   return round(sal_, 2)

# mulplica random por 100 para conseguir um valor com duas casas inteiras 
# usa round para transformar esse valor em somente duas casas decimais: xx,xxxx[...]
salario_por_horas = round(random() * 100)

# retorna um valor entre 200 e 220 que é a quantidade de horas trabalhadas no mês
horas_por_mes = randint(200, 220)

salario_por_mes = round(horas_por_mes * salario_por_horas)

imposto_renda = salario_por_mes * 0.11
sindicato = salario_por_mes * 0.05
inss = salario_por_mes * 0.08

salario_liquido = salario_por_mes - (imposto_renda + sindicato + inss)

# update nos valores do dicionário
salario_info["horas trabalhadas no mês"] = horas_por_mes
salario_info["salário bruto"] = salario_por_mes
salario_info["salário líquido"] = salario_liquido
salario_info["imposto de renda"] = imposto_renda
salario_info["INSS"] = inss
salario_info["sindicato"] = sindicato

# chama função de arredondamento em todos os itens do dict e salva seu retorno
for info, valor in salario_info.items():
   salario_info.update({info: arredonda(valor)})

print(salario_info)