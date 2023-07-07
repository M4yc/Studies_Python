while True:
    N = int(input('N = '))
    if N < 3 or N > 10:
        print("Valor deve estar entre (3, 10)")
    else:
        break
lim = 2*N
cont = 1
for i in range(1,N+1):
    for j in range(1,2*N+1):
        print(2*j-1, end=' ')
    print()


