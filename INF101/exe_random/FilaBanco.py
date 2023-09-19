nome=["João", "Maria", "Pedro", "José", "Antonio", "Ana"]
fila = [1, 2, 3, 4, 5, 6]
nomes = [(1,"João"), (2,"Maria"), (3,"Pedro"), (4,"José"), (5,"Antonio"), (6,"Ana")]

#print(f"Fila do banco está com {len(nome)} pessoas na fila.")
def menu():
    print('-------------------------------------------------------')
    print(f"Fila do banco está com {len(nome)} pessoas na fila.")
    print("| A | para adicionar um cliente ao fim da fila.")
    print("| C | para começar o atendimento.")
    print("| S | para finalizar.")
    print("| M | para mostrar a fila.")
    print('-------------------------------------------------------')
cont = 0
while True:
    menu()
    operacao = str(input("Digite o que deseja fazer:").upper())
    print('')
    if operacao == "A":
        #fila.append(len(fila)+1)
        in_nome = input("Digite o nome da pessoa que deseja inserir no final da fila:")
        nome.append(in_nome)
    elif operacao == "C":
        if len(nome) > 0:
            nome_proc = nome[0]
            print(f"O Cliente {nome[0]} foi atendido com sucesso ele era o numero {nome.index(nome_proc)+1}° da fila.")
            nome.pop(0)
            cont += 1
        else:
            print("Fila Vazia todos já foram atendidos.")
    elif operacao == "S":
        break
    elif operacao == "M":
        print("Fila Agora:")
        print(nome)
        print('')
    else:
        print("Opção invalida! Digite apenas A,C ou S.")

print(f"{cont} Clientes atendidos hoje.")