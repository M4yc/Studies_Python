#Entre 90 e 100 Conceito 'A'
#Entre 75 e 89 Conceito 'B'
#Entre 60 e 74 Conceito 'C'
#Menor que 60 Reprovado

#(60 - 10*0.25)/0.75 = nota necessária para passar nas outras 3 provas

#Explicando a fórmula:

#60 é a nota necessária para passar na matéria
#10 é a nota que você já tirou na primeira prova
#0.25 é o peso da primeira prova (1/4 de 100)
#0.75 é o peso das outras três provas (3/4 de 100)

print('')
print("|        Conceitos           |")
print("| Entre 90 e 100 Conceito 'A'|")
print("| Entre 75 e 89 Conceito 'B' |")
print("| Entre 60 e 74 Conceito 'C' |")
print("| Entre 40 e 59 Prova final. |")
print("| Menor que 40 Reprovado     |")
print('')

nota_p1 = 0
nota_p2 = 0
nota_p3 = 0
nota_p4 = 0

n_provas = int(input("Quantas provas você já fez [1 á 4]: "))
nota_desejada = float(input("Digite a nota mínima desejada para passar na matéria: "))

if n_provas == 1:
    nota_p1 = int(input("Insira o valor da primeira prova: "))
elif n_provas == 2:
    nota_p1 = int(input("Insira o valor da primeira prova: "))
    nota_p2 = int(input("Insira o valor da Segunda prova: "))
elif n_provas == 3:
    nota_p1 = int(input("Insira o valor da primeira prova: "))
    nota_p2 = int(input("Insira o valor da Segunda prova: "))
    nota_p3 = int(input("Insira o valor da Terceira prova: "))
elif n_provas == 4:
    nota_p1 = int(input("Insira o valor da primeira prova: "))
    nota_p2 = int(input("Insira o valor da Segunda prova: "))
    nota_p3 = int(input("Insira o valor da Terceira prova: "))
    nota_p4 = int(input("Insira o valor da Quarta prova: "))

total = (nota_p1+nota_p2+nota_p3+nota_p4) / 4

nota_nece3 = (nota_desejada - nota_p1*0.25)/0.75
nota_nece2 = ((nota_desejada - (nota_p1 + nota_p2))*0.50)/0.50
nota_nece1 = ((nota_desejada - (nota_p1 + nota_p2 + nota_p3))*0.75)/0.25


print("")
print("Não é posivel calcular a mádia ainda você só fez uma prova.")
print("|  P1    = %2.d    |" % nota_p1)
print("|  P2    = %2.d    |" % nota_p2)
print("|  P3    = %2.d    |" % nota_p3)
print("|  P4    = %2.d    |" % nota_p4)
print("|  Total = %2.f    |" % total)
if n_provas == 1:
    print("|  PF    = %2.d    |" % nota_nece3)
elif n_provas == 2:
    print("|  PF    = %2.d    |" % nota_nece2)
elif n_provas == 3:
    print("|  PF    = %2.d    |" % nota_nece3)