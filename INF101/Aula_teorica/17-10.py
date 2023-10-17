#Aula de conjuntos
S={'a', 'b', 'c', 'd'}
S.add('1.2')
S.add((1,2,4))
if (1,2,4) in S:
    print("Sim")
else:
    print("Não")
print(S)