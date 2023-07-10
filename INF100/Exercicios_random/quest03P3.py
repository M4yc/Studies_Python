import numpy as np
BIKES = np.empty((9,8),dtype=str)
BIKES[8][7] = "R"
for i in range(0,7):
    BIKES[8][i] = 'E'
for i in range(0,8):
    BIKES[i][2] = 'r'
for i in range(0,9):
    for j in range(0,8):
        if BIKES[i][j] == '':
            BIKES[i][j] = 'S'

print(BIKES)