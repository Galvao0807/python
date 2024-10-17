#Declaração das váriaveis
soma = 0
print("Soma dos pares entre 1 e 50: ")
for numero in range (1,51):
    if numero %2 == 0: #Verifica se o número é par
        soma += numero #Adiciona o numero à soma
        print(f"A soma dos números pares entre 1 e 50 é: {soma}")