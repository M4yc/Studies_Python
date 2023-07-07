import turtle as t

def quadrado(tamanho):
    for _ in range(4):
        t.forward(tamanho)
        t.right(90)

def shift(delta_x, delta_y):
    t.up()
    x, y = t.window_width() // 2, t.window_height() // 2
    t.goto(-x + delta_x, y - delta_y)
    t.down()

h = int(input('Tamanho do quadrado externo: '))

while h > 0:
    quadrado(h)
    shift(5, -5)
    h -= 10

t.Screen().exitonclick()
