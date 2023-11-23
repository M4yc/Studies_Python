# p15.py

def sinc(a1, a2):
    # Calcula a diferença simétrica entre os conjuntos a1 e a2
    return a1.symmetric_difference(a2)

def main():
    # Abre o arquivo agenda1.dat, lê os números de telefone e converte para um conjunto
    with open('agenda1.dat', 'r') as file1:
        agenda1 = set(file1.read().split('\n')[:-1])  # Remove a última linha em branco, se houver

    # Abre o arquivo agenda2.dat, lê os números de telefone e converte para um conjunto
    with open('agenda2.dat', 'r') as file2:
        agenda2 = set(file2.read().split('\n')[:-1])  # Remove a última linha em branco, se houver

    # Chama a função sinc para obter a agenda sincronizada
    agenda_sincronizada = sinc(agenda1, agenda2)

    # Imprime o número de telefones lidos em cada agenda
    print(f"{len(agenda1)+1} número(s) de telefone lido(s) na agenda1")
    print(f"{len(agenda2)+1} número(s) de telefone lido(s) na agenda2")

    # Imprime a agenda sincronizada
    print("Agenda Sincronizada")
    for telefone in sorted(agenda_sincronizada):
        print(telefone)

# Chama a função main para iniciar o processo
if __name__ == "__main__":
    main()
