# Exerciții Laborator 2

## Ușoare
1. Scrieți un program care să citească dintr-un fișier 10 numere și să afișeze maximul lor.
2. Scrieți un program care să citească dintr-un fișier 10 cuvinte și să afișeze cîte vocale conțin în total.
3. Scrieți un program care să citească de la tastatură un caracter, apoi să afișeze pe ecran după cîte poziții a găsit acela caracter într-un text dintr-un fișier.
4. Scrieți un program care să citească de la tastatură un număr natural `n`, apoi dintr-un fișier o listă de 10 numere și să scrie într-un alt fișier numerele reprezentînd `n %` din numerele din fișierul de intrare.
5. Scrieți un program care citește de la tastatură două cuvinte, `nume` și `extensie`, apoi creează un fișier în directorul curent de tipul `nume.extensie`.
6. Scrieți un program care citește de la tastatură un număr natural `n`, apoi scrie într-un fișier toate numerele *impare* de la `1` la `n`.
7. Scrieți un program care citește de la tastatură un număr natural `n`, apoi scrie într-un fișier `n` numere aleatorii, între 1 și 1000.
8. Scrieți un program care citește de la tastatură un caracter `c` și un număr `n`, apoi scrie într-un fișier caracterul `c` de `n` ori (a) pe aceeași linie (b) cîte un caracter pe linie.
9. Scrieți un program care citește dintr-un fișier două numere `a` și `b`, apoi scrie într-un alt fișier un număr aleatoriu între `a` și `b`.
10. Scrieți un program care citeste dintr-un fișier trei numere `a`, `b` și `n`, apoi scrie într-un alt fișier `n` numere aleatorii între `a` și `b`.

## Medii
1. Scrieți un program care să citească de la tastatură un număr natural `n`, să scrie într-un fișier `n` numere aleatorii între 1 și 1000 și să afișeze pe ecran maximul lor.
2. Scrieți un program care să se execute cu două argumente (de tipul `argv`), care să fie un caracter și un fișier text, apoi să afișeze pe ecran de cîte ori apare caracterul respectiv în fișierul respectiv.
3. Scrieți un program care să citească de la tastatură `n`, apoi dintr-un fișier `n` numere naturale și să afișeze pe ecran `cmmdc` al celor `n` numere.
4. Scrieți un program care să citească numerele (pînă la finalul fișierului) dintr-un fișier denumit `expIn.txt` și să scrie într-un fișier denumit `expOut.txt` exponențialele numerelor din primul fișier.
5. Scrieți un program care să citescă de la tastatură `n`, apoi să scrie într-un fișier `n` numere naturale între 2 și 1000, apoi să scrie într-un alt fișier numerele prime dintre cele generate, precum și cîte procente reprezintă ele din totalul numerelor generate.
6. Scrieți un program care citește de la tastatură un număr natural `n`, apoi scrie într-un fișier primele `n` numere prime.
7. Scrieți un program care:
	- citește de la tastatură `n`, `a`, `b`;
	- scrie într-un fișier `n` numere naturale generate aleatoriu între `a` și `b`;
	- scrie într-un alt fișier numerele prime din fișierul de mai sus.
8. Scrieți un program care generează un caracter aleatoriu `c`, apoi afișează pe ecran de cîte ori apare caracterul respectiv într-un text salvat într-un fișier de intrare (a) case sensitive (exemplu: dacă `c = a`, se afișează numărul de apariții ale lui `a` și numărul de apariții ale lui `A`) (b) case insensitive (se afișează suma aparițiilor caracterului cu minusculă și cu majusculă). Indicație: Puteți folosi o listă `alfabet = ['a', 'b', 'c', 'd', ..., 'z']` sau un `string` `alfabet = "abcdefghijklmnopqrstuvwxyz` și generați un număr aleatoriu între 0 și 25, apoi preluați caracterul de pe poziția respectivă.
9. Scrieți un program care scrie într-un fișier un număr aleatoriu `x` între 1 și 1000, apoi preia de la tastatură un număr natural `n` și încearcă să ghicească numărul `x`, aleatoriu, din `n` încercări (adică generează `n` numere diferite și le testează dacă sînte egale cu `x`). Se afișează pe ecran dacă s-a ghicit numărul `x`, din cîte încercări sau dacă nu s-a ghicit, un mesaj corespunzător (e.g. `Nu s-a ghicit`).
10. Scrieți un program care scrie într-un fișier 10 numere aleatorii între 1 și 1000, apoi citește de la tastatură o opțiune `s, d, p, c`, pentru sumă, diferența, produs, cît și afișează într-un alt fișier calculul corespunzător: suma numerelor din primul fișier, diferența, produsul sau cîtul lor.

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
