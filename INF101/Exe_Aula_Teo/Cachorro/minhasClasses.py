class Cachorro:
    def __init__(self, nome):
        self.nome = nome
    def andar(self):
        return "Andando"

    def latir(self):
        return "AuAu!"

class Pug(Cachorro):
    def latir(self):
        return "Aff!"
    def raca(self):
        return "Pug"
class Poodle(Cachorro) :
    def latir(self) :
        return super().latir() + ' ' + super().latir()
    def raca(self):
        return "Poodle"