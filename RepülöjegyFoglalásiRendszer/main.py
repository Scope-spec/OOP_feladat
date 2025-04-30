from Belfoldi import Belfoldi
from Nemzetkozi import Nemzetkozi
from Legitarsasag import Legitarsasag
from Jegyfoglalas import Jegyfoglalas

j1 = Belfoldi("N101", "Budapest", 1200)
j2 = Belfoldi("B02", "Debrecen", 1000)
j3 = Nemzetkozi("Z11", "London", 20000)
j4 = Nemzetkozi("Z12", "Lisbon", 15000)
j5 = Belfoldi("N201", "Pécs", 1400)

lt = Legitarsasag("Testair")
lt.append_jaratok(j1)
lt.append_jaratok(j2)
lt.append_jaratok(j3)
lt.append_jaratok(j4)
lt.append_jaratok(j5)

rendszer = Jegyfoglalas(lt)
rendszer.foglal("Kis Béla", "N101")
rendszer.foglal("Nagy Péter", "N201")
rendszer.foglal("Kiss Márta", "Z12")

def felhasznaloi_felulet(rendszer):
    while True:
        print(f"\n--- {lt.get_nev()} Repülőjegy Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Elérhető járatok")
        print("0. Kilépés")

        valasztas = input("Válassz egy műveletet: ")

        if valasztas == "1":
            name = input("Adja meg a nevét: ")
            jaratszam = input("Adja meg a járatszámot: ")
            eredmeny = rendszer.foglal(name, jaratszam)
            print(eredmeny)

        elif valasztas == "2":
            name = input("Adja meg a nevét: ")
            jaratszam = input("Adja meg a járatszámot: ")
            eredmeny = rendszer.lemond(name, jaratszam)
            print(eredmeny)

        elif valasztas == "3":
            print()
            print("Foglalások:")
            rendszer.foglalasok_listazasa()

        elif valasztas == "4":
            print()
            print("Elérhető járatok:")
            print(lt.info())

        elif valasztas == "0":
            print("Kilépés a rendszerből.")
            break

felhasznaloi_felulet(rendszer)
