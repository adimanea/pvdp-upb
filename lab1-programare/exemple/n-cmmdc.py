# Programul afișează cmmdc al numerelor dintr-o listă.

# funcție de cmmdc între 2 numere
def cmmdc(a, b):
	"""Calculează cmmdc între două numere"""
	# dacă vreuna dintre valor este nulă, returnăm eroare
	if a * b == 0:
		return -1
	if a == 1 or b == 1:
		return 1
	# Euclid clasic, cu scăderi
	while a != b:
		if a > b:
			a -= b
		else:
			b -= a
	return a

def ncmmdc(n, lista):
	"""Calculează cmmdc pentru n elemente din listă"""
	d = lista[0]
	for i in range(n - 1):
		# atenție: funcția range lucrează cu intervale deschise
		# i in range(3) înseamnă i = 0, 1, 2
		# la fel și dacă scrieți i in range(0, 3), înseamnă 0, 1, 2
		d = cmmdc(lista[i], lista[i + 1])
	return d


# Programul principal
# atenție: Python nu cere neapărat să avem o funcție main()
# Cei obișnuiți cu C și C++ pot scrie ca mai jos
def main():
	n = int(input("Introduceți numărul de elemente: "))
	# lista goală de numere:
	lista = []
	print(f"Acum introduceți cele {n} numere:")
	for i in range(n):
		# citim elementele și le adăugăm în listă
		element = int(input())
		lista.append(element)

	nc = ncmmdc(n, lista)

	print(f"cmmdc al elementelor din listă este {nc}")


# la final, apelăm funcția main()
if __name__ == '__main__':
	main()

# Dacă nu doriți să lucrați cu funcția main(), 
# puteți șterge sau comenta liniile 33 și 48-50