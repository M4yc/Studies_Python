#Escreva um programa que exiba os números divisíveis por 4 e por 5 menores que 200.

i = 0

while i <= 200:
    if i % 4 == 0 and i % 5 == 0:
        print("| %d |" % i)
    i += 1