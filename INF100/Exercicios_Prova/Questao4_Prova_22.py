cod = str(input("Informe o codigo da disciplina: "))
n = int(input("Informe o numero de alunos matriculados: "))

if n <= 30:
    print("")
    print("Por favor, use a sua sala de aula!")
elif n >= 1000:
    print("")
    print("A reserva devera ser feita pessoalmente.")
else:

   num_sala90 = n // 90
   num_sala60 = (n % 90) // 60
   num_sala30 = (n -(num_sala60 * 60)-(num_sala90 * 90)) // 30

   if (n -(num_sala60 * 60)-(num_sala90 * 90)) % 30 != 0:
      num_sala30 += 1

   num_vagas = num_sala90 * 90 + num_sala60 * 60 + num_sala30 * 30
   num_salas = num_sala30 + num_sala60 + num_sala90
   print('')
   print("%d sala(s) reservadas para %s" % (num_salas, cod))
   print("%d sala(s) de 90 lugares." % num_sala90)
   print("%d sala(s) de 60 lugares." % num_sala60)
   print("%d sala(s) de 30 lugares." % num_sala30)
   print("Total de %d lugares para %d alunos."%(num_vagas,n))