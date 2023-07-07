#Escreva um programa para ler o número de gols marcados pelo Flamengo e o
#número de gols marcados pelo Fluminense em um Fla-Flu. Então, escreva o nome
#do time vencedor ou que houve empate.

gol_fla = int(input("Informe o numero de gols do flamengo: "))
gol_flu = int(input("Informe o numero de gols do fluminense: "))

if gol_fla > gol_flu:
    print("Flamengo vence o fluminense por %d x %d "%(gol_fla,gol_flu))
elif gol_flu > gol_fla:
    print("Fluminense vence o flamengo por %d x %d "%(gol_flu,gol_fla))
else:
    print("A partida terminou empatada.")

