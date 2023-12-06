#nome: Maycon Vinicius
#matricula: 113683
#data: 30/11/2023
#Programa que faz a união de dois conjuntos para criar um agenda sincronizada
def sinc(a1,a2):
    return a1.union(a2)

def main():
    try:
        nomearq = input("Insira o nome do 1° arquivo do contatos e a extensão: ")
        with open(nomearq, 'r')as arq1:

            agenda1 = set()
            linha = arq1.readline().rstrip('\n')
            while linha != '':
                agenda1.add(linha)
                linha = arq1.readline().rstrip('\n')
    except OSError:
        print("Erro ao iniciar o arquivo da agenda 1.")

    try:
        nomearq2 = input("Insira o nome do 2° arquivo de contatos e a extensão: ")
        with open( nomearq2, 'r')as arq2:

            agenda2 = set()
            linha = arq2.readline().rstrip('\n')
            while linha != '':
                agenda2.add(linha)
                linha = arq2.readline().rstrip('\n')
    except OSError:
        print("Erro ao iniciar o arquivo da agenda 2.")
    print("%d número(s) de telefone lido(s) na agenda1" % len(agenda1))
    print("%d número(s) de telefone lido(s) na agenda2" % len(agenda2))
    
    agenda_sinc = sinc(agenda1,agenda2)
    
    print("\nAgenda Sincronizada")
    for telefone in sorted(agenda_sinc):
        print(telefone)
main()
