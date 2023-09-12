import math
import numpy
import random

quadrados = [math.sqrt(x) for x in range(10)]

for i in quadrados:
    print(f"Imprime lista com o quadrado dos números de 0 a 9:{i:.2f}")
