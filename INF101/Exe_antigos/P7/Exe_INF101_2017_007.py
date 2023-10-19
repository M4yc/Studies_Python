# Faz um relatório dos salários brutos auferidos pelos funcionários de
# uma empresa. Os registros dos funcionários são lidos do arquivo
# 'funcionarios.csv' e as horas trabalhadas, do arquivo 'horas_trab.dat'.

def main():
    funcionarios = leiaFunc('funcionarios.csv')
    salariosBrutos = calcSalBruto('horas_trab.dat', funcionarios)

    # Imprime relatório dos salários brutos de todos os funcionários.
    print("\n***     Relatório dos Salários Brutos     ***"
          "\nMatrícula         Nome          Salário Bruto")
    for i in range(len(funcionarios)):
        print("%7d    %-20s    %8.2f" % (funcionarios[i][0],
                                         funcionarios[i][1],
                                         salariosBrutos[i]))

def leiaFunc(nomeArq):
    # Abre o arquivo no formato csv contendo os dados dos funcionários:
    # matr,nome,cargo,salPorHora
    arqFuncs = open(nomeArq, 'r')

    # Gera o banco de dados dos funcionarios armazenando-o em uma lista
    # de tuplas.
    bd = []
    linha = arqFuncs.readline().rstrip('\n')
    while linha != '':
        dados = linha.split(',')
        #print(dados)
        matr = int(dados[0])
        nome = dados[1]
        cargo = dados[2]
        salPorHora = float(dados[3])
        bd.append((matr, nome, cargo, salPorHora))
        linha = arqFuncs.readline().rstrip('\n')
    arqFuncs.close()

    return bd

###
# Implemente aqui a função calcSalBruto(nomeArq, bd)
def calcSalBruto(nomeArq, bd):

    arq = open(nomeArq, 'r')

    bdt = []
    linha = arq.readline().rstrip('\n')
    i = 0
    while linha != '':
        dados = linha.split(' ')
        ht = float(dados[0])
        he = float(dados[1])

        salarioh = ht * (bd[i][3])
        salarioe = he * ((1.5)*(bd[i][3]))
        salariotot = salarioe+salarioh

        bdt.append((salariotot))
        i += 1
        linha = arq.readline().rstrip('\n')
    arq.close()

    return bdt


###


main()
