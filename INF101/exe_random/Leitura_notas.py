def abraArq():
    notas = {}
    arq = open("notas.txt", 'r')
    arq.readline()

    linha =arq.readline().rstrip('\n')
    while linha != '':
        dados = linha.split('; ')
        matr = int(dados[0])
        nome = str(dados[1])
        idade = int(dados[2])
        p1 = float(dados[3])
        p2 = float(dados[4])
        p3 = float(dados[5])
        notas[matr]= (nome, idade, p1, p2, p3)
        linha = arq.readline().rstrip('\n')
    arq.close()

    return notas

notas = abraArq()

notaf = 0
for matricula, (nome, idade, p1, p2, p3) in notas.items():
    notaf = p1 + p2 + p3
    notas[matricula] = (nome, idade, p1, p2, p3,notaf)

def pesqNota(mat_input,notas):

    mat_input= int(mat_input)
    if mat_input in notas:
        nome, idade, p1, p2, p3, notaf = notas[mat_input]
        print(f"Nome: {notas[mat_input][0]}")
        print(f"Nota P1: {p1}")
        print(f"Nota P2: {p2}")
        print(f"Nota P3: {p3}")
        print(f"Nota Final: {notaf}")
        if notaf < 60:
            print("Reprovou")
        elif notaf < 40:
            print("Reprovado direto")
        elif notaf > 60:
            print("Passou")
    else:
        print("Matricula não encontrada")

def main():
    mat_input = input("Iforme a matricula: ")

    pesqNota(mat_input, notas)

main()

