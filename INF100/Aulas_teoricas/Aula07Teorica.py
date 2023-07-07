import numpy as np

n = int(input("Informe o numero de alunos: "))
print('Entre com a nota de cada aluno (uma em cada linha):')
notas = np.empty(n)
soma = 0
menor = 1000
maior = -1
for i in range(0,n):
    x = float(input("Informe a %d° nota: "%(i+1)))
    notas[i] = x
    soma += x
    if x < menor:
        menor = x
    if x > maior:
        maior = x
media = soma / n

soma = 0
for i in range(0,n):
    soma += (notas[i]-media)**2
desvio = (soma/n)**0.5

print('\nMedia das notas: %.2f' % media)
print('Desvio padrão: %.2f' % desvio)
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')

n_menor = 0
for i in range(0,n):
    if notas[i]<media:
        n_menor += 1
print(f'Notas menores que a média: {n_menor}')