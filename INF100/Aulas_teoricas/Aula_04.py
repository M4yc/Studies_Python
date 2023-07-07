#Aula de loop
#While
#Autor: Maycon Vinicius
#17/04/2023 - 18/04/2023
nota = float(input("Insira sua nota: "))
while nota < 0 or nota > 100:
    print("Nota Inválida.")
    nota = float(input("Insira sua nota: "))

print("Fim")