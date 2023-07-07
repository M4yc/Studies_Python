N = 4
W = 7
for j in range(0,N):
    i = j + 4
    print(i, end='')
    while i < W:
        print('*', end='')
        i= i+1
    print(i)
