valor = int(input("Digite o valor a pagar: \n\n"))
cedulas_disponiveis = [50, 20, 10 , 5, 1]
apagar = valor

for cedula in cedulas_disponiveis:
    quantidade_cedulas = apagar // cedula
    if quantidade_cedulas > 0:
        print(f"{quantidade_cedulas} cédula(s) de R${cedula:.2f}")
    apagar = apagar % cedula
    
    if apagar == 0:
        break
    
