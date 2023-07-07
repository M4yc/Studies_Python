#Nome: Maycon Vinicius Batista Araujo
#Matrícula: 113683
#Data: 04/06/2023
# A pratica de hoje é um jogo da velha simplificado em python

import auxiliar as aux

# jogo da velha
l = 3 # número de linhas
c = 3 # número de colunas

#inicio do jogo
print('Novo jogo')
# cria e preenche o tabuleiro vazio - todas as posições terão o caractere -
Tab = aux.inicializaTabuleiro(l, c)

# imprime o tabuleiro inicial
aux.imprimeTabuleiro(Tab)

# jogador = 1 e marca = 'X' (Jogador 1 é o primeiro a jogar, com marca 'X')
marca, jogador = aux.inicializaJogo()

num_jogadas = 0       # sem jogadas (marcações)
alguem_venceu = False # jogo sem ganhador

#### não modifique as linhas de código ACIMA desta linha

while num_jogadas < 9 and not alguem_venceu:
    print('Jogador %d, sua vez de marcar' % jogador)
    while True:
        # 1 jogada
        lin = int(input('Número da linha: '))#Inserindo a Linha
        while lin > 3 or lin <=0: #Validando a Linha
            print("Linha deve ser entre 1 e 3")
            lin = int(input('Número da linha: '))

        col = int(input('Número da coluna: '))#Inserindo a Coluna
        while col > 3 or col <=0: #Validando a Coluna
            print("Coluna deve ser entre 1 e 3")
            col = int(input('Número da coluna: '))
        if Tab[lin - 1][col - 1] == '-':  # posição vazia
            break
        else:
            print('Posição ocupada')

    Tab[lin - 1][col - 1] = marca #Marcação

    # incrementa o número de jogadas
    num_jogadas += 1
    # imprime o tabuleiro
    aux.imprimeTabuleiro(Tab)

    # Verica se venceu
    for i in range(len(Tab)):
        for j in range(len(Tab)):
            if Tab[i, 0] == marca and Tab[i, 1] == marca and Tab[i, 2] == marca: #Ganhando pela Linha
                alguem_venceu = True
                break
            if Tab[0, j] == marca and Tab[1, j] == marca and Tab[2, j] == marca: #Ganhando pela Coluna
                alguem_venceu = True
                break
            if Tab[0, 0] == marca and Tab[1, 1] == marca and Tab[2, 2] == marca: #Ganhando pela Diagonal Principal
                alguem_venceu = True
                break
            if Tab[0, 2] == marca and Tab[1, 1] == marca and Tab[2, 0] == marca: #Ganhando pela Diagonal Secundária
                alguem_venceu = True
                break
            else:
                #Muda o jogador e marca
                if jogador == 1:
                    jogador = 2
                    marca = 'O'
                else:
                    jogador = 1
                    marca = 'X'

if alguem_venceu:
    print('O jogador %d Venceu!!!' % jogador)
else:
    print('Empate')