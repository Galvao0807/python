
contador = 0
multiplicador = 1
resultado = 0

while multiplicador <= 10:
    contador = 0
    print(f"Tabuada do {multiplicador}")
    while contador <= 10:
        resultado = multiplicador * contador
        print(f"{multiplicador}x{contador}={resultado}")
        contador += 1
    multiplicador += 1
    print()