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

elif es == 4:
    K = float(input("Informe a temperatura: "))
    F = (K-273)*1.8+32
    print(f"{K}° Kelvin é {F:.1f}° Fahrenheit..")

elif es == 3:
    F = float(input("Informe a temperatura: "))
    K = (F-32)*5/9+273
    print(f"{F}° Fahrenheit é {K:.1f}° Kelvin.")

elif es == 2:
    F = float(input("Informe a temperatura: "))
    C = (F -32)/1.8
    print(f"{F}° Fahrenheit é {C}° Celsius.")

elif es == 1:
    K = float(input("Informe a temperatura: "))
    C = 273 - K
    print(f"{K}° Kelvin é {C}° Celsius.")

elif es == 0:
    C = float(input("Informe a temperatura: "))
    F = 1.8 * C + 32
    print(f"{C}° Celsius é {F:.1f}° Fahrenheit..")