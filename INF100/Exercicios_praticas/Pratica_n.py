def primo(N):
    if N <= 1:
        print("O numero %d não é Primo." % N)
        print("O numero %d possui 1 divisor" % N)
        return
    is_primo = 1
    cont = 0

    for i in range(1,N+1):
        if N % i == 0:
            cont +=1
    if cont > 2:
        is_primo = 0
    if is_primo == 1:
        print("O numero %d é Primo." % N)
    else:
        print("O numero %d não é Primo." % N)
    print(f"O numero {N} tem {cont:.2f} divisores.")

N = int(input("Insira o numero que deseja: "))
primo(N)
