def addOne(d,m,a):
    lista = ([d],[m],[a])
    if d < dias_mes(m,a):
        return (d + 1, m, a)
    else:
        if m < 12:
            return (1, m + 1, a)
        else:
            return (1, 1, a + 1)


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

data_at = (28,2,2022)
nova_data = addOne(*data_at)
print(f"Data atual: {data_at}")
print(f"Nova data: {nova_data}")