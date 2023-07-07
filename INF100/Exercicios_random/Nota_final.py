#Programa para definir nota final da UFV
#Vc passa se tiver no minimo 75% de presença
#São 16 aulas de INF100 esse semestre
#Deve ter no minimo 12 presenças

nota = float(input("Insira sua nota final:"))
Num_f = int(input("Insira o numero de faltas:"))
if nota >= 0 and nota <= 100:
    if Num_f > 4:
        print("Você foi reprovado por falta.")
    else:
        if nota >= 60:
            print("Aprovado")
        else:
            if nota >= 40:
                print("Deve fazer a prova final.")
            else:
                print("Reprovado direto.")
else:
    print("Nota invalida!")
