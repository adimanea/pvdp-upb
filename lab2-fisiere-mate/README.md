# Lucrul cu fișiere text și funcții matematice standard

De cele mai multe ori, nu este comod să lucrăm cu date introduse 
de la tastatură. Mai mult decît atît, sîntem și limitați, pentru că dacă
vrem să realizăm un test pe sute sau mii de numere ori linii de text,
va fi foarte greu să le introducem manual, de la tastatură. De aceea,
în majoritatea situațiilor, se preferă lucrul cu fișiere text. Acestea
pot fi folosite atît ca date de intrare, cît și ca date de ieșire.
Cu alte cuvinte, vom putea *citi din fișier* datele pe care le prelucrăm
și vom putea *scrie în fișier* rezultatul calculelor.

Vom prezenta pe scurt în acest laborator lucrul cu fișiere text, atît
pentru date de intrare, cît și pentru date de ieșire. În mare,
putem lucra cu astfel de fișiere detaliate în codul sursă, sau le putem
folosi drept *argumente* atunci cînd rulăm programul. Vom vedea avantajele
și dezavantajele fiecăreia dintre cele două metode.

## Fișere text în cod
Ca în majoritatea limbajelor de programare, lucrul cu fișiere se bazează
pe atribuirea lor la variabile din program, precum și pe folosirea unor
funcții specifice de citire și scriere.

Una dintre cele mai simple metode în Python este aceasta:
```python
file = open("fisier_intrare.txt", "r")
print(file.read())
```

În exemplul de mai sus, fișierul `fisier_intrare.txt`, *care se află în același*
*director cu sursa programului* este deschis folosind funcția `open`.
El se deschide pentru citire, ceea ce se vede din argumentul `"r"` (pentru `read`).
Conținutul fișierului se accesează atunci cînd folosim metoda `read()`. Fără aceasta,
variabila `file` doar face legătura (este un fel de pointer) cu fișierul respectiv.

Funcția `read()` citește *întreg* conținutul fișierului. Dar putem să precizăm
cîte caractere să se citească din fișier, dînd un argument. Astfel, un apel precum
```py
file = open("fisier_intrare.txt", "r")
caractere = file.read(3)
```
păstrează primele 3 caractere din fișier în variabila `caractere`, de tip `string`.

Scrierea în fișiere este la fel de intuitivă:
```py
file = open("fisier_iesire.txt", "w")
file.write("Mesaj de scris în fișier")
```

Deschidem de data aceasta un fișier pentru scriere (dînd argumentul `"w"` la funcția `open`)
și scriem în fișier cu metoda `write`.

Pentru evitarea erorilor, se recomandă ca fișierele deschise pentru scriere
sau citire să se închidă cînd nu se mai folosesc, cu metoda `close()`.
Astfel, dacă linia respectivă este tot ce am vrea să scriem în fișier, de exemplu,
completăm codul:
```py
file = open("fisier_iesire.txt", "w")
file.write("Mesaj de scris în fișier")
file.close()
```

Modul `write` șterge fișierul și scrie doar conținutul pe care îl precizăm (face *overwrite*).
Dacă fișierul pe care îl deschidem pentru scriere mai conține deja text, putem folosi
modul `append`, care *adaugă* ceea ce indicăm la conținutul deja existent.
Astfel, am avea:
```py
file = open("fisier_iesire.txt", "a")
file.write("Mesaj de adăugat în fișier")
file.close()
```

Dacă vrem doar să creăm un fișier (eventual, pentru utilizare ulterioară), folosim
modul `"x"` pentru `open`. Astfel, se creează fișierul în directorul specificat
(directorul curent este implicit) sau se returnează o eroare dacă fișierul deja există:
```py
fNou = open("fisier_nou.txt", "x")
```

În cazul în care fișierul există, programul termină cu eroarea `FileExistsError`.

O metodă specială și ceva mai sigură de lucru cu fișiere este cea care folosește
instrucțiunea `with`, ca în exemplul de mai jos:
```py
with open("fisier_iesire.txt", "w") as f:
	f.write("Mesaj de scris în fișier")
```

Lucrul cu `with` are avantajul că închide automat fișierul cînd se iese din bucla
respectivă. În plus, din punct de vedere tehnic, leagă variabila `f` de fișier
doar în bucla respectivă (*scope*-ul variabilei este doar în bucla respectivă).

Acum, nu mereu avem nevoie să folosim *tot* conținutul unui fișier ca date de intrare.
Sau poate vrem să-l procesăm linie cu linie ori propoziție cu propoziție.
Pentru aceasta, în loc de metoda `read()`, avem alternative.

