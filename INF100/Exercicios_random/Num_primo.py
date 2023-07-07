while True:
    n = int(input('N= '))
    if n <= 0:
        break

    x=2
    while x < n and n % x != 0:
        x +=1

    if x == n:
        print('%d é primo.' % n)
    else:
        print('%d não é primo.' % n)
