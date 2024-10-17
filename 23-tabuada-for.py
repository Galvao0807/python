numero=int(input("Digite um número: "))
print(f"Tabuada do número {numero}:")
for multiplicador in range (1,11): # tabuada do 1 ao 10
    resultado = numero * multiplicador
    print(f"{numero}x{multiplicador}={resultado}")