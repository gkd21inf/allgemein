from random import *

erwuenschte_zahl = input("Ein Wuerfel wird mehrmals geworfen. Auf welche Zahl wartest Du?")

wurf = 0
repeat 6:
    zahl = randint(1,6)
    wurf += 1
    if zahl == erwuenschte_zahl:
        print("Deine Zahl wurde beim", wurf, ".ten Wurf zum ersten Mal gewürfelt")
