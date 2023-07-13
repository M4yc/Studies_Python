#algorito para troca de pneu
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