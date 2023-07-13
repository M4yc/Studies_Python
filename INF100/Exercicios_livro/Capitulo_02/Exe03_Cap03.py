#algorito para troca de pneu
print("Algoritmo para troca de pneu.")
print("[1] para pneu furado.")
print("[0] para pneu bom.")
pneu = int(input("O pneu está furado: "))
if pneu == True:
    print("Precisa trocar de pneu.")
else:
    print("O Pneu ainda está bom")
    libra = int(input("Com quantas libras o pneu está: "))
    if libra < 20:
        print("Precisa encher")
    else:
        print("Está bom assim.")