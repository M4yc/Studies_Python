nota = int(input("Nota do aluno (0 a 100): "))

while nota < 0 or nota > 100:
    print("Nota Invalida")
    nota = int(input("Nota do aluno (0 a 100): "))
if nota>=90:
    print("Conceito A")
elif nota>=60:
    print("Conceito B")
elif nota>=60:
    print("Conceito C")
else:
    print("Reprovado")