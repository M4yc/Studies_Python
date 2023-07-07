# Faça um programa para ler o tempo gasto por dois maratonistas para completar uma
#prova, informando quem foi o vencedor e calculando a diferença de tempo entre
#eles. Todos os valores serão dados em horas, minutos e segundos.

temps1 = str(input("Tempo do corredor 1: "))
temps2 = str(input("Tempo do corredor 2: "))
hora1,min1,seg1 = temps1.split(" ")
hora2,min2,seg2 = temps2.split(" ")

hora1 = int(hora1)
min1 = int(min1)
seg1 = int(seg1)

hora2 = int(hora2)
min2 = int(min2)
seg2 = int(seg2)

# Conversão hora em segundos multiplique o valor de tempo por 3600
# Conversão minutos em segundos multiplique o valor de tempo por 60

temp1 = (hora1 * 3600)+(min1*60)+seg1
temp2 = (hora2 * 3600)+(min2*60)+seg2

# Conversão segundos em horas divide o valor de tempo por 3600
# Conversão segundos minutos divide o valor de tempo por 60

if temp1 < temp2:
    dif = temp2 - temp1
    difh = dif // 3600
    difm = (dif % 3600) // 60
    difs = (dif % 3600) % 60
    print("Vencedor: corredor 1")
    print("Diferença: %d horas %d minutos %d segundos" % (difh,difm,difs))
elif temp2 < temp1:
    dif = temp1 - temp2
    difh = dif // 3600
    difm = (dif % 3600) // 60
    difs = (dif % 3600) % 60
    print("Vencedor: corredor 2")
    print("Diferença: %d horas %d minutos %d segundos" % (difh, difm, difs))

