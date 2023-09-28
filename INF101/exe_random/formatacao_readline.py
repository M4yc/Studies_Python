arquivo = open('entrada.txt','r')
linha = arquivo.readline()
while linha != '' :
  if linha[0] == ';' :
    linha = arquivo.readline()  # lê a próxima linha
    continue
  elif linha[0] == '>' :
    print(linha[1:].rjust(80),end='')
  elif linha[0] == '<' :
    print(linha[1:-1].lstrip().ljust(80))
  elif linha[0] == '*' :
    print(linha[1:].center(80), end='')
  else :
    print(linha[0:-1])
  linha = arquivo.readline()  # lê a próxima linha

arquivo.close()