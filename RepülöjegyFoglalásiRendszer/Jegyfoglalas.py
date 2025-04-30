from Legitarsasag import Legitarsasag

class User:
    def __init__(self, name, jarat):
        self.name = name
        self.jarat = jarat

class Jegyfoglalas(Legitarsasag):
    def __init__(self, legitarsasag):
        self.legitarsasag = legitarsasag
        self.foglalasok = []

    def foglal(self, user, jaratszam):
        jarat = next((j for j in self.legitarsasag.jaratok if j.get_jaratszam() == jaratszam), None)
        if not jarat:
            return "Hiba: Nincs ilyen járat!"
        else:
            foglalas = User(user, jarat)
            self.foglalasok.append(foglalas)
            return f"A foglalás sikeres! {jarat.get_jegyar()}"

    def lemond(self, user, jaratszam):
        for foglalas in self.foglalasok:
            if foglalas.name == user and foglalas.jarat.get_jaratszam() == jaratszam:
                self.foglalasok.remove(foglalas)
                return "Foglalás sikeresen lemondta!"
            else:
                return "Nincs ilyen foglalás"

    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"{foglalas.name}: {foglalas.jarat.get_jegyar()}")
