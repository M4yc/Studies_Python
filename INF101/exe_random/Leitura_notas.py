def abraArq(nomeArq):
    print()

notas = {}
arq = open("notas.txt", 'r')
linha =arq.readline().rstrip('\n')
while linha != '':
    dados = linha.split('; ')
    matr = int(dados[0])
    nome = str(dados[1])
    idade = int(dados[2])
    p1 = float(dados[3])
    p2 = float(dados[4])
    p3 = float(dados[5])
    notas[matr]= (nome, idade, p1, p2, p3)
    linha = arq.readline().rstrip('\n')
arq.close()