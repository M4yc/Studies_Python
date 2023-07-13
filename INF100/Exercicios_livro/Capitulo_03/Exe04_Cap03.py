#programa de conversão de temperatura
print("[0] De Celsius para Fahrenheit.")
print("[1] De Celsius para Kelvin.")
print("[2] De Fahrenheit para Celsius.")
print("[3] De Fahrenheit para Kelvin.")
print("[4] De Kelvin para Fahrenheit")
print("[5] De Kelvin para Celsius")

es = int(input("Qual opção você esolhe: "))
if es == 5:
    C = float(input("Informe a temperatura: "))
    K = C + 273
    print(f"{C}° Celsius é {K}° Kelvin.")
elif es == 1:
    K = float(input("Informe a temperatura: "))
    C = 273 - K
    print(f"{K}° Kelvin é {C}° Celsius.")
    print("%f° Kelvin é %f° Celsius."%(K,C))