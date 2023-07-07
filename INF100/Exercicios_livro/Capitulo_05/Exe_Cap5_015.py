#Faça um programa que leia duas datas, compostas por dia, mês e ano: uma é a data
#de nascimento de alguém, e a outra é a data atual. Em seguida, o programa deve
#imprimir a idade da pessoa. Veja os exemplos:
#dat_nasc = str(input("Insira a sua data de nascimento no formato dd mm aaaa: "))
#dat_atual = str(input("Insira a data atual no formato dd mm aaaa: "))

# leitura da data de nascimento
dia_nasc = int(input("Digite o dia de nascimento: "))
mes_nasc = int(input("Digite o mês de nascimento: "))
ano_nasc = int(input("Digite o ano de nascimento: "))

# leitura da data atual
dia_atual = int(input("Digite o dia atual: "))
mes_atual = int(input("Digite o mês atual: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nasc

#verificação do mes
if mes_atual < mes_nasc:
    idade -= 1
elif mes_nasc == mes_atual and dia_atual < dia_nasc:
    idade -= 1

print("A idade da pessoa é:", idade, "anos.")