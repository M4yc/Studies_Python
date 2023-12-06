#nome: Maycon Vinicius
#matricula: 113683
#data: 30/11/2023
#Programa que faz a união de dois conjuntos para criar um agenda sincronizada
def sinc(a1,a2):
    return a1.union(a2)

def main():
    with open('agenda1.dat', 'r')as arq1:
        
        agenda1 = set()
        linha = arq1.readline().rstrip('\n')
        while linha != '':
            agenda1.add(linha)
            linha = arq1.readline().rstrip('\n')  

    with open('agenda2.dat', 'r')as arq2:
        
        agenda2 = set()
        linha = arq2.readline().rstrip('\n')
        while linha != '':
            agenda2.add(linha)
            linha = arq2.readline().rstrip('\n')
    print("%d número(s) de telefone lido(s) na agenda1" % len(agenda1))
    print("%d número(s) de telefone lido(s) na agenda2" % len(agenda2))
    
    agenda_sinc = sinc(agenda1,agenda2)
    
    print("\nAgenda Sincronizada")
    for telefone in sorted(agenda_sinc):
        print(telefone)
main()
