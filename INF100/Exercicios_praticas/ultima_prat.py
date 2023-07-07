import imagens
def trocar_verde_por_azul(imagem):
    lin = im.altura
    col = im.largura
    for i in range(0,lin):
        for j in range(0,col):
            r, g, b = imagem[i, j]  # Obtém as componentes RGB do pixel atual
            if g > r and g > b:  # Verifica se o verde é a cor predominante
                imagem[i][j] = (r, 0, b)  # Substitui o verde pelo azul, mantendo as outras componentes

# Exemplo de uso:
nome = 'cores.png'
im = imagens.Imagem(nome)
trocar_verde_por_azul(im)
im.mostrar()