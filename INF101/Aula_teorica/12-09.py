import math
import numpy
import random

quadrados = [ x**2 for x in range(10)]
print("Imprime lista com o quadrado dos números de 0 a 9:")
for i in quadrados:
    print(f"{i:.0f}",end=', ')
