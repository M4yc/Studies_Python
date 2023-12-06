# p09.py
# Programador: Maycon Vinicius
# Matrícula: 113683
# Data de criação: 09/11/2023
# Data de atualização: 09/11/2023
# Produz um horário escolar usando uma heurística muito simples baseada
# na estrutura de dados conjunto. Os dados de entrada são as disciplinas
# a ser oferecidas e as matrículas dos alunos que farão algumas das
# disciplinas oferecidas.

import sys

def main():
    # Define os nomes dos arquivos de entrada; usa os defaults, se não houver
    # argumentos com os nomes na linha de comando.
    nomeArqDisc = 'disciplinas2.txt'
    nomeArqMatric = 'matriculas2.txt'
    if len(sys.argv) > 1:
        nomeArqDisc = sys.argv[1]
    if len(sys.argv) > 2:
        nomeArqMatric = sys.argv[2]
    
    discs = leia_arq_disciplinas(nomeArqDisc)
    matrics = leia_arq_matriculas(nomeArqMatric)

    hor = faz_horario_escolar(discs, matrics)
    # Imprime as sessões não conflitantes do horário.
    print('\nSessões:')
    for i in range(len(hor)):
        print('{:3d}: '.format(i), sorted(hor[i]))


# Lê uma disciplina por linha do arquivo cujo nome externo é 'nomearq'.
# Retorna a lista de disciplinas lidas.
####                                                                 ####
# COLOQUE AQUI A IMPLEMENTAÇÃO DA FUNÇÃO: leia_arq_disciplinas(nomearq) #
####                                                                 ####

def leia_arq_disciplinas(nomearq):
    arq = open(nomearq, 'r')
    listamat = []
    linha = arq.readline().rstrip('\n')
    while linha != '':
        dados = linha
        mat = dados
        listamat.append((mat))
        linha = arq.readline().rstrip('\n')

    arq.close()
    
    return listamat

# Lê, por linha, o nome de um aluno e as disciplinas em que ele se matriculou.
# Os dados em cada linha são separados por uma vírgula. O nome externo do
# arquivo é passado como parâmetro. Retorna um dicionário em que a chave é o
# nome de um aluno e o valor associado é o conjunto de disciplinas em que o
# aluno se matriculou.
####                                                                 ####
# COLOQUE AQUI A IMPLEMENTAÇÃO DA FUNÇÃO: leia_arq_matriculas(nomearq)  #
####                                                                 ####
def leia_arq_matriculas(nomearq):
    arq = open(nomearq, 'r')
    dicMate = {}
    linha = arq.readline().rstrip('\n')
    while linha != '':
        dados = linha.split(',')
        matri = str(dados[0])
        disci = set(dados[1:])
        dicMate[matri] = disci
        linha = arq.readline().rstrip('\n')
    arq.close()
    
    
    
    return dicMate

####                                                                    ####
# COLOQUE AQUI A IMPLEMENTAÇÃO DA FUNÇÃO: faz_horario_escolar(disciplinas, #
#                                                             matriculas)  #
####                                                                    ####

def faz_horario_escolar(disciplinas,matriculas):
    emptySet = set() # conjunto vazio
    
    conflitos = [ emptySet for d in disciplinas ]
    for a in matriculas.keys():
        for d in range(len(disciplinas)):
            if disciplinas[d] in matriculas[a]:
                conflitos[d] = conflitos[d].union(matriculas[a])
    
    restantes = set(disciplinas)
    horario = []
    while restantes != emptySet:
        i = 0
        d = disciplinas[i]
        while d not in restantes:
            i = i + 1
            d = disciplinas[i]
        sessao = { d }
        tentativa = restantes.difference(conflitos[i])
        for s in range(len(disciplinas)):
            if disciplinas[s] in tentativa:
                if conflitos[s].isdisjoint(sessao):
                    sessao.add(disciplinas[s])
        restantes = restantes.difference(sessao)

        horario.append(sessao)
    

    return horario

if __name__ == '__main__':
    main()
