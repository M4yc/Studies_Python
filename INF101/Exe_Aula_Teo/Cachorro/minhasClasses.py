class Cachorro:
    def andar(self):
        return "Andando"

    def latir(self):
        return "AuAu!"

class Pug(Cachorro):
    def latir(self):
        return "Aff!"

class Poodle(Cachorro) :
    def latir(self) :
        return super().latir() + ' ' + super().latir()