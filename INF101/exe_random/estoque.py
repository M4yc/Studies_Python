estoque = { 'Tomate' : [1000, 2.30],
            'Cenoura' : [500, 1.50],
            'Batata': [1500, 1.30],
            'Couve' : [300, 1.00],
            'Feijao' : [500, 6.00]}

vendas = [('Tomate', 5), ('Batata', 100), ('Cenoura', 40), ('Couve', 20), ('Feijao', 80)]

for item, (qnt,preco) in estoque.items():
    for venda_item, venda_qnt in vendas:
        if item == venda_item:
            estoque[item][0] -= venda_qnt

with open('EstoqueMercado.txt', 'w') as arquivo:
    arquivo.write("***       Estoque do Supermercado       ***\n")
    arquivo.write("Produto         Quantidade          Preço\n")
    for item, (qnt, preco) in estoque.items():
        arquivo.write(f"{item:12s}       {qnt:4d}             R$ {preco:.2f} \n")

