# Acest program implementează cifrul Caesar:
# - se cere de la tastatură un cuvînt;
# - se cere un număr (cheia de criptare);
# - se afișează cuvîntul rezultat prin translația literelor din cuvîntul inițial
#   cu un număr de poziții date de cheie.
# Se va lucra în Z26, adică folosind alfabetul englez, fără punctuație.

# păstrăm alfabetul într-o listă, pentru a prelua pozițiile
# astfel, A = 0, B = 1, C = 2, ..., Z = 25.
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
		   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
		   's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

mesaj = input("Introduceți cuvîntul de criptat (fără pauze și diacritice): ")

# validare (opțională): ne asigurăm că mesajul conține doar caractere din lista alfabet
mesajOK = 0
while mesajOK == 0:
	for c in mesaj:
		if c not in alfabet:
			mesajOK = 0
			print(f"Mesajul introdus nu conține doar litere din alfabet. Reîncercați.")
			mesaj = input("Introduceți cuvîntul de criptat (fără pauze și diacritice): ")
			break
		else:
			mesajOK = 1	

# eliminăm majusculele, dacă există
mesaj = mesaj.lower()

# cheia de criptare
cheie = int(input("Introduceți cheia de criptare: "))

# validare: cheia trebuie să fie pozitivă
while cheie < 0:
	print("Cheia trebuie să fie pozitivă. Reîncercați.")
	cheie = int(input("Introduceți cheia de criptare"))

# dacă cheie > 26, preluăm valoarea din Z26
cheie = cheie % 26

# obținem lista de litere din mesaj
# scriem lista direct, cu o tehnică numită LIST COMPREHENSION
# detalii aici: https://www.w3schools.com/python/python_lists_comprehension.asp
litereMesaj = [litera for litera in mesaj]

# obținem lista de poziții în alfabet ale literelor din mesaj
pozitiiLitera = [alfabet.index(litera) for litera in litereMesaj]

# obținem lista de poziții mutate cu cheia
pozitiiCriptate = [(p + cheie) % 26 for p in pozitiiLitera]

# obținem lista de litere corespunzătoare pozițiilor criptate
litereCriptate = [alfabet[p] for p in pozitiiCriptate]

# obținem cuvîntul criptat
cuvCriptat = ''
for lc in litereCriptate:
	cuvCriptat += lc

# afișăm mesajul criptat
print(f"Cuvîntul criptat este {cuvCriptat}.")