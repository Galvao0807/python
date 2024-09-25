# Atividade 08-tabuada.py
# Faça um programa que mostre a tabuada de um número que o usuário escolher.

contador = 0
multiplicador = int(input("Digite o numero da tabuada:\n\n"))
resultado = 0


while contador <= 10 and multiplicador:
    resultado = multiplicador * contador
    print(f"{multiplicador}x{contador}={resultado}")
    contador += 1
