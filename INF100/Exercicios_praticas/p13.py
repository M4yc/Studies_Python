import imagens

def main():
    #nome = input('Nome do arquivo: ')
    nome = '1207769.jpg'

    im = imagens.Imagem(nome)
    #im.mostrar()
    lin = im.altura
    col = im.largura

    while True:
        qc = int(input("Quadrante a ser copiado: "))
        if qc >= 1 and qc <=4:
            break
        print("O valor deve estar entre 1 e 4.")

    while True:
        qe = int(input("Quadrante a ser eliminado: "))
        if qe >= 1 and qe <=4 and qe != qc:
            break
        elif qe < 1 or qe > 4:
            print("O valor deve estar entre 1 e 4.")
        if qe >= 1 and qe <=4 and qe == qc:
            print("Os dois quadrantes devem ser diferentes.")
    #########################################################
    #Quadrante a ser copiado
    if qc == 1 or qc == 2:
        dci=0
    else:
        dci = lin//2

    if qc == 1 or qc == 3:
        dcj = 0
    else:
        dcj = col//2

    # Quadrante a ser eliminado
    if qe == 1 or qe == 2:
        dei = 0
    else:
        dei = lin // 2

    if qe == 1 or qe == 3:
        dej = 0
    else:
        dej = col // 2

    for i in range(0,lin//2):
        for j in range(0,col//2):
            im[i+dei][j+dej] = im[i+dci][j+dcj]
    im.mostrar()

main ()