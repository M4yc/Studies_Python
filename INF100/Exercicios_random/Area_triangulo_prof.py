# autores: Carlos Goulart e turma teórica 2
# Data: 12/04/2023

# mensagem para informar o que o programa faz
print('Este programa calcula a áres de um triângulo de lados a, b, c')
# ler os valores dos lados do triângulo
a = float (input('a = '))
b = float (input('b = '))
c = float (input('c = '))

if a < b+c : # testa se o lado a é menor que a soma dos outros dois lados
    if b < a+c : # testa se o lado b é menor que a soma dos outros dois lados
        if c < a+b : # testa se o lado c é menor que a soma dos outros dois lados
            # calcular o valor de p
            p = (a + b + c) / 2

            # calcular o valor da área
            area = (p*(p-a)*(p-b)*(p-c))**0.5
            # exibir o resultado
            print('A área do triângulo é = ', area)
        else: # lado c é maior que a soma dos outros dois
            print('Com os lados fornecidos não é possível formar um triângulo')
    else: # lado b é maior que a soma dos outros dois
        print('Com os lados fornecidos não é possível formar um triângulo')
else: # lado a é maior que a soma dos outros dois
    print('Com os lados fornecidos não é possível formar um triângulo')