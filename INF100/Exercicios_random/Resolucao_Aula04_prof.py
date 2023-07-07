# Nome:
# Matrícula:
# data:
# (Substitua está linha pelo comentário obrigatório)
from datetime import date

hoje = date.today() #pega a data de hoje no sistema
hoje = hoje.strftime('%d/%m/%Y') # formata a data como uma string dd/mm/aaaa
dia_atual, mes_atual, ano_atual = hoje.split('/')
dia_atual = int(dia_atual) #dia atual
mes_atual = int(mes_atual) #mes atual
ano_atual = int(ano_atual) #ano atual

#Input do nome da pessoa
nome = input("Insira seu nome: ")
data_nasc = input("Informe sua data de nascimento (dd/mm/aaaa): ")

# Comando que separa as partes númericas da string, sempre que encontrar /
dia_nasc, mes_nasc, ano_nasc = data_nasc.split('/') #Split da data de nascimento
#Transformação
dia_nasc = int(dia_nasc) # transforma "dd" (dia) para numero inteiro correspondente
mes_nasc = int(mes_nasc) # transforma "mm" (mes) para numero inteiro correspondente
ano_nasc = int(ano_nasc) # transforma "aaaa" (ano) para numero inteiro correspondente

# Calcular a idade
if ano_nasc > ano_atual or ano_nasc == ano_atual and mes_nasc > mes_atual or ano_nasc == ano_atual and mes_nasc == mes_atual and dia_nasc > dia_atual:
    idade = -1
elif mes_atual > mes_nasc or mes_atual == mes_nasc and dia_atual >= dia_nasc: #data é valida
    idade = ano_atual - ano_nasc #já fez aniversario
else:
    idade = ano_atual - ano_nasc -1 #não fez aniversario

#exibição do resultado
if idade == -1:
    print("%s, a data de nascimento (%02d/%02d/%d) está após o dia de hoje!" % (nome, dia_nasc, mes_nasc, ano_nasc))
else:
    print("%s, hoje é dia %02d/%02d/%d e você tem %d " %(nome, dia_atual,mes_atual,ano_atual, idade), end="")
    if idade != 1:
        print("anos.")
    else:
        print("ano.")
