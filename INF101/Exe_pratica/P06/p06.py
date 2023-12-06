# p06.py
# Nome do programador:
# Matrícula:
# Data:
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
        print("{:7d}    {:20s}    {:8.2f}".format(funcionarios[i][0],
                                             funcionarios[i][1],
                                             salariosBrutos[i]))


#####                                             #####
# Implemente aqui a função leiaFunc(nomeArq)          #
#####                                             #####




#####                                             #####
# Implemente aqui a função calcSalBruto(nomeArq, bd)  #
#####                                             #####




if __name__ == "__main__":
    main()
