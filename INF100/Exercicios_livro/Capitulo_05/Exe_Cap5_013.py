# progressão Geotrica
print("Calculo da soma dos N elementos de uma Progressão Geométrica.")
a1 = int(input("Entre com o primeiro elemento da PG: "))
n = int(input("Entre com o numero de elementos elemento da PG: N= "))
q = float(input("Entre com o valor da razão da PG: "))

an = a1 * q**(n-1)

# an : numero que queremos obter
# a1: o primeiro numero da sequencia
# q**(n-1): Razão elevada ao numero que queremos obter menos 1
if q == 1:
    Sn = a1 * n
else:
    Sn = a1*((q**n - 1)/(q -1))
# Sn: Soma dos numeros da PG
# a1: primeiro termo da sequência
# q : razão
# n: quantidade de elementos da PG

print("")
print("O %d elemento da PG é %.2f " % (n, an))
print("A soma dos %d elemento da PG é %.2f " % (n, Sn))