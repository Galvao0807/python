# Declaração da função exibirMensagem(nome)
def exibirMensagem(nome, idade):
    print(f"Olá, {nome} com {idade} anos!")

def somar(a, b):
    return a + b


def calcularAreaCirculo(raio):
    area = 3.1415 * raio**2
    return area



# início do meu algoritmo
nome = input("Digite o seu nome: \n")
idade = input("Digite a sua idade: \n")
exibirMensagem(nome, idade) # Exibe a mensagem com o nome do usuário.

valorA = int(input("Digite o primeiro número: \n"))
valorB = int(input("Digite o segundo número: \n"))
resultado = somar(valorA, valorB)
print(f"O resultado da soma: \n{resultado}")

# Calcular área do círculo
print("Área do circulo!")
raio = float(input("Digite o valor do raio: "))
area = calcularAreaCirculo(raio)
print(f"Área do circulo: {area:.2f}")