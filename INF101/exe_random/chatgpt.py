import os

def abraArq():
    notas = {}
    arq = open("notas.txt", 'r')
    arq.readline()

    linha = arq.readline().rstrip('\n')
    while linha != '':
        dados = linha.split('; ')
        matr = int(dados[0])
        nome = str(dados[1])
        idade = int(dados[2])
        p1 = float(dados[3])
        p2 = float(dados[4])
        p3 = float(dados[5])
        notas[matr] = (nome, idade, p1, p2, p3)
        linha = arq.readline().rstrip('\n')
    arq.close()

    return notas

def pesqNota(mat_input, notas):
    if mat_input in notas:
        nome, idade, p1, p2, p3, notaf = notas[mat_input]
        print(f"Matrícula: {mat_input}")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Nota P1: {p1}")
        print(f"Nota P2: {p2}")
        print(f"Nota P3: {p3}")
        print(f"Nota Final: {notaf}")
        if notaf < 40:
            print("Situação: Reprovado Direto")
        elif notaf < 60:
            print("Situação: Reprovado")
        else:
            print("Situação: Aprovado")
    else:
        print("Matrícula não encontrada")

# Limpar a tela antes de começar
os.system('cls' if os.name == 'nt' else 'clear')

notas = abraArq()

while True:
    mat_input = input("Informe a matrícula (ou digite 0 para sair): ")
    if mat_input == '0':
        break
    else:
        try:
            mat_input = int(mat_input)
            pesqNota(mat_input, notas)
            print("\n")
        except ValueError:
            print("Matrícula inválida. Digite um número válido.")
