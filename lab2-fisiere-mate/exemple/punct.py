# Programul afișează cel mai apropiat punct din plan 
# de un punct citit de la tastatură
import math

print("""Programul afișează cel mai apropiat punct
	din plan de un punct introdus de la tastatură.""")
print("Introduceți cele două coordonate ale punctului:")
x = float(input("x = "))
y = float(input("y = "))

p = [x, y]
punctMin = []
d = 9999
with open("punctIn.txt", "r") as fIn:
	# citim punctele, linie cu linie
	puncte = fIn.readline()
	while puncte:
		# punctele se citesc ca o listă de string-uri,
		# deci le transformăm într-o listă de float-uri
		punct = list(map(float, puncte.split()))
		if math.dist(p, punct) < d:
			d = math.dist(p, punct)
			punctMin = punct
		puncte = fIn.readline()

print(f"Punctul cel mai apropiat de {p} este {punctMin},")
print(f"care se află la distanța {round(d, 3)}.")