##### fisier.txt ########
# Ana are mere. Ion vrea
# să cumpere gutui.
#########################

with open("fisier.txt", "r") as f:
	linii = f.readlines()
	print(linii)
	
	for linie in linii:
		print(linie)			

	
	for linie in linii:
		cuv = linie.split()
		print(cuv)

	f.seek(0, 0)
	continut = f.read()
	print(continut)
	propozitii = continut.split(".")
	print(propozitii)					