# p06.py
# Nome do programador: Maycon Vinicius
# Matrícula: 113683
# Data: 28/09/2023
# Faz um relatório dos salários brutos auferidos pelos funcionários de
# uma empresa. Os registros dos funcionários são lidos do arquivo
# 'funcionarios.csv' e as horas trabalhadas, do arquivo 'horas_trab.dat'.


def main():
    nomeArq = "funcionarios.csv"
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
def leiaFunc(nomeArq):
    arq = open(nomeArq ,"r")
    lista=[]
    linha = arq.readline().rstrip('\n')
    while linha != '':
        dados = linha.split(',')
        matri = int(dados[0])
        nome = str(dados[1])
        cargo = str(dados[2])
        salario = float(dados[3])
        lista.append((matri, nome, cargo, salario))
        linha = arq.readline().rstrip('\n')
        
    arq.close()    
    return lista
        
        
#####                                             #####





#####                                             #####
# Implemente aqui a função calcSalBruto(nomeArq, bd)  #
def calcSalBruto(nomeArq, bd):
    arq = open("horas_trab.dat" ,"r")
    listah=[]
    lista_sal=[]
    linha = arq.readline().rstrip('\n')
    while linha != '':
        dados = linha.split(" ")
        horas = int(dados[0])
        horas_ex = float(dados[1])
        listah.append((horas,horas_ex))
        linha = arq.readline().rstrip('\n')
    arq.close()
    for i in range(len(bd)):
        calculo = (bd[i][3]*listah[i][0])+((bd[i][3]*1.5)*listah[i][1])
        lista_sal.append(calculo)
            
    
    return lista_sal
        
    
    
#####                                             #####




if __name__ == "__main__":
    main()
