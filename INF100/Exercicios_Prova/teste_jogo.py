# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i][j], end=" ")
        print()


# Função para verificar se alguém ganhou
def verificar_ganhador(tabuleiro, jogador):
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True

    # Verificar colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False


# Função principal do jogo
def jogo_da_velha():
    # Tabuleiro inicial vazio
    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    jogador = "X"
    jogadas = 0

    while True:
        # Imprimir o tabuleiro
        imprimir_tabuleiro(tabuleiro)

        # Solicitar a jogada
        linha = int(input("Digite a linha (0-2): "))
        coluna = int(input("Digite a coluna (0-2): "))

        # Validar a jogada
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2 or tabuleiro[linha][coluna] != " ":
            print("Jogada inválida. Tente novamente.")
            continue

        # Realizar a jogada
        tabuleiro[linha][coluna] = jogador
        jogadas += 1

        # Verificar se alguém ganhou
        if verificar_ganhador(tabuleiro, jogador):
            imprimir_tabuleiro(tabuleiro)
            print("Jogador", jogador, "venceu!")
            break

        # Verificar se deu empate
        if jogadas == 9:
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # Alternar o jogador
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"


jogo_da_velha()
