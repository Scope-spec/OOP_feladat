from Jaratok import Jaratok

class Belfoldi(Jaratok):
    def _init_(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def info(self):
        return f"Belföldi Járat:  {self.get_jaratszam()} -> Célállomás: {self.get_celallomas()}, Jegyár: {self.get_jegyar()}"


