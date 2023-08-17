def fatorial (n):
    fat = 1
    if n == 0:
        return 1
    for i in range(2,n+1):
        fat *= i
    return fat
n = int(input("Qual número quer o fatorial: "))

print(fatorial(n))
