from Domestic import Domestic
from International import International

j1 = Domestic("N30", "Budapest", 400)
j2 = Domestic("B102", "Debrecen", 1000)
j3 = International("N100", "New York", 100000)
j4 = International("B888", "Paris", 34440)
print(j1.info())
print(j2.info())
print(j3.info())
print(j4.info())

