# p07.py
# Programador: Maycon Vinicius Batista Araujo
# Matrícula: 113683
# Data: 05/10/2023
# Atualiza um estoque de acordo com as vendas do dia; calcula o valor das
# vendas do dia e grava, em novo arquivo, o estoque atualizado.

def main():
    estoque = leiaEstoque('estoque.txt')
    

    vendas = leiaVendas('vendas.txt')
    
    
    processeVendas(estoque, vendas)
    
    
    nomearq = input('\nEntre com o nome do arquivo para conter o estoque '
                    'atualizado: ')
    salveEstoqueAtualizado(nomearq, estoque)


#####                                                              #####
# Implemente aqui as funções que faltam.                               #
#####                                                              #####
def leiaEstoque(nomeArq):
    with open(nomeArq, 'r') as arq:
        listaE = {}
        linha = arq.readline().rstrip('\n')
        while linha != '':
            dados = linha.split(',')
            pro = str(dados[0])
            qnt = int(dados[1])
            price = float(dados[2])
            listaE[pro]= [qnt, price]
            linha = arq.readline().rstrip('\n')
            
    return listaE

def leiaVendas(nomeArq):
    with open(nomeArq, 'r') as arq:
        listaV = []
        nlinha = 0
        linha = arq.readline().rstrip('\n')
        while linha != '':
            nlinha += 1
            dados = linha.split(',')
            v0 = str(dados[0])
            v1 = float(dados[1])
            listaV.append((v0, v1))
            linha = arq.readline().rstrip('\n')
    print("%s linhas lidas do arquivo %s \n"%(nlinha,nomeArq))
    return listaV

def processeVendas(estoque, vendas):
    print("                     *****Vendas Realizadas*****                       \n")
    print("Produto           Quantidade   Preço por Unid.         Valor da Venda")
    print("---------------------------------------------------------------------")
    total = 0
    
    for op in vendas:
        produto,qnt = op
        if [produto][0] in estoque:
            estoque[produto][0] -= qnt
            price = estoque[produto][1]
            valor = price*qnt
            total += valor
            print('%12s        %3.2f        %6.2f                %6.2f' %(produto,qnt,price,valor))
        else:
            print("%12s      *** não há estoque ***                  " % produto)
            
    print("---------------------------------------------------------------------")
    print("TOTAL:                                                %.2f" % total)
    print("")
        
    
    
def salveEstoqueAtualizado(nomearq, estoque):
    with open(nomeArq, 'w') as arq:
        print()


if __name__ == '__main__':
    main()
