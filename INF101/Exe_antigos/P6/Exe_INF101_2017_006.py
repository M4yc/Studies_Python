#s elaborar um programa que gere uma listagem dos salários brutos mensais de
#todos os funcionários da empresa, dado o número de horas trabalhadas no mês de cada
#funcionário.

def leiaFunc():
    func = () #funcionarios

    numero = int(input("Entre com o nº de matrícula de um(a) funcionário(a) (nº < 0 p/ terminar):"))
    if numero <= 0:
        return func
    else:
        nome = str(input("Digite o nome do(a) funcionário(a): "))
        cargo = str(input("Digite o cargo dele(a): "))
        salario = float(input("Digite o salário por hora dele(a): "))

        func = (numero,nome,cargo,salario)

        return func

def calcSalBruto(func, nht):
    salariotot = func[3] * nht

    return salariotot
def main():
    listfunc = []
    t = leiaFunc()

    while t != ():
        listfunc.append(t)
        t = leiaFunc()

    lsb = [] #lista de salario Bruto

    cont = 1

    for i in range(0,len(listfunc)):

        nht = float(input('\nDigite o número de horas trabalhadas do(a) %d° funcionário(a): ' % cont ))
        sbf = calcSalBruto(listfunc[i], nht)
        lsb.append(sbf)
        cont += 1

    print('\n***     Relatorio dos Salários Brutos     ***')
    print('Matrícula         Nome          Salário Bruto')
    for j in range(0, len(listfunc)):
        print('%7d   %-15s   %8.2f' % (listfunc[j][0], listfunc[j][1], lsb[i]))

main()
