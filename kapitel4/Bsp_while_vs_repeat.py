from gturtle import *

makeTurtle()
hideTurtle()

laenge= input("Wie lange ist die erste Seite der Spirale?")

while laenge > 2:
    forward(laenge)
    right(90)
    laenge = laenge/1.5