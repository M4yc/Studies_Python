#Programa que mostra a saida de valores em uma nota de posto
nome = 'Jair Silva'#input('Informe o nome:')
sexo = "M"#input('Informe seu sexo:')
idade = 40#int(input('Informe a idade:'))
prod = 'Gasolina Aditivada'#input('Informe o tipo de combustivel:')
preco = 5#float(input('Informe o preço do produto:'))
qtd = 29.7#float(input('Informe a quantidade do produto:'))
print('=-'*30)
print('Nome: %s ' % nome,end='')
print('Sexo: %s Idade: %d' %(sexo,idade))
print()
print('Produto                Valor       Qtd        Total',end='\n')
print('%-15s %9.2f %9.1f %12.2f' %(prod, preco, qtd, qtd*preco))
print('=-'*30)