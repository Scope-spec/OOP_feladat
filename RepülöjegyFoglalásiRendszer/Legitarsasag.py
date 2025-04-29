class Legitarsasag:
    def __init__(self, nev):
        self._nev = nev
        self._jaratok = []

    def get_nev(self):
        return self._nev

    def append_jaratok(self, jarat):
        self._jaratok.append(jarat)

    def info(self):
        jaratok_info = []
        for jarat in self._jaratok:
            jaratok_info.append(jarat.info())
        return '\n'.join(jaratok_info)

