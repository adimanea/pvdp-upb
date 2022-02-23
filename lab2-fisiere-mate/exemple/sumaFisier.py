# Programul calculează suma numerelor dintr-un fișier și scrie într-un alt fișier

suma = 0
with open("sumaFisierIn.txt", "r") as fIn:
	continut = fIn.readlines()
	for linie in continut:
		suma += int(linie)

with open("sumaFisierOut.txt", "w") as fOut:
	fOut.write("Suma numerelor din fisier este\n")
	fOut.write(str(suma))
