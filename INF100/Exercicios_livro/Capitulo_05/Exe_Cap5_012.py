#Escreva um programa que leia a velocidade máxima permitida de uma avenida e a
#velocidade com que o motorista estava dirigindo nela e calcule a multa que uma
#pessoa vai receber, sabendo que são pagos:
#a) Nenhuma multa, se não ultrapassou a velocidade máxima;
#b) 50 reais se o motorista ultrapassar em até 20km/h da velocidade máxima permitida;
#c) 100 reais, se o motorista ultrapassar de 21km/h a 40 km/h a velocidade máxima permitida;
#d) 200 reais, se estiver acima de 41km/h da velocidade máxima permitida

velo_max = int(input("Insira a Velocidade maxima permitida na via: "))
velo = int(input("Insira a velocidade que você estava dirigindo: "))

exce = velo - velo_max

if velo == velo_max or velo < velo_max:
    print("Nenhuma multa estava dentro da velocidade permitida.")
elif exce <= 20:
    print("MULTA excesso de velocidade multa de R$ 50,00.")
elif exce >=21 and exce <= 40:
    print("MULTA excesso de velocidade multa de R$ 100,00.")
elif exce >= 41:
    print("MULTA excesso de velocidade multa de R$ 200,00.")