Metoda `readlines()` citește liniile din fișier și le salvează într-o listă, fiecare element
al listei fiind o linie din fișier. Dacă vrem să obținem apoi cuvintele din fiecare linie,
de exemplu, folosim metoda `split()`. Aceasta folosește drept separator implicit spațiul,
dar putem preciza separatorul, dacă vrem, de exemplu, să separăm după propoziții.
Iată un exemplu simplu:
```py
##### fisier.txt ########
# Ana are mere. Ion vrea
# să cumpere gutui.
#########################

with open("fisier.txt", "r") as f:
	linii = f.readlines()
	print(linii)				# ["Ana are mere. Ion vrea", "să cumpere gutui."]
	
	for linie in linii:
		print(linie)			# Ana are mere. Ion vrea
								# să cumpere gutui
	
	for linie in linii:
		cuv = linie.split()
		print(cuv)				# Ana
								# are
								# mere
								# ...etc...

	f.seek(0, 0)				# vezi detalii mai jos
	continut = f.read()
	propozitii = continut.split(".")
	print(propozitii)			# Ana are mere.
								# Ion vrea
								# să cumere gutui.
```

Puteți studia exemplul [aici](./exemple/propozitii.py)

**ATENȚIE:** Atunci cînd citim dintr-un fișier, cursorul rămîne la finalul fișierului.
Astfel, două instrucțiuni consecutive de citire nu vor produce rezultatul așteptat.
Prima instrucțiune citește, lasă cursorul la final (sau unde s-a terminat citirea),
iar a doua instrucțiune continuă citirea din punctul respectiv.
Pentru reluarea citirii se foloseste metoda `seek`. Aceasta acceptă două argumente:
- primul argument este numărul de poziții unde să se plaseze cursorul;
- al doilea argument precizează *referința*, adică față de ce poziție se calculează
  primul argument. Acesta poate fi:
  	+ `0` pentru începutul fișierului. Este valoarea folosită implicit și poate lipsi;
  	+ `1` înseamnă față de poziția curentă;
  	+ `2` înseamnă față de finalul fișierului.

Exemple:
```py
##### fisier.txt #######
# 1234567890
########################

with open("fisier.txt", "r") as f:
	patru = f.read(4)
	print(patru)			# 1234
	
	cinci = f.read(1)
	print(cinci)			# 5

	f.seek(-2, 1)			# EROARE (vezi mai jos)
	patruIar = f.read(1)
	print(patruIar)			# 4

	f.seek(-1, 2)
	zero = f.read(1)
	print(zero)				# 0

	f.seek(0)				# echivalent cu f.seek(0, 0)
	unu = f.read(1)
	print(unu)				# 1
```

**ATENȚIE:** Limbajul nu ne permite să folosim un offset negativ *față de poziția curentă*.
Astfel, funcția `f.seek(-2, 1)` va returna o eroare. Acest lucru se rezolvă folosind fișierul
deschis cu modul binar, adică `"rb"`. Dar atunci, fiecare rezultat va fi afișat sub forma
`b'1'`, ceea ce se rezolvă codificînd la loc cu formatul `utf-8`.

Puteți studia exemplul [aici](./exemple/seek.py).

Dacă nu mai știm unde ne aflăm în fișier, putem folosi metoda `tell()`, care afișează poziția
din fișier unde ne aflăm.

