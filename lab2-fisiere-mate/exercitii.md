# Exerciții Laborator 2

## Ușoare
1. Scrieți un program care să citească dintr-un fișier 10 numere și să afișeze maximul lor.
2. Scrieți un program care să citească dintr-un fișier 10 cuvinte și să afișeze cîte vocale conțin în total.
3. Scrieți un program care să citească de la tastatură un caracter, apoi să afișeze pe ecran după cîte poziții a găsit acela caracter într-un text dintr-un fișier.
4. Scrieți un program care să citească de la tastatură un număr natural `n`, apoi dintr-un fișier o listă de 10 numere și să scrie într-un alt fișier numerele reprezentînd `n %` din numerele din fișierul de intrare.
5. Scrieți un program care citește de la tastatură două cuvinte, `nume` și `extensie`, apoi creează un fișier în directorul curent de tipul `nume.extensie`.

## Medii
1. Scrieți un program care să citească de la tastatură un număr natural `n`, să scrie într-un fișier `n` numere aleatorii între 1 și 1000 și să afișeze pe ecran maximul lor.
2. Scrieți un program care să se execute cu două argumente (de tipul `argv`), care să fie un caracter și un fișier text, apoi să afișeze pe ecran de cîte ori apare caracterul respectiv în fișierul respectiv.
3. Scrieți un program care să citească de la tastatură `n`, apoi dintr-un fișier `n` numere naturale și să afișeze pe ecran `cmmdc` al celor `n` numere.
4. Scrieți un program care să citească numerele (pînă la finalul fișierului) dintr-un fișier denumit `expIn.txt` și să scrie într-un fișier denumit `expOut.txt` exponențialele numerelor din primul fișier.
5. Scrieți un program care să citescă de la tastatură `n`, apoi să scrie într-un fișier `n` numere naturale între 2 și 1000, apoi să scrie într-un alt fișier numerele prime dintre cele generate, precum și cîte procente reprezintă ele din totalul numerelor generate.

## Grele
1. Scrieți un program care să se execute asupra fișierului text reprezentat de sursa programului însuși și să afișeze cuvîntul (de cel puțin 2 litere) care apare cel mai des în sursă.
2. Scrieți un program care să se execute folosind un fișier de configurare JSON, în care să se specifice (cel puțin):
	- un fișier text de intrare;
	- dacă programul lucrează case sensitive sau nu;
	- o listă de caractere
și să afișeze cît la sută reprezintă caracterele din listă din textul complet din fișier.
3. Refaceți programul [punct.py](./exemple/punct.py) *fără a folosi* `math.dist`. Practic, implementați manual distanța euclidiană între două puncte de dimensiuni cunoscute.
4. Scrieți un program care citește de la tastatură un număr natural `k`, apoi aplică cifrul Caesar de cheie `k` pe textul dintr-un fișier dat, scriind textul codat într-un alt fișier text. *Se vor ignora semnele de punctuație, dar se va ține cont de majuscule.*
5. Scrieți un program care:
	- se rulează cu 3 argumente numerice, `a`, `b`, `n` (exemplu `$ python program.py 2 1023 2000`);
	- folosește un fișier de configurare JSON, care specifică numele și calea către un fișier de intrare, unul de ieșire și un interval de tipul `[min, max]`;
	- generează `n` numere naturale aleatorii între `min` și `max` și le scrie în fișierul de intrare;
	- scrie în fișierul de ieșire numerele prime din fișierul de intrare, care se află între `a` și `b`;
	- afișează pe ecran cel mai mare dintre aceste numere prime.

-------

**La toate exercițiile se primesc bonusuri dacă se prevăd condiții de validare a datelor.**