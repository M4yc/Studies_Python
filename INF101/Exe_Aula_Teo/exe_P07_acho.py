def main():
    alunos = leiaAlunos('let374.dat')
    reprov = verifiqueReprovados(alunos)
    #Impressão relatorio
    print("\n *** Alunos Reprovados na Disciplina LET374***\n"
          "Matricula                Nome        Curso       Nota        Faltas")
    for i in range(len(reprov)):
        print(f'%7d    %-25s   %-24s   %1d   %4d' % (reprov[i][0], reprov[i][1], reprov[i][2], reprov[i][3], reprov[i][4]))


def leiaAlunos(nomeArq):
    bd = []
    with open(nomeArq, 'r') as arq:
    #arq = open(nomeArq, 'r')
        linha = arq.readline().rstrip('\n')
        while linha != '':
            dados = linha.split(',')
            matr= int(dados[0])
            nome = dados[1]
            curso = dados[2]
            nota = int(dados[3])
            faltas = int(dados[4])
            bd.append((matr, nome, curso, nota, faltas))
            linha = arq.readline().rstrip('\n')
    #arq.close()

    return  bd

def verifiqueReprovados(bd):
    ar = []
    for i in range(len(bd)):
        if bd[i][3] < 60 or bd[i][4] > 15:
            ar.append(bd[i])

    return ar

main()