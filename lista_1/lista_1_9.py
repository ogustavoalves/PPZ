# 9.Escreva um programa que pergunte a quantidade de km percorridos 
# por um carro alugado pelo usuário, assim como a quantidade de dias 
# pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo 
# que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

qntd_kms = int(input("Qtnd de kms: "))
dias_alugados = int(input("Qntd de dias alugados: "))

def calc_aluguel(kms, dias):
    return ((kms * 0.15) + (dias * 60))

total_aluguel = calc_aluguel(qntd_kms, dias_alugados)

print(f"R${total_aluguel:.2f}")