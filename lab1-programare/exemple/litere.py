# Programul afișează prima literă a unui cuvînt, ultima literă,
# numărul de litere, cuvîntul inversat și sortat alfabetic

cuv = input("Introduceți un cuvînt (fără diacritice): ")
print(f"Prima literă din {cuv} este {cuv[0]}")
print(f"Ultima literă din {cuv} este {cuv[-1]}")
print(f"Numărul de litere din {cuv} este {len(cuv)}")
print(f"{cuv} invers este {cuv[::-1]}")

# transformăm cuvîntul în listă (inițial, este string)
cuvLista = list(cuv)
cuvLista.sort()

# înapoi în string (cuvînt)
cuvSortat = ""
for litera in cuvLista:
	cuvSortat += litera
print(f"{cuv} sortat alfabetic este {cuvSortat}")