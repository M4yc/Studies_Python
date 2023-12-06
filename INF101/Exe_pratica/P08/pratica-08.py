#nome: Maycon Vinicius
#matricula: 113683
#data:19/10/2023

#Controle de estoque por dicionario e imprimindo em ordem alfabetica 

def main():
    estoque = { 'tomate': [1000, 2.30],
            'alface': [500, 0.45],
            'batata': [2150, 1.20],
            'feijão': [100, 5.50] }
    
    estoque['cebola'] = [500, 1.15] 
    print("\n       Estoque da Quitanda")
    print("\nProduto      Preço    Quantidade")
    
    #print(estoque.keys())
        
    for operacao in estoque:
        produto = operacao
        preco = estoque[produto][1]
        quantidade = estoque[produto][0]
        print("%s %11.2f %12d" % (produto, preco, quantidade))

    valor_total = calculaValorTotal(estoque)
    
    print("\nValor total do estoque: %12.2f" % valor_total)
def calculaValorTotal(estoque):
    total = 0
    vtotalP = 0
    for operacao in estoque:
        produto = operacao
        preco = estoque[produto][1]
        quantidade = estoque[produto][0]
        vtotalP = (preco * quantidade)
        total += vtotalP

    return total

main()
