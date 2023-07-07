#Escreva um programa que leia o valor de 3 ângulos de um triângulo. Se os ângulos
#formarem um triângulo (soma deles igual a 180°) então, escreva se o triângulo é
#acutângulo, retângulo ou obtusângulo. Caso contrário, escreva que os ângulos não
#formam um triângulo.
#Observação: triângulo retângulo possui um ângulo reto (90°); triângulo obtusângulo:
#possui um ângulo obtuso (ângulo maior que 90°); e triângulo acutângulo: possui 3
#ângulos agudos (ângulo menor que 90°)

an1 = int(input("Insira o primeiro angulo de um triangulo: "))
an2 = int(input("Insira o segundo angulo de um triangulo: "))
an3 = int(input("Insira o Terceir angulo de um triangulo: "))

if an1 + an2 + an3 == 180:
    if an1 == 90 or an2 == 90 or an3 == 90:
        print("Triangulo retângulo.")

    elif an1 > 90 or an2 > 90 or an3 > 90:
        print("Triangulo obtusângulo")

    elif an1 < 90 and an2 < 90 and an3 < 90:
        print("Triangulo acutângulo.")

else:
    print("Esses angulos não formam um triangulo.")