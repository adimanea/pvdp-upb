## Exerciții
Scopul acestui curs & laborator este să vă familiarizați cu noul mod de lucru.
Astfel că principala cerință va fi să lucrați exemple simple în noul format,
folosind cît mai multe elemente.

De exemplu, **elemente de bază**:
- asigurați-vă că ați instalat corect Jupyter;
- creați o foaie de lucru `ipynb`;
- introduceți un bloc de text și „rulați-l“ cu `Shift + Enter` (exemplu `Test bloc text.`);
- introduceți un bloc de cod și rulați-l cu `Shift + Enter` (exemplu `print("Salut!")`).

Apoi, **elemente intermediare**:
- folosiți cît mai multe tipuri de conținut în blocul text:
  + heading (titlu, subtitlu etc., cu sintaxa `# Titlu` pentru titlu, `## Subtitlu` pentru subtitlu etc.);
  + text **bold**, cu sintaxa `**text**`;
  + text *italic*, cu sintaxa `*text*`;
  + text `preformatat`, stil cod, cu sintaxa `` `text` ``;
  + [link](https://tcsi.ro/), cu sintaxa `[text](URL)`;
  + liste numerotate și nenumerotate;
- blocurile de cod să facă unele calcule simple: 
  + afișați toți multiplii de 13 de la 1 la 100;
  + afișați numerele prime de la 1 la 100;
  + afișați toate pătratele perfecte de la 1 la 1000.
  + afișați toate numerele prime dintr-un interval `[a,b]`, cu capetele citite de la tastatură (puteți folosi `input()` într-un bloc de cod);
  + afișați 10 numere aleatorii *diferite* între 1 și 100.

---

## Exerciții suplimentare (13 aprilie 2022)
Rezolvați toate exercițiile de mai jos într-o singură foaie Jupyter cu titlul (heading 1): `Exerciții în Jupyter`.

- scrieți un bloc Markdown care să conțină ca titlu (heading 2) `Exercițiul 1: Lucrul cu text`;
- în același bloc Markdown introduceți un citat (blockquote) de pe Wikipedia și introduceți-i sursa cu un link de tipul [link](https://en.wikipedia.org/wiki/James_Rumsey_Monument);
- scrieți un bloc Markdown care să conțină descrierea: Codul de mai jos numără caracterele din citatul de mai sus;
- scrieți un bloc Python care să preia de la tastatură sau dintr-un fișier citatul din bloc și să afișeze cîte caractere conține; executați blocul și afișați rezultatul;
- scrieți încă un bloc Markdown care să conțină descrierea: Codul de mai jos numără aparițiile unui caracter introdus de la tastatură din citatul de mai sus. *Varianta non-case-sensitive*;
- scrieți un bloc Python care să rezolve cerința și să afișeze rezultatul;
- scrieți încă un bloc Markdown care să conțină descrierea: **Varianta case-sensitive**;
- scrieți un bloc Python care să rezolve cerința.

---

- scrieți un bloc Markdown care să conțină ca titlu (heading 2) `Exercițiul 2: Lucrul cu numere prime`;
- în același bloc Markdown introduceți un tabel cu 2 coloane, de forma:

| Număr `n` | Al `n`-lea număr prim |
|-----------|-----------------------|
| 1         | 2                     |
| 2         | 3                     |
| 3         | 5                     |
| 4         | 7                     |
| 5         | 11                    |

- scrieți un bloc Markdown care să conțină descrierea: Codul de mai jos afișează primele `n` numere prime, cu `n` citit de la tastatură;
- scrieți un bloc Python care să rezolve cerința.

---

- scrieți un bloc Markdown care să conțină ca titlu (heading 2) `Exercițiul 3: Loto 6/49`;
- în același bloc Markdown introduceți o imagine sugestivă pentru o loterie, precum ![img_6.png](img_6.png);
- scrieți un bloc Markdown care să conțină descrierea: Codul de mai jos vă permite alegerea a 6 numere de la 1 la 49, apoi face o extragere aleatorie și afișează cîte numere ați ghicit;
- scrieți un bloc Python care să rezolve cerința:
  - citiți de la tastatură 6 numere de la 1 la 49 și le salvați într-o listă `jucator`;
  - faceți o extragere de 6 numere diferite de la 1 la 49 (folosind modulul `random` și funcția `random.randint(1, 49)`) și le salvați într-o listă `extragere`;
  - verificați cîte numere din lista `jucator` se găsesc în lista `extragere`;

---

- scrieți un bloc Markdown care să conțină ca titlu (**heading 3**) `Exercițiul 4: Mai multe bilete, mai multe șanse de cîștig!`;
- scrieți un bloc Markdown care să conțină descrierea: Codul de mai jos vă permite să jucați mai multe seturi de numere, salvate într-un fișier și afișează cîte numere ați ghicit la fiecare bilet. Exemplu:
```
inFile.txt
----------------
1 5 7 31 44 14
41 22 5 33 23 11
11 12 13 6 4 31

OUTPUT:
--------------------------
Extragere: 5 7 31 22 32 21
Bilet 1: 3 ghicite
Bilet 2: 1 ghicit
Bilet 3: 1 ghicit

```
- scrieți un bloc Python care să rezolve cerința:
  - salvați într-un fișier un număr (> 1) de seturi de cîte 6 numere, de la 1 la 49;
  - preluați numerele din fișier într-o singură listă, cu toate biletele, pe care o spargeți în liste de cîte 6 elemente, cîte o listă pentru fiecare bilet;
  - realizați o extragere folosind `random.randint(1, 49)`;
  - verificați cîte numere extrase se găsesc în fiecare dintre listele corespunzătoare biletelor;
  - **Puncte bonus dacă refolosiți elemente (funcții, variabile) din blocul anterior, fără a le copia, evident.**

---

## Exerciții suplimentare (20 aprilie 2022)
Rezolvați toate exercițiile de mai jos într-o singură foaie Jupyter cu titlul (heading 1): `Exerciții în Jupyter 20 aprilie`.

- scrieți un bloc Markdown cu titlul (heading 2): `Ghicește numărul!`;
- scrieți un bloc Markdown care să conțină descrierea: Codul de mai jos alege un număr aleatoriu între 1 și 100, apoi vă dă posibilitatea de a-l ghici din 10 încercări. Dacă introduceți un număr mai mare decît cel ales, se afișează mesajul `Prea mare!`, iar dacă introduceți un număr mai mic decît cel ales, se afișează mesajul `Prea mic!`. Jocul oferă posibilitatea de a renunța oricînd, dacă se introduce caracterul `q` sau `Q`. La finalul jocului se afișează numărul ales. Exemplu de output:
```
Ghicește numărul!
Încercarea 1: 5
Prea mic!
Încercarea 2: 30
Prea mic!
Încercarea 3: 58
Prea mare!
Încercarea 4: 44
Prea mare!
Încercarea 5: q
Ai renunțat după 5 încercări. Numărul ales era 41.
```
- scrieți un bloc Python care să rezolve cerința:
  + generați numărul folosind `random.randint(1, 100)` și salvați-l într-o variabilă;
  + "gameplay"-ul va fi o buclă cu condiția de ieșire `nrIncercari < 10`;
  + testați input-ul pentru early quit (e.g. `if input(f"Încercarea {nrIncercari}: ").lower() == 'q': break`);
  + pentru condiția de mai sus aveți nevoie să preluați numărul de intrare ca `string`! Deci folosiți `input()`, nu `int(input())` și îl convertiți în `int` doar dacă nu este `q/Q`.

---

- scrieți un bloc Markdown cu titlul (heading 2): `Zaruri`;
- scrieți un bloc Markdown care să conțină descrierea: Codul de mai jos joacă zaruri. Computerul aruncă 2 zaruri și se afișează rezultatul și suma punctelor de pe cele două zaruri. Apoi aruncă și pentru dumneavoastră și se afișează rezultatul și suma punctelor de pe cele două zaruri. Cîștigă jucătorul cu suma mai mare. Exemplu de output:
```
Să jucăm zaruri!
CPU zar 1: 4
CPU zar 2: 6
CPU total: 10
DVS zar 1: 5 (apăsați Enter)
DVS zar 2: 2
DVS total: 7
CPU cîștigă.
```
- scrieți un bloc Python care să rezolve cerința:
  + generați pe rînd două numere folosind `random.randint(1, 6)` pentru zarurile CPU;
  + calculați-le suma și salvați-o;
  + generați pe rînd două numere folosind `random.randint(1, 6)` pentru zarurile DVS;
  + calculați-le suma și salvați-o;
  + comparați suma DVS cu suma CPU și afișați mesajul corespunzător.

---

- scrieți un bloc Markdown cu titlul (heading 2): `Mai multe zaruri, mai multe runde`;
- scrieți un bloc Markdown care să conțină descrierea: Codul de mai jos îmbunătățește jocul de zaruri cu următoarele modificări:
  + se permite alegerea numărului de zaruri;
  + se acordă punctaj pe rundă și se oferă posibilitatea jucătorului să continue;
  + se afișează scorul final și numărul de runde.
Exemplu de output:
```
Să jucăm zaruri!
RUNDA 1
--------------------
Numărul de zaruri: 4
CPU zar 1: 4
CPU zar 2: 2
CPU zar 3: 2
CPU zar 4: 5
CPU total: 13
DVS zar 1: 4 (apăsați Enter)
DVS zar 2: 4 (apăsați Enter)
DVS zar 3: 3 (apăsați Enter)
DVS zar 4: 1
DVS total: 12
CPU cîștigă.
CPU 1 - DVS 0
Mai jucați (d/n): d
RUNDA 2
---------------------
CPU zar 1: 5
CPU zar 2: 3
CPU zar 3: 6
CPU zar 4: 2
CPU total: 16
DVS zar 1: 5 (apăsați Enter)
DVS zar 2: 4 (apăsați Enter)
DVS zar 3: 5 (apăsați Enter)
DVS zar 4: 2
DVS total: 16
Egalitate.
CPU 2 - DVS 1
Mai jucați (d/n): n
Ați jucat 2 runde.
Scorul final CPU 2 - DVS 1.
CPU cîștigă.
```
- scrieți un bloc Python care să rezolve cerința.

**La toate exercițiile se acordă puncte bonus dacă optimizați sau folosiți condiții de validare a datelor.**

---

## Exercițiu complet

Creați o foaie Jupyter care să conțină în formatare Markdown exemplul [de aici](./ex_md.md).

Adăugați la final și blocul Python care rezolvă problema.