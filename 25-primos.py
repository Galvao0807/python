x = int(input('Digite um número para a verificação: \n\n'))
primo = True

if x < 2:
    primo = False
else:
    for i in range (2, int(x **0.5 ) + 1):
        if x % i == 0:
            primo = False
            break

if primo:
    print(f"\n{x} é um número primo.")
else:
    print(f"\n{x} não é um numero primo.")