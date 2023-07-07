#Programa que faz a analise de conceitos da ufv
nota = int(input("Insira sua nota:"))
if 90 <= nota <= 100:
    print("Conceito A")
elif 75 <= nota <= 89:
    print("Conceito B")
elif 60 <= nota <= 74:
    print("Conceito C")
else:
    print("Conceido D")