import numpy as np

m = int(input('Informe o tamanho da matriz quadrada: '))

A = np.random.randint(0,9,(m,m))
#função randint precisa de: menor valor, maior valor e o tamannho da matriz

print(A)
p =1

for i in range(m):
     p = p * A[i][i]
print('\nProduto dos elementos da diagonal principal = %1.f'%p)

p = 1
for i in range(m):
     p = p * A[i][m-1-i]
print('Produto dos elementos da diagonal secundaria = %1.f'%p)

soma=0
for i in range(0,m):
    for j in range(0,m):
        soma+=A[i][j]
media = soma/(m*m)
print('Media dos elementos da matriz: %1.f'%media)

baixo = 0
for i in range(0,m):
    for j in range(0,m):
        if A[i][j] <  media: baixo += 1

print("Nº de elementos abaixo da media:",baixo)