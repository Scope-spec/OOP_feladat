from Jaratok import Jaratok

class Nemzetkozi(Jaratok):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def info(self):
        return (f"Nemzetközi Járat: {self.get_jaratszam()} -> Célállomás: {self.get_celallomas()}, Jegyár: {self.get_jegyar()}")