Mai multe detalii, de exemplu, [aici](https://pynative.com/python-file-seek/).

## Fișiere text ca argumente
Putem să precizăm fișierul cu care lucrăm la rulare, cu ajutorul argumentelor.
Situația funcționează similar cu variabilele de tip `argc` și `argv` din C.
Avem nevoie de modulul `sys`, care conține, printre altele, și lista
`argv`. Astfel, `sys.argv[0]` este numele programului, iar apoi urmează
argumentele date de la tastatură.

În varianta simplă, vom implementa un program care să precizeze la rulare
fișerul de intrare și cel de ieșire, astfel încît să-l putem rula cu
```sh
$ python program.py in.txt out.txt
```

Pentru aceasta, nu avem decît să începem programul cu:
```py
import sys

numeFisierIntrare = sys.argv[1]
numeFisierIesire = sys.argv[2]

# apoi le folosim cu metodele specifice de lucru cu fișiere
with open(numeFisierIntrare, "r") as inf:
	continut = inf.read()

	with open(numeFisierIesire, "w") as outf:
		outf.write(continut)
```

### Fișiere text ca argumente cu flag-uri
Putem fi și mai preciși, ca să facem rularea mai sugestivă. Astfel, putem folosi
flag-uri, care să precizeze care dintre argumente este fișierul de intrare și care
este cel de ieșire. Urmărim, deci, o rulare de forma:
```sh
$ python program.py -i intrare.txt -o iesire.txt
```

Sau, în varianta lungă:
```sh
$ python program.py --infile intrare.txt --outfile iesire.txt
```

Pentru aceasta, avem nevoie de modulul `getopt`, care ne permite să preluăm
argumentele într-o listă. Acest modul conține o funcție cu același nume
(deci se apelează cu `getopt.getopt()`) și este mai flexibil decît preluarea pur și simplu
în lista `sys.argv`, deoarece permite utilizarea flag-urilor scurte și a celor lungi
într-o manieră flexibilă.

Pentru a realiza cele de mai sus, atît în varianta scurtă, cît și în cea lungă, avem
o sursă de forma:
```py
import getopt
import sys

numeFisierIntrare = ""
numeFisierIesire = ""

# preluăm argumentele, mai puțin pe primul,
# care este numele programului
argv = sys.argv[1:]

# verificăm dacă s-au introdus argumentele corect
try:
	options, args = getopt.getopt(argv, "i:o:", ["infile = ", "outfile = "])
except:
	print("Nu ați introdus opțiunile corect.")

for i, v in options:
	if i in ['-i', '--infile']:
		numeFisierIntrare = v
	elif i in ['-o', '--outfile']:
		numeFisierIesire = v

print(f"Fișierul de intrare: {numeFisierIntrare}")
print(f"Fișierul de ieșire: {numeFisierIesire}")
```

În exemplul de mai sus, funcția `getopt.getopt()` primește următoarele argumente:
- lista din care să ia opțiunile (în cazul nostru, `argv`, care este `sys.argv[1]`);
- o listă de opțiuni scurte, apelate cu liniuță, *dar fără liniuță*. Lista se separă prin
  două puncte dacă sînt opțiuni care cer argument. Astfel, `i:o:` înseamnă că flag-urile
  `-i` și `-o` cer neapărat argument. Dacă aveam și un flag care nu cere argument, el se 
  preciza fără două puncte, de exemplu în forma `i:o:x`, deci un astfel de program putea fi rulat cu
  ```sh
  $ python program.py -i arg1 -o arg2 -x
  ```
- o listă de opțiuni lungi, apelate cu două liniuțe, *dar fără liniuțe* și precizate
  într-o listă cu sintaxa din exemplu (obligatoriu cu egal). Exemplul de mai sus
  înseamnă că programul acceptă argumente lungi de forma `--infile` și `--outfile`.

Funcția `getopt.getopt()` returnează perechi de forma `(argument, valoare)`,
pe care le prelucrăm ulterior.

Documentația oficială este [aici](https://docs.python.org/3/library/getopt.html).

### Fișiere text ca argumente în `config.json`
O variantă modernă pentru a transmite orice fel de argumente către un program
este să folosim fișiere de configurare. Formatul JSON este foarte popular și Python
include un parser destul de ușor de utilizat.

Astfel, soluția propusă este să creăm un fișier de configurare JSON care să conțină
orice argumente dorim, pe care apoi le preluăm în programul Python. Avem nevoie de modulele
`argparse` și `json`, dar într-o variantă minimală.

Atunci, nu avem decît să rulăm programul cu o comandă precum:
```sh
$ python program.py --config config.json
```
și va prelua automat configurația din fișierul `config.json`.

De exemplu, în `config.json` putem avea:
```json
{
	"infile": "path/to/fileIn.txt",
	"outfile": "path/to/fileOut.txt"
}
```

Iar apoi în Python vom scrie:
```py
import argparse
import json

# creăm un obiect de tip parser al argumentelor
parser = argparse.ArgumentParser(description="")

# precizăm ce fel de argumente pot apărea, în varianta scurtă sau lungă
parser.add_argument("-c", "--config", required=False, default="config.json", help="Fișierul de configurare")

# salvăm argumentele într-o listă
args = parser.parse_args()

# verificăm dacă am preluat configurarea
# și o încărcăm în caz afirmativ
if args.config:
	with open(args.config, "r") as f:
		config = json.load(f)
# altfel, am folosit valoarea default
else:
	print("Am folosit valoarea default, config.json")
	with open("config.json", "r") as f:
		config = json.load(f)

# acum avem acces la toate opțiunile din fișierul json
# sub formă de dicționar
numeFisierIntrare = config["infile"]
numeFisierIesire = config["outfile"]
```

În exemplul de mai sus, `args` este un parser, care are atîtea opțiuni cîte precizăm
prin `add_argument`. Astfel, am adăugat doar opțiunea `-c` sau `--config`, deci de aceea
putem apela `args.config`.

Documentația oficială este [aici](https://docs.python.org/3/library/argparse.html).

## Funcții matematice uzuale
Acestea se găsesc în modulul `math`, a cărui documentație este [aici](https://docs.python.org/3/library/math.html).

Cîteva exemple, precum și utilizarea lor găsiți în exercițiile rezolvate de mai jos.

## Exerciții rezolvate
- [calculator simplu care exemplifică funcții matematice](./exemple/mate.py);