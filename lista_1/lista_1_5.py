# 5.Solicite o preço de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preço a pagar.
preco_mercadoria = float(input("Digite o preço da mercadoria: R$"))
percentual_desconto = int(input("Digite percentual de desconto: "))

valor_desconto = percentual_desconto * (percentual_desconto / 100)
preco_descontado = preco_mercadoria - valor_desconto
print(f"Valor do desconto R$ {preco_descontado:.2f}")