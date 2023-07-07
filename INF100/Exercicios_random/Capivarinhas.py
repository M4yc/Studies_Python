#programa para calcular peso das capivarinhas da ufv
#Capivara 1
peso1 = float(input("Informe o peso da 1° capivara: "))
n = 0
somapeso = 0
pesomedio = 0
if peso1 > 0:
    n = n+1
    somapeso = somapeso + peso1
else:
    print("Peso inválido!")
#Capivara 2
peso2 = float(input("Informe o peso da 2° capivara: "))
if peso2 > 0:
    n = n + 1
    somapeso = somapeso + peso2
else:
    print("Peso inválido!")
#Capivara 3
peso3 = float(input("Informe o peso da 3° capivara: "))
if peso3 > 0:
    n = n + 1
    somapeso = somapeso + peso3
else:
    print("Peso inválido!")
#Capivara 4
peso4 = float(input("Informe o peso da 4° capivara: "))
if peso4 > 0:
    n = n + 1
    somapeso = somapeso + peso4
else:
    print("Peso inválido!")

if n !=0:
    pesomedio = somapeso / n
    print("")
    print('O peso medio das capivaras foi: %.2f Kg' % pesomedio)
else:
    print("")
    print("(Nenhum valor valido inserido!)")