
minhalista = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: \n"))
    minhalista.append (numero)

menor = min(minhalista)
maior = max(minhalista)
soma = sum(minhalista)
print(f"\nO menor número da lista: {menor}\n")
print(f"O maior número da lista: {maior}\n") 
print(f"A soma dos números da lista: {soma}\n")

for lista in minhalista:
    print(lista)


