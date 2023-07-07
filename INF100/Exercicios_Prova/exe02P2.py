
cont = 0
soma = 0
while True:
    preco = float(input('Preço Sabonete (<= 0 p/ fim): '))
    if preco <= 0:
        break
    soma = soma + preco
    cont += 1
if cont > 0:
    print('O preço médio do Sabonete é: %.2f'%(soma/cont))
else:
    print('Nenhum valor foi fornecido!')