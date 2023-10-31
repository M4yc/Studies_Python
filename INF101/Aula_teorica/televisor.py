class Televisor:
    def __init__(self, min, max, c, vol):
        self.marca = None
        self.tamanho = 0
        self.ligado = False
        self.canal = c
        self.cmin = min
        self.cmax = max
        self.volume = vol
    def mudaCanalParaCima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin
            
    def mudaCanalParaBaixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def aumentaVolume(self):
        if self.volume + 1 <= 100:
            self.volume += 1
    def diminuiVolume(self):
        if self.volume - 1 >= 0:
            self.volume -= 1
