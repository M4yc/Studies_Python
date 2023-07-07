#programa para calcular peso das capivarinhas da ufv
#Capivara 1

num = int(input("Informe o numero de capivaras: "))
n = 0 #inicialização do contador com 0
somapeso = 0
pesomedio = 0


while n < num:
    peso = float(input("Informe o peso da %d° capivara: " %(n+1)))
    if peso > 0:
        n = n + 1
        somapeso = somapeso + peso
    else:
        print("Peso inválido!")

if n !=0:
    pesomedio = somapeso / n
    print("")
    print('O peso medio das capivaras foi: %.2f Kg' % pesomedio)
else:
    print("")
    print("(Nenhum valor valido inserido!)")