import turtle as t

def quadrado( tamanho ):
    for i in range(0, 4):
        t.forward( tamanho )
        t.right( 90 )

def shift( delta_x, delta_y ):
    t.up()
    t.goto( t.xcor() + delta_x, t.ycor() + delta_y )
    t.down()

h = int(input('Tamanho do quadrado externo: '))

while h > 0:
    quadrado( h )
    shift( 5, -5 )
    h = h - 10
t.Screen().exitonclick()
