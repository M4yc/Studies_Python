#Faça um programa para ler o número de lados de um polígono regular, e a medida
#do lado. Em seguida, ele deve calcular e imprimir o seguinte:
#- Se o número de lados for igual a 3 escrever Triangulo e o valor do seu perímetro;
#- Se o número de lados for igual a 4 escrever Quadrado e o valor da sua área;
#- Se o número de lados for igual a 5 escrever Pentagono;
#- Em qualquer outra situação escrever Poligono não identificado.

n_lados = int(input('Insira o numero de lados de um poligono regular: '))
if n_lados == 3:
    lado1 = float(input("Informe o valor do primeiro lado: "))
    lado2 = float(input("Informe o valor do segundo lado: "))
    lado3 = float(input("Informe o valor do terceiro lado: "))
    peri = lado1+lado2+lado3
    print("É um triangulo.")
    print('Com o perimetro de: %.2f'%peri)
elif n_lados == 4:
    lado1 = float(input("Informe o valor do primeiro lado: "))
    lado2 = float(input("Informe o valor do segundo lado: "))
    area = lado1 * lado2
    print("É um quadrado.")
    print('Com a area de: %.2f' % area)

elif n_lados == 5:
    lado1 = float(input("Informe o valor do primeiro lado: "))
    lado2 = float(input("Informe o valor do segundo lado: "))
    lado3 = float(input("Informe o valor do terceiro lado: "))
    lado4 = float(input("Informe o valor do Quarto lado: "))
    lado5 = float(input("Informe o valor do Quinto lado: "))
    print("É um pentagono.")
else:
    print("Poligono não identificado")