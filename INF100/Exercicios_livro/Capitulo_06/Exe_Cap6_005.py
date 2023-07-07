# Escreva um programa para ler o número de alunos existentes em uma turma, ler a
# nota de cada aluno e calcular a média aritmética da turma.
soma = 0
nota = 0
i = 0
n_aluno = int(input("Informe o numero de alunos: "))

while i != n_aluno:
    nota = float(input("Infome a nota dos alunos: "))
    soma += nota
    i += 1
media = soma / n_aluno
print("A média das notas foi de: %.2f " % media)