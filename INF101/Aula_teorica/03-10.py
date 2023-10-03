notas = {"113683": ("Maycon", 21, "M"),
         "113684": ("Mariana", 24, "F"),
         "113685": ("Josue", 15, "M"),
         "113686": ("Isabella", 17, "F")}

#cont = 0

#for matricula, (nome, idade, sexo) in notas.items():
    #if idade > 18:
        #cont += 1

#print("Maiores de 18:", cont)

notas = ["113685"][1] = 18

def verIdade(notas):
    cont = 0
    for matricula, (nome, idade, sexo) in notas.items():
        if idade > 18:
            cont += 1

    return cont

