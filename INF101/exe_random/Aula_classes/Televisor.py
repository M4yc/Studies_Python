
class Televisor:
  def __init__(self):
    self.ligado = False
    self.canal = 2

tv = Televisor()
print('Tv está ligada? ', tv.ligado)
print('Canal da Tv:', tv.canal)
print()

tv_sala = Televisor()
print('Tv está ligada? ', tv_sala.ligado)
print('Canal da Tv:', tv_sala.canal)
tv_sala.ligado = True
tv_sala.canal = 4
print('Tv está ligada? ', tv_sala.ligado)
print('Canal da Tv:', tv_sala.canal)

print('Canal da Tv:', tv.canal)
print('Canal da Tv da sala:', tv_sala.canal)

print( type(tv) )