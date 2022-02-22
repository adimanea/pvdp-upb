# Programul exemplifică unele funcții din biblioteca de matematică.
# Pentru simplitate, nu mai adăugăm validarea datelor.

import math

def combinari():
	"""Funcția calculează combinări de n luate cîte k"""
	n = int(input("n = "))
	k = int(input("k = "))
	print(f"Combinări de {n} luate cîte {k} = {math.comb(n, k)}")

def factorial():
	"""Funcția calculează n!"""
	n = int(input("n = "))
	print(f"{n}! = {math.factorial(n)}")

def suma():
	"""Funcția calculează suma valorilor dintr-o listă."""
	n = int(input("Numărul de elemente din listă: "))
	lista = []
	print("Introduceți elementele:")
	while len(lista) < n:
		lista.append(int(input()))
	print(f"Suma elementelor introduse este {math.fsum(lista)}")

def intRad():
	"""Funcția calculează partea întreagă a radicalului"""
	x = int(input("x = "))
	print(f"[sqrt({x})] = {math.isqrt(x)}")

def expo():
	"""Funcția calculează exponențiala numărului introdus, în baza e"""
	x = float(input("x = "))
	print(f"exp({x}) = {math.exp(x)}")

def logaritm():
	"""Funcția calculează logaritmul în baza b din x"""
	b = int(input("Baza logaritmului: "))
	x = float(input("Argumentul logaritmului: "))
	print(f"Logaritm în baza {b} din {x} este {math.log(b, x)}")

def distanta():
	"""Funcția calculează distanța euclidiană între două puncte"""
	p = []
	q = []
	d = int(input("Introduceți dimensiunea: "))
	print("Introduceți coordonatele primului punct:")
	while len(p) < d:
		p.append(float(input()))
	print("Introduceți coordonatele celui de-al doilea punct:")
	while len(q) < d:
		q.append(float(input()))
	print(f"Distanța dintre punctele introduse este {math.dist(p, q)}")

def eulerGamma():
	"""Funcția calculează valoarea funcției Gamma a lui Euler"""
	n = int(input("n = "))
	print(f"Gamma(n) = {math.gamma(n)}")


print("Programul reprezintă un calculator. Alegeți operația dorită:")
print("1. Combinări de n luate cîte k")
print("2. Factorial")
print("3. Suma valorilor dintr-o listă")
print("4. Partea întreagă a radicalului")
print("5. Exponențială în baza e")
print("6. Logaritm în bază precizată")
print("7. Distanța dintre două puncte")
print("8. Funcția Gamma a lui Euler")

optiune = int(input("\nOpțiunea: "))
while optiune not in range(1, 9):
	print("Opțiune invalidă. Reîncercați.")
	optiune = int(input("\nOpțiunea: "))

if optiune == 1:
	combinari()
elif optiune == 2:
	factorial()
elif optiune == 3:
	suma()
elif optiune == 4:
	intRad()
elif optiune == 5:
	expo()
elif optiune == 6:
	logaritm()
elif optiune == 7:
	distanta()
else:
	eulerGamma()