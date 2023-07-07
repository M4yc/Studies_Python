v = [[2,0,1],
     [2,1,0],
     [1,0,0]]
#2 é bola
#1 é X
#0 é nada


print("\nState:")
for i in range(3):
    for j in range(3):
        print("%3.f"%(v[i][j]), end='')
    print()
n = int(input("Você é qual jogador [1,2]: "))

if (n==v[0][0]==v[0][1]==v[0][2]
    or n==v[1][0]==v[1][1]==v[1][2]
    or n==v[2][0]==v[2][1]==v[2][2]
    or n==v[0][0]==v[1][0]==v[2][0]
    or n==v[0][1]==v[1][1]==v[2][1]
    or n==v[0][2]==v[1][2]==v[2][2]
    or n==v[0][0]==v[1][1]==v[2][2]
    or n==v[0][2]==v[1][1]==v[2][0]): #<=entrou neste caso.
    print(n,"é o vencedor.")
else:
    print(n, "não é o vencedor.")

