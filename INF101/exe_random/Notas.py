def leia_notas(v_min,v_max):
    dados =[]
    cont = 0
    dado = int(input(f"Digite uma nota entre {v_min} e {v_max}: "))
    while dado != -1:
        if dado >= 0 and dado <= 100:
            dados.append(dado)
            cont += 1
        else:
            print(f"Valor invalido! O valor deve estar entre {v_min} e {v_max}.")

        dado = int(input(f"Digite uma nota entre {v_min} e {v_max}: "))

    return dados, cont
def calc_media(lista):

    return sum(lista)/len(lista)

notas,cont = leia_notas(0,100)
media = calc_media(notas)

print("\nDados lidos:\n",notas)
print(f"Dados validos {cont}")
print(f"Media das notas: {media:.2f}")