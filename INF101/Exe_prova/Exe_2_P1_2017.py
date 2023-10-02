def addOne(d,m,a):
    lista = ([d],[m],[a])

#Verificação de ano bissextos
#Ano bissexto se for divisivel por 4 mas não por 100
    if a % 4 != 0 and a % 100 == 0 or a % 400 == 0:
        print("Ano bissexto")
    else:
        print("Não é bissexto")