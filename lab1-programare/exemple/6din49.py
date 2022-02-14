# Programul extrage 6 numere, de la 1 la 49,
# cere utilizatorului să introducă și el 6 numere,
# apoi afișează cîte numere a ghicit utilizatorul.

import random

extrase = []
while len(extrase) < 6:
	# adăugăm la lista de extrase, fără dubluri
	x = random.randint(1, 49)
	if x not in extrase:
		extrase.append(x)

print("Introduceți cele 6 numere alese:")
alese = []
while len(alese) < 6:
	x = int(input())
	if x in alese or x < 1 or x > 49:
		print("Numărul introdus nu poate fi acceptat. Reîncercați.")
	else:
		alese.append(x)

ghicite = [a for a in alese if a in extrase]

print(f"S-au extras numerele: {extrase}.")
print(f"Ați ales numerele: {alese}.")

if len(ghicite) == 0:
	print(f"Nu ați ghicit niciun număr.")
else:
	print(f"Ați ghicit {len(ghicite)} numere, anume {ghicite}.")