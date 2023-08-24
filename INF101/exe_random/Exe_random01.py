def leiaInt(msg, vmin, vmax):
    v = int(input(msg))
    while v < vmin or v > vmax:
        print("***Entrada errada!,Valor deve estar entre 10 e 20.")
        v = int(input(msg))
    return v
v0 = leiaInt('Digite um numero: ', 10,20)
print('Teste')
print(v0)