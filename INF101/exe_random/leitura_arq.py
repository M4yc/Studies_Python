# Lê um arquivo linha por linha; cada linha contém dois dados separados por um
# espaço em branco: um número inteiro e outro float; depois insere os dados em
# uma lista de 2-tuplas.

arq = open('dados.txt', 'r')
lista = []
linha = arq.readline().rstrip('\n')
while linha != '' :
  dados = linha.split(' ')
  v0 = int(dados[0])
  v1 = float(dados[1])
  lista.append( (v0, v1) )
  linha = arq.readline().rstrip('\n')
arq.close()

print(lista)