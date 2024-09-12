# Algoritmo
#
#
#
#

idade = int(input("Digite a sua idade: "))

if (idade>= 18 and idade <65):
    print("Voto obrigatorio.")
    print("Caso não votar, levará multa.")
elif(idade >=16 and idade <=17 or idade>65): 
    print("Voto opcional!")
    print("Nesse caso, você não tem obrigação! Viva a sua vida, obrigado.")
else:
    print("Voto não permitido")
    print("Você é muito novo ainda, porque perguntou?")

print("\n\nFIM DO PROGRAMA")


