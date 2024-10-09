# Ferramenta Continue
# A ferramenta continue no Python vai interromper o loop, mas vai dar continuidade a ele.

contador = 0

while contador <= 40:
    contador += 1

    # Verifica se o valor de 'contador' é múltiplo de 4.
    if (contador % 4 == 0 ):
        print("prim") # Se for múltiplo de 4, imprime "pim"
        continue # Interrompe a iteração atual e volta para o início

    # Se o número não for múltiplo de 4, imprime do valor do contador.
    print(contador)
# Após o término do loop, imprime a mensagem de finalização.
print("Fim do programa")