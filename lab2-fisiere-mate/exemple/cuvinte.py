# Programul realizează diverse statistici pe un text dintr-un fișier

inFile = open("cuvinteIn.txt", "r")
continut = inFile.read()

lungimeMax = 0
cuvMax = ""
continutCuvinte = continut.split()

print(f"Textul conține {len(continutCuvinte)} cuvinte.")

for cuvint in continutCuvinte:
	if len(cuvint) > lungimeMax:
		cuvMax = cuvint
		lungimeMax = len(cuvint)

print(f"Cel mai lung cuvînt este \"{cuvMax}\", cu lungimea {lungimeMax}")

nrNumere = 0
for cuvint in continutCuvinte:
	if cuvint.isnumeric():
		nrNumere += 1

print(f"Textul conține {nrNumere} numere.")

punctuatie = [".", ",", ";", "?", "!"]
nrPunctuatie = 0
for cuvint in continutCuvinte:
	for litera in cuvint:
		if litera in punctuatie:
			nrPunctuatie += 1

print(f"Textul conține {nrPunctuatie} semne de punctuație.")

# putem elimina punctuația din cuvinte la calcule
lungimeMaxFaraPunct = 0
cuvMaxFaraPunct = ""
for cuvint in continutCuvinte:
	for punct in punctuatie:
		if punct in cuvint:
			cuvintFaraPunct = cuvint.strip(punct)
			if len(cuvintFaraPunct) > lungimeMaxFaraPunct:
				lungimeMaxFaraPunct = len(cuvintFaraPunct)
				cuvMaxFaraPunct = cuvintFaraPunct

print(f"Cel mai lung cuvînt FĂRĂ PUNCTUAȚIE este \"{cuvMaxFaraPunct}\", cu lungimea {lungimeMaxFaraPunct}")