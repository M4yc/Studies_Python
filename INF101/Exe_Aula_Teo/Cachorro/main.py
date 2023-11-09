from minhasClasses import Cachorro, Pug, Poodle
#import minhasClasses as mc
cao = Cachorro('Caramelo')
print( 'Cão' )
print( cao.nome )
# print( cao.raca )
print( cao.andar() )
print( cao.latir() )

cao1 = Pug('Tiu')
print( '\nCão1' )
print( cao1.nome )
print( cao1.raca )
print( cao1.andar() )
print( cao1.latir() )

cao2 = Poodle('Cachorro')
print( '\nCao2' )
print( cao2.nome )
print( cao2.raca )
print( cao2.andar() )
print( cao2.latir() )