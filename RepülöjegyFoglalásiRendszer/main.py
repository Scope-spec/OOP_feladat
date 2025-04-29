from Belfoldi import Belfoldi
from Nemzetkozi import Nemzetkozi
from Legitarsasag import Legitarsasag

j1 = Belfoldi("N101", "Budapest", 1200)
j2 = Belfoldi("B02", "Debrecen", 1000)
j3 = Nemzetkozi("Z11", "London", 20000)
j4 = Nemzetkozi("Z12", "Lisbon", 15000)

lt = Legitarsasag("Testair")
lt.append_jaratok(j1)
lt.append_jaratok(j2)
lt.append_jaratok(j3)
lt.append_jaratok(j4)

#print(f"---- {lt.get_nev()} ----")




def felhasznaloi_felulet():
    while True:
        print(f"\n--- {lt.get_nev()} Repülőjegy Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Elérhető járatok")
        print("0. Kilépés")

        valasztas = input("Válassz egy műveletet: ")
        """""
        if valasztas == "1":

        elif valasztas == "2":

        elif valasztas == "3":
        """
        if valasztas == "4":
            print()
            print("Elérhető járatok:")
            print(lt.info())

        elif valasztas == "0":
            print("Kilépés a rendszerből.")
            break

felhasznaloi_felulet()
