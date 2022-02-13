# Klartext eingeben lassen und in Grossbuchstaben umwandeln
klartext = input("Klartextwort:")
klartext = klartext.upper()

# Anzahl 3er Bloecke in String berechnen
laenge = len(klartext)
anzahl_bloecke = laenge // 3

# Alle Bloecke durchgehen und die gewuenschten Characters vertauschen
block = 0
text_liste = list(klartext)
while block < anzahl_bloecke:
    # Jeder Block startet beim Buchstaben 3*block (0, 3, 6, 7, ...)
    print("Block ", block, " von ", anzahl_bloecke, ": Buchstaben", 3*block, "bis", 3*block+2)
    # In jedem Block hat es die Positionen 0, 1, 2 -- Hier werden Positionen 0 und 2 vertauscht
    text_liste[block*3+0], text_liste[block*3+2] = text_liste[block*3+2], text_liste[block*3+0]
    block += 1

# Ein String generieren
geheimtext = "".join(text_liste)

# Resultate ausgeben
print("Klartext  :", klartext)
print("Geheimtext:", geheimtext)