#programa de conceito das notas
nota = int(input('Insira sua nota: '))
if nota >= 90:
    print('Conceito A')
elif nota >= 75 and nota <= 89 :
    print('Conceito B')
elif nota >= 60 and nota <= 74 :
    print('Conceito C ')
elif nota < 60:
    print('Reprovado')