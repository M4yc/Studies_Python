arquivo = open('entrada.txt','r')

for linha in arquivo.readlines() :
  setinela = linha[0]
  frase = linha[1:-1]
  largura = 80
  if setinela == ';' :
    continue
  elif setinela == '>' :
    print(frase.rjust(largura))
  elif setinela == '<' :
    print(frase.ljust(largura))
  elif setinela == '*' :
    print(frase.center(largura))
  else :
    print(linha, end='')
  #linha = arquivo.readline()
arquivo.close()

# Confirmando o width do rjust()
print()
#for i in range(0,80) :
print('0'*80,end='')