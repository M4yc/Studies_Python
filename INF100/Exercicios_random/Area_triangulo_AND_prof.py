# autores: Carlos Goulart e turma teórica 2
# Data: 12/04/2023

# mensagem para informar o que o programa faz
print('Este programa calcula a áres de um triângulo de lados a, b, c')
# ler os valores dos lados do triângulo
a = float (input('a = '))
b = float (input('b = '))
c = float (input('c = '))

if a < b+c and b < a+c and c < a+b :
    # calcular o valor de p
    p = (a + b + c) / 2

    # calcular o valor da área
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    # exibir o resultado
    print('A área do triângulo é = ', area)
else:
    print('Com os lados fornecidos não é possível formar um triângulo')