# Elemente de statistică

Ne concentrăm acum pe cîteva calcule statistice simple, pe care le vom face
cu ajutorul [fișierelor CSV](../lab4-csv/README.md), iar data viitoare le vom
vizualiza grafic.

Funcțiile statistice pe care le calculăm vor putea fi implementat fie manual,
fie folosind o bibliotecă Python.

## Calcule elementare
Să presupunem că avem un set de date de forma `(X, Y)` sau, mai general, un n-tuplu
de forma `(X1, X2, X3, ..., Xn)`. Vom calcula:
- media sau media aritmetică (eng. "mean" sau "average");
- media ponderată (eng. "weighted average");
- mediana (eng. "median");
- abaterea standard (eng. "standard deviation");
- modul (eng. "mode").

Mai jos, definițiile:
- **media aritmetică** se calculează prin raportul între suma valorilor și numărul lor. Astfel, în pseudocod, dacă avem o listă de forma `l = [x1, x2, ..., xn]`, atunci:
```
media_aritmetica = (x1 + x2 + ... + xn) / n
```
- **media ponderată**, cu ponderi `p1, p2, p3, ... pn` se calculează cu formula:
```
media_ponderata = (x1 * p1 + x2 * p2 + ... + xn * pn) / (p1 + p2 + p3 + ... + pn)
```
- **mediana** este valoarea care apare în mijlocul setului de date. Dacă avem un număr impar de date, atunci este chiar valoarea din mijloc. Dacă avem un număr par, atunci se ia media aritmetică a celor două valori din mijloc. De exemplu, pentru setul `[1, 2, 3, 4, 5]`, mediana este `3`, fiind valoarea din mijloc. Dar pentru setul `[1, 2, 3, 4, 5, 6]`, mediana este `(3 + 4) / 2 = 3.5`;
- **modul** este valoarea care apare cel mai frecvent. Dacă există o singură astfel de valoare, setul se numește *unimodal*. Dacă există mai multe cu același număr maxim de apariții, setul se numește *multimodal*:
  + modul setului `[1, 2, 3, 3, 4, 5]` este `3`, setul fiind unimodal;
  + modurile setului `[1, 2, 3, 3, 4, 4, 5]` sînt `3` și `4`, setul fiind multimodal (bimodal, mai precis);
- **abaterea standard** sau **abaterea medie pătratică**, notată de obicei cu `sigma` se calculează folosind media aritmetică. Dacă avem un set de date `[x1, x2, ..., xn]`, care are media egală cu `media`, atunci `sigma` este:
```
sigma = sqrt( ( (x1 - media)^2 + (x2 - media)^2 + ... + (xn - media)^2 ) / n )
```

## Exemplu
Fie setul `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`:
- media este 5.5;
- dacă avem, de exemplu, ponderile `1, 2, 0, 0, 0, 0, 1, 2, 0, 0`, atunci media ponderată este 4.67;
- mediana este 5.5;
- modul nu există (sau fiecare valoare este un mod);
- abaterea standard este 2.8722.

## Verificare Excel
Valorile pot fi verificate folosind Excel (sau Google Sheets sau LibreOffice) și formulele:
- `AVERAGE` este formula pentru medie (e.g. `AVERAGE(A1:A10)`);
- media ponderată se calculează cu o combinație de `SUMPRODUCT` și `SUM`. Dacă avem, de exemplu, valorile stocate în celulele `A1:A10` și ponderile în celulele `B1:B10`, atunci:
    + `SUMPRODUCT(A1:A10, B1:B10)` calculează suma produselor între valori și ponderi;
    + `SUM(B1:B10)` calculează suma ponderilor;
    + `SUMPRODUCT(A1:A10, B1:B10) / SUM(B1:B10)` calculează media ponderată;
- `MEDIAN` returnează mediana (e.g. `MEDIAN(A1:A10)`);
- `MODE.MULT` returnează modul, dacă există, sau `N/A` dacă nu există (e.g. `MODE.MULT(A1:A10)`);
- `STDEV.P` returnează abaterea standard (e.g. `STDEV.P(A1:A10)`).

## Calcule directe folosind funcții Python
Avem nevoie de bibliotecile `statistics` și `numpy`. Apoi, funcțiile sînt cele de mai jos. Putem redenumi
o bibliotecă atunci cînd o importăm, pentru a o folosi mai scurt. În exemplul următor, biblioteca `statistics`
o redenumim simplu `stat`, iar `numpy`, `np`.
```python
import random
import statistics as stat
import numpy as np

# generăm un set de numere aleatorii între 1 și 10
# setul avînd un număr aleatoriu de elemente, între 100 și 1000
count = random.randint(100, 1000)
date = [random.randint(0, 10) for i in range(count)]

# funcțiile statistice
media = stat.mean(date)
mediana = stat.median(date)
modul = stat.multimode(date)
sigma = stat.stdev(date)

# generăm o listă de ponderi între 0 și 1 (zecimale)
ponderi = [random.random() for _ in range(count)]
# calculăm media ponderată, cu funcția specifică din numpy
media_ponderata = np.average(date, weights=ponderi)

print(f"Media este {media}, mediana este {mediana}, modul este {modul}, abaterea standard este {sigma}")
print(f"Media ponderată este {media_ponderata}")
```

Un exemplu mai sofisticat, care să folosească și datele dintr-un fișier CSV, [aici](exemplu-statistica.ipynb).

## Exerciții
1. Creați un set de date aleatoriu, pe care să calculați toate funcțiile statistice, în 2 moduri: manual și cu funcții Python. Prevedeți și cazurile cînd avem un număr par de date, și cel în care avem un număr impar de date. Lista de ponderi o puteți genera aleatoriu, de exemplu cu valori între 0 și 1 (folosind `random.random()`).
2. Folosiți datele dintr-un fișier CSV, creat manual sau descărcat de pe Internet și repetați exercițiul de mai sus, pentru datele numerice din una sau mai multe coloane. Opțional, verificați calculele folosind fișierul CSV în Excel, Google Sheets sau o alternativă.