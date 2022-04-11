from gturtle import *

# Befehl für ein gleichseitiges Dreieck
# mit beliebiger Seitenlaenge
def dreieck(seite):
    repeat 3:
        forward(seite)
        left(120)

makeTurtle()
hideTurtle()
right(90)

# Eingabe der ersten Seitenlaenge
seite = input("Laenge der ersten Dreiecksseite:")

# Schleife, welche immer kleinere Dreiecke zeichnet
# solange wiederholen, bis die Seitenlänge kleiner als 3 ist
while seite >= 3:
    
    # Dreieck zeichnen
    dreieck(seite)  
    
    # Uebergang zum naechsten Dreieck
    left(60)
    forward(seite/2)

    # Seitenlänge halbieren
    seite = seite/2