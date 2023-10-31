#Aula de classe e objetos
#import televisor
from televisor import Televisor

tv = Televisor(1, 99)
for x in range(120):
    tv.mudaCanalParaCima()
print(tv.canal)
for x in range(120):
    tv.mudaCanalParaBaixo()
print(tv.canal)