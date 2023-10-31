class Televisor:
    def __init__(self, min, max):
        self.marca = None
        self.tamanho = 0
        self.ligado = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    def mudaCanalParaCima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
    def mudaCanalParaBaixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
