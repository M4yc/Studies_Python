# Leitura do código da disciplina
codigo = input("Digite o código da disciplina: ")

# Leitura do número de estudantes matriculados
num_estudantes = int(input("Digite o número de estudantes matriculados: "))

# Verificação do número de salas necessárias
if num_estudantes <= 30:
    print("Reserva em uma sala de aula")
elif num_estudantes > 1000:
    print("A reserva deve ser feita pessoalmente")
else:
    num_salas_90 = num_estudantes // 90
    num_salas_60 = (num_estudantes % 90) // 60
    num_salas_30 = (num_estudantes % 90 % 60) // 30
    total_salas = num_salas_90 + num_salas_60 + num_salas_30
    total_lugares = num_salas_90 * 90 + num_salas_60 * 60 + num_salas_30 * 30

    print("%d sala(s) reservadas para %s" % (total_salas, num_estudantes))
    print("%d sala(s) de 90 lugares." % num_salas_90)
    print("%d sala(s) de 60 lugares." % num_salas_60)
    print("%d sala(s) de 30 lugares." % num_salas_30)
    print("Total de %d lugares para %d" % (total_lugares, num_estudantes))
