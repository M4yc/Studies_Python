def abraArq(nomeArq):
    print()

notas = {}
arq = open("notas.txt", 'r')
arq.readline()

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

notaf = 0

for matricula, (nome, idade, p1, p2, p3) in notas.items():
    notaf = p1 + p2 + p3
    notas[matricula] = (nome, idade, p1, p2, p3,notaf)

print(f"Nome:{notas[113683][0]} Nota P1= {notas[113683][2]} Nota P2= {notas[113683][3]} Nota P3= {notas[113683][4]} Nota Final= {notas[113683][5]}")