import numpy as np
#dimensões de A
m = int(input('Informe o numero de linhas da matriz A:'))
n = int(input('Informe o numero de colunas da matriz A:'))

#dimensões de B
o = int(input('Informe o numero de linhas da matriz B:'))
p = int(input('Informe o numero de colunas da matriz B:'))

if n!=o:
    print('Não é possivel fazer o produto de matrizes com as dimensões informadas!')
else:
    A = np.empty((m,n))
    B = np.empty((o, p))
    C = np.empty((m, n))

    for i in range(m):
        for j in range(n):
            A[i][j]=np.random.randint(0,100)

    for i in range(o):
        for j in range(p):
            B[i][j]=np.random.randint(0,100)


