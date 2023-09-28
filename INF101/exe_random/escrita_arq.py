# Abre um arquivo em modo de escrita, e em cada linha são escritos dois números,
# um número inteiro e outro float.

arq = open('dados.txt','w')
for linha in range(1,11):
  valor0 = linha
  valor1 = (linha * 5) / 2
  arq.write( '{} {}\n'.format(valor0, valor1) )
arq.close()