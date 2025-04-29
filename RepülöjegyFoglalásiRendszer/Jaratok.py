from abc import ABC, abstractmethod

class Jaratok(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self._jaratszam = jaratszam
        self._celallomas = celallomas
        self._jegyar = jegyar

    def get_jaratszam(self):
        return self._jaratszam
    def get_celallomas(self):
        return self._celallomas
    def get_jegyar(self):
        return self._jegyar

    @abstractmethod
    def info(self):
        pass