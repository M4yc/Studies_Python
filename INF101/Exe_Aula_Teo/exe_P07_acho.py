def main():
    alunos = leiaAlunos('let374.dat')
    reprov = verifiqueReprovados(alunos)
    #Impressão relatorio
    print("\n *** Alunos Reprovados na Disciplina LET374***\n"
          "Matricula                Nome        Curso       Nota        Faltas")
    for i in range(len(reprov)):
        print(f'%7d    %-25s   %-24s   %1d   %4d' % (reprov[i][0], reprov[i][1], reprov[i][2], reprov[i][3], reprov[i][4]))


def leiaAlunos(nomeArq):
    arq = open(nomeArq, 'r')
    bd = []
    linha  = arq.readline().rstrip('\n')
    while linha != '':
        dados = linha.split(',')