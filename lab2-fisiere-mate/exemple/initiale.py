# Programul afișează cuvîntul rezultat din inițialele cuvintelor dintr-un fișier

fisierIn = open("initialeIn.txt", "r")
continut = fisierIn.read()

cuvinte = continut.split()

initiale = ""
for cuv in cuvinte:
	initiale += cuv[0]

print(f"Cuvîntul obținut din inițiale este {initiale}.")