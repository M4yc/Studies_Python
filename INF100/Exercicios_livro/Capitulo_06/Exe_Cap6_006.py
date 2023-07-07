#Escreva um programa para escrever a soma dos números pares e a soma dos
#números ímpares de 1 a 200, inclusive.

# n % 2 == 0 é par

i = 1
somapar= 0
somaimpar = 0

while i <= 200:
    if i % 2 == 0:
        somapar += i
    else:
        somaimpar += i
    i += 1
print("Soma dos números pares de 1 a 200: %d" % somapar)
print("Soma dos números ímpares de 1 a 200: %d" % somaimpar)