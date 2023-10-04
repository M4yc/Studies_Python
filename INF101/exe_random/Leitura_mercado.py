def abrirArq1():
    lista = {}
    with open("mercado.txt", "r") as arq:
        arq.readline()  # Pule a primeira linha do arquivo

        for linha in arq:
            dados = linha.rstrip('\n').split('; ')
            produto = str(dados[0])
            qnt = int(dados[1])
            mod = str(dados[2])
            lista[produto] = [qnt, mod]

    return lista

def abrirArq2():
    precos = {}
    with open("precoEstoque.txt", "r") as arq:
        arq.readline()  # Pule a primeira linha do arquivo

        for linha in arq:
            dados = linha.rstrip('\n').split('; ')
            produto = str(dados[0])
            qnt = int(dados[1])
            mod = str(dados[2])
            price = float(dados[3])
            precos[produto] = [qnt, mod, price]

    return precos

estoque = abrirArq1()
preco = abrirArq2()

extrato = {}

for produto_lista, (qnt_lista, mod_lista) in estoque.items():
    for produto_estoque, (qnt_estoque, mod_estoque, price) in preco.items():
        extrato[produto_estoque] = (qnt_lista, mod_estoque, (price * qnt_lista))

pd_desj = 'Fosforo'
try:
    qnt, mod, valor = extrato[pd_desj]
    print(f'Produto: {pd_desj:12s}     Quantidade: {qnt}     Valor: R$ {valor:.2f}')
except KeyError:
    print(f'Produto: "{pd_desj}" não encontrado no extrato.')
