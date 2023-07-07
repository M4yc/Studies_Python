#Escreva um programa para ler o número de gols marcados pelo Flamengo e o
#número de gols marcados pelo Fluminense em um Fla-Flu. Então, escreva o nome
#do time vencedor ou que houve empate.
vit_Fla = 0
vit_Flu = 0
empate = 0
n_partida = 0
vencedor = ''
ngols_flu = 0
ngols_fla = 0
while True:
    gol_fla = int(input("Informe o numero de gols do flamengo: "))
    gol_flu = int(input("Informe o numero de gols do fluminense: "))

    if gol_fla > gol_flu:
        print("Flamengo vence o fluminense por %d x %d " % (gol_fla, gol_flu))
        vit_Fla += 1
    elif gol_flu > gol_fla:
        print("Fluminense vence o flamengo por %d x %d " % (gol_flu, gol_fla))
        vit_Flu += 1
    else:
        print("A partida terminou empatada.")
        empate += 1

    n_partida += 1
    ngols_flu += gol_flu
    ngols_fla += gol_fla

    resposta = str(input("Novo Fla-Flu 1.Sim 2.Não?"))
    if resposta == "N" or resposta == "2":
        break

if vit_Fla > vit_Flu:
    vencedor = 'Flamengo'
elif vit_Flu > vit_Fla:
    vencedor = 'Fluminense'
elif vit_Fla == vit_Flu:
    if ngols_fla > ngols_flu:
        empate -= 1
        vit_Fla += 1
    elif ngols_flu > ngols_fla:
        empate -= 1
        vit_Flu += 1

print('')
print("--Resultado Final--")
print("Numero de partidas do Fla-Flu: %d " % n_partida)
print("Numero de vitorias do Flamengo: %d " % vit_Fla)
print("Numero de vitorias do Fluminense: %d " % vit_Flu)
print("Numero de empates: %d " % empate)
print("Time com maior numero de vitorias: %s " % vencedor)