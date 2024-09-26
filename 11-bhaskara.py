print("Cauculadora da Fórmula de Bhaskara: \n")

a = float(input("Informe o coeficiente a:\n"))
b = float(input("Informe o coeficiente b:\n"))
c = float(input("Informe o coeficiente c:\n"))

# Cálculo de delta.
delta = b**2 - 4*a*c

# Verificando o Delta
if delta < 0:
    print("A equação não possuí raízes reais.")

elif delta == 0:
    x = -b /(2 * a)
    print(f"A única raiz real é {x}")

else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"As raízes reais são {x1:.3f} e {x2:.3f}")