def f1(n):
    x = 0
    for i in range(1, n+1):
        x = x + i;
    print(x)
    return x
def f2(n, x, i):
    global L
    for i in range(0, n):
        if L[i] == x:
            return i
    return -1
def main():
    global L
    L = [4, 5, 6]
    for i in range (0, 3):
        L[i] = f1(L[i])
    j = 3
    for i in range(3, 0, -1):
        j = f2(3, i*5, j)
        if j >= 0:
            print(i, " > ", j)
        else:
            print(i, " < ")
main()
