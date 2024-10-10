def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return celsius_para_kelvin(fahrenheit_para_celsius(fahrenheit))

def kelvin_para_fahrenheit(kelvin):
    return celsius_para_fahrenheit(kelvin - 273.15)

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15



while True:
    print("\nMenu:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Celsius para Kelvin")
    print("3. Converter de Fahrenheit para Celsius")
    print("4. Converter de Fahrenheit para Kelvin")
    print("5. Converter de Kelvin para Fahrenheit")
    print("6. Converter de Kelvin para Celsius")
    print("7. Sair")

    escolha = input("Escolha uma opção (1-7): ")    

    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C = {celsius_para_fahrenheit(celsius)}°F")
    elif escolha == '2':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C = {celsius_para_kelvin(celsius)}K")
    elif escolha == '3':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_para_celsius(fahrenheit)}°C")
    elif escolha == '4':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_para_kelvin(fahrenheit)}K")
    elif escolha == '5':
            
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print(f"{kelvin}K = {kelvin_para_fahrenheit(kelvin)}°F")
    elif escolha == '6':
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print(f"{kelvin}K = {kelvin_para_celsius(kelvin)}°C")
    elif escolha == '7':
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")