# 09-rent-car.py = escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado pelo usuario,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o 
# carro custa R$ 60 por dia e R$ 0,15 por km rodado.

# Variavel
dias_locados = int(input("Dias alugados:\n"))
km_percorridos = int(input("Digite os km percorridos:\n\n"))

# calculo do preço total
total = (dias_locados*60)+(km_percorridos*0.15)
print(f"O valor total a pagar é R$ {total:.2f}")