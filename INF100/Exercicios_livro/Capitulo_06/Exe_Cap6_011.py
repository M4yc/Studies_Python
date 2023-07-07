# Escreva um programa para ler 2 notas de um aluno, calcular e imprimir a média final.
#Logo após escrever a mensagem "Calcular a média de outro aluno [S]im [N]ao?" e
#solicitar uma resposta. Se a resposta for “S” ou “s”, o programa deve ser executado
#novamente, caso contrário deve ser encerrado imprimindo a quantidade de alunos
#aprovados, reprovados e que ficaram em exame final, considerando o mesmo
#critério adotado pela UFV, conforme tabela mostrada a seguir.

#as notas finais na UFV são sempre valores inteiros, com arredondamento para
#cima se o valor decimal for maior ou igual a 0,5 e arredondamento para baixo, caso
#contrário. Ex: 59.4 vira 59 e 59.5 vira 60.
aprovados = 0
reprovados = 0
final = 0

while True:
    nota1 = float(input("Informe a 1° nota: "))
    nota2 = float(input("Informe a 2° nota: "))
    media = round((nota1 + nota2) / 2)

    if media >= 60 and media <= 100:
        print("Aprovado")
        aprovados += 1
    elif media >= 40 and media <= 59:
        print("Exame Final")
        final += 1
    elif media >= 0 and media <= 39:
        print("Reprovado")
        reprovados += 1

    resposta = str(input("Calcular a média de outro aluno [S]im [N]ão? "))
    if resposta == 'N' or resposta =='n':
        break

print('')
print("Numero de Alunos aprovados: %d " % aprovados)
print("Numero de Alunos para o exame final: %d " % final)
print("Numero de Alunos reprovados: %d " % reprovados)
