class Legitarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def get_nev(self):
        return self.nev

    def append_jaratok(self, jarat):
        self.jaratok.append(jarat)

    def info(self):
        jaratok_info = []
        for jarat in self.jaratok:
            jaratok_info.append(jarat.info())
        return '\n'.join(jaratok_info)

