#O Dia da Páscoa, por definição, é o primeiro Domingo após a primeira lua cheia que
#ocorre depois do equinócio da Primavera (no hemisfério norte, Outono no hemisfério
#sul), e pode cair entre 22 de Março e 25 de Abril. As fórmulas existentes calculam o
#que se convencionou chamar de "Cálculo Eclesiático", definido pelo Concílio de
#Nicea (325 d.C.). Existem diversas fórmulas para se determinar o Domingo de
#Páscoa, entretanto uma das mais simples é a fórmula de Gauss, descrita a seguir.
#Para calcular o dia da Páscoa (Domingo), usa-se a fórmula abaixo, onde o ANO
#deve ser introduzido com 4 dígitos e X e Y são dados pela tabela a seguir.

ano = int(input("Digite um ano: "))

if not ano >= 1582 and ano <= 2499:
    print("Ano Invalido.")

if ano >= 1582 and ano <= 1699:
    x = 22
    y = 2
elif ano >= 1700 and ano <= 1799:
    x = 23
    y = 3
elif ano >= 1800 and ano <= 1899:
    x = 23
    y = 4
elif ano >= 1900 and ano <= 2099:
    x = 24
    y = 5
elif ano >= 2100 and ano <= 2199:
    x = 24
    y = 6
elif ano >= 2200 and ano <= 2299:
    x = 25
    y = 0
elif ano >= 2300 and ano <= 2399:
    x = 26
    y = 1
elif ano >= 2400 and ano <= 2499:
    x = 25
    y = 1

#a = ANO MOD 19
#b= ANO MOD 4
#c = ANO MOD 7
#d = (19 * a + X) MOD 30
#e = (2 * b + 4 * c + 6 * d + Y) MOD 7