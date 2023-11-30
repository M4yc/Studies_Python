
def sinc(a1,a2):
    return a1.symmetric_difference(a2)
def main():
    print()
    with open('agenda1.dat', 'r') as arq1:

        agenda1 = set()
        linha = arq1.readline().rstrip('\n')
        while linha != '':
            agenda1.add(linha)
            linha = arq1.readline().rstrip('\n')


    with open('agenda2.dat', 'r') as arq2:
        agenda2 = set()
        linha = arq2.readline().rstrip('\n')
        while linha != '':
            agenda2.add(linha)
            linha = arq2.readline().rstrip('\n')

    agenda_sin = sinc(agenda1,agenda2)
    print("%d número(s) de telefone lido(s) na agenda1"%len(agenda1))
    print("%d número(s) de telefone lido(s) na agenda2" % len(agenda2))

    print("Agenda Sincronizada")
    for telefone in sorted(agenda_sin):
        print(telefone)

main()