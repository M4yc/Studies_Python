
# autores: Carlos Goulart e turma teórica 2
# Data: 12/04/2023

# mensagem para informar o que o programa faz
print('Este programa calcula raizes de uma equação do segundo grau')
print('ax² + bx + c = 0')
# ler os coeficientes da equação
a = float (input('a = '))
b = float (input('b = '))
c = float (input('c = '))
delta = b**2 - 4*a*c     #cálculo do delta antes do comando condicional
# verifica se a é diferente de zero
if a == 0 :  # caso que não é equação do 2o. grau
    print('Com coeficiente a = 0, não é equação do 2⁰ grau')
elif delta < 0 :  # caso que não possui raízes reais
    print('A equação não possui raízes reais')
elif delta == 0 : # caso que tem 2 raízes iguais
    r1 =  -b / (2*a)
    if r1 == -0.0 :
        r1 =-r1
    print("2 raízes iguais a", r1)
else  :  # delta > 0 -> # caso que tem duas raízes reais e diferentes
    # calcular o valor de r1
    r1 = ( -b + delta**0.5 ) / (2*a)
    # calcular o valor de r2
    r2 = ( -b - delta**0.5 ) / (2*a)
    # exibir o resultado
    print('As raízes são: ', r1, r2)
