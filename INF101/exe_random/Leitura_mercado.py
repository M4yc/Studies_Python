def abrirArq1():
    estoque = {}
    arq = open("mercado.txt", "r")
    arq.readline()
    #with open("mercado.txt", "r") as arquivo:

    linha = arq.readline().rstrip('\n')
    while linha != '':
        dados = linha.split('; ')
        produto = str(dados[0])
        qnt = int(dados[1])
        mod = str(dados[2])
        estoque[produto]=[qnt, mod]
        linha = arq.readline().rstrip('\n')

    arq.close()

    return  estoque


def abrirArq2():
    precos = {}
    arq = open("preco.txt", "r")
    arq.readline()
    # with open("mercado.txt", "r") as arquivo:

    linha = arq.readline().rstrip('\n')
    while linha != '':
        dados = linha.split('; ')
        produto = str(dados[0])
        qnt = int(dados[1])
        mod = str(dados[2])
        price = float(dados[3])
        precos[produto] = [qnt, mod, price]
        linha = arq.readline().rstrip('\n')

    arq.close()

    return precos

estoque  = abrirArq1()

preco = abrirArq2()

extrato = {}

for produto1, (qnt1,mod1) in estoque.items():
    for produto2, (qnt2, mod2,price) in preco.items():
        extrato[produto1] = (qnt2, mod2,price*qnt1)

print(extrato)