#Aula de classe e objetos
#import televisor
from televisor import Televisor

tv = Televisor(1, 99, 4, 30)
for x in range(120):
    tv.mudaCanalParaCima()
print(tv.canal)
for x in range(120):
    tv.mudaCanalParaBaixo()

print(tv.canal)
tv.aumentaVolume()
print(tv.volume)