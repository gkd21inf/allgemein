# Variable mit mehreren gespeicherten Werten
daten = [4, 2, -6, 17, 5, 12]
print(daten)

# Werte verändern
daten[0] = 5
daten[1] = daten[0]
daten[2] = daten[1]
print(daten)

# Eigenschaft der Liste
eigenschaft = len(daten)
print(eigenschaft)

# Etwas mit der Liste machen
stelle = 0
etwas = 0
repeat eigenschaft:
    wert = daten[stelle]
    etwas += wert
    stelle += 1

print(etwas)

