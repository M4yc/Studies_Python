dia_atual = 22
mes_atual = 4
ano_atual = 2023

nome = input("Insira seu nome: ")

data_nasc = input("Informe sua data de nascimento (dd/mm/aaaa): ")
dia_nasc, mes_nasc, ano_nasc = data_nasc.split('/') #Split da data de nascimento

dia_nasc = int(dia_nasc) # transforma "dd" (dia) para numero inteiro correspondente
mes_nasc = int(mes_nasc) # transforma "mm" (mes) para numero inteiro correspondente
ano_nasc = int(ano_nasc) # transforma "aaaa" (ano) para numero inteiro correspondente

#idade = ano_atual - ano_nasc

if ano_nasc > ano_atual: #Verificando se a data é valida
    print("%s, a data de nascimento (%s) está após o dia de hoje!" % (nome, data_nasc))
elif ano_atual == ano_nasc and mes_nasc > mes_atual:
    print("%s, a data de nascimento (%s) está após o dia de hoje!" % (nome, data_nasc))
elif ano_atual == ano_nasc and mes_nasc == mes_atual and dia_nasc > dia_atual:
    print("%s, a data de nascimento (%s) está após o dia de hoje!" %(nome, data_nasc))
else:
    if dia_nasc == dia_atual and mes_nasc == mes_atual and ano_nasc == ano_atual:
        idade = 0
        print("")
        print("%s, hojé é dia %s/%s/%s e você tem %d anos." % (nome, dia_atual, mes_atual, ano_atual, idade))
    elif dia_nasc == dia_atual and mes_nasc == mes_atual:
        idade = ano_atual - ano_nasc
        print("")
        print("%s, hojé é dia %s/%s/%s e você tem %d anos." %(nome, dia_atual, mes_atual, ano_atual, idade))
        print("Aliás, meus parabéns!!! Hoje é o seu aniversário!")

    else:
        idade = ano_atual - ano_nasc
        if idade == 1:
            print("")
            print("%s, hojé é dia %s/%s/%s e você tem %d ano." % (nome, dia_atual, mes_atual, ano_atual, idade))
        else:
            print("")
            print("%s, hojé é dia %s/%s/%s e você tem %d anos." % (nome, dia_atual, mes_atual, ano_atual, idade))