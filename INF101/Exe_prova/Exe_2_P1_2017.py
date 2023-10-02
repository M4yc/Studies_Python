def addOne(d,m,a):
    lista = ([d],[m],[a])

def dias_mes(m,a):
    if m == 2 and bissexto(a) == True:
        return 29
    elif m == 2:
        return 28
    elif m in [4,6,9,11]:
        return 30
    else:
        return 31

def bissexto(a):
    # Verificação de ano bissextos
    # Ano bissexto se for divisivel por 4 mas não por 100
    if a % 4 != 0 and a % 100 == 0 or a % 400 == 0:
        #print("Ano bissexto")
        return True
    else:
        #print("Não é bissexto")
        return False