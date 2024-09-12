# Abaixo do peso - IMC < 18,5
# Peso normal - IMC entre 18,5 e 24,9
# Sobrepeso - IMC entre 25 e 34,9
# Obesidade - IMC a partir de 35

print("Programa para calculo IMC!")
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))
imc = peso / (altura**2)
print(f"Seu IMC é {imc:.2f}") # .2f é usado para mostrar apenas duas casas decimais.



if (imc<= 18.5):
    print("Abaixo do peso.")
    print("Indico um nutricionista, para fazer um dieta para engordar, você precisa ficar saudavel.")
elif(imc>=18.5 and imc<=24.9): 
    print("Peso normal")
    print("Você está saudável! Parabéns.")
elif(imc>=25  and imc<=34.9):
    print("Acima do peso.")
    print("Já que você está acima do peso, tome cuidado antes que piore a sua situação")
else:
    print("Obesidade")
    print("Procure um nutri, e faça sua dieta, ser obeso prejudica sua saúde!")

print("Fim do código")



