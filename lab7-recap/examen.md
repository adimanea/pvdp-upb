# Examen Java și Software Matematic
# 15-17 iunie, 2021

Rezolvați, din exercițiile de mai jos, la alegere, astfel încît
să totalizați maximum 2 puncte din fiecare secțiune.

Pentru exercițiile Python, le puteți rezolva în fișiere individuale `.py`
sau în cîte o foaie Jupyter sau pe toate într-o singură foaie Jupyter.

**Exercițiile rezolvate peste punctaj se vor ignora. Se acordă, însă, punctaje parțiale pe exerciții (nu vor fi notate doar cu 0 sau maxim).**

Pentru rezolvarea oricărui exercițiu, se pot folosi fie metodele, modulele și bibliotecile
studiate la curs și laborator, fie oricare altele, cu condiția ca studentul să poată
explica detaliat eventual, la evaluarea orală, funcționarea programului.

## Python, secțiunea 1: Calcule

P1.1. **(0.5p)** Citiți de la tastatură un număr întreg pozitiv `n` și afișați
o listă de `n` numere, astfel `[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ...]`.
Includeți condiții de validare a datelor.

Exemplu: Pentru `n = 3` se afișează `[1, 2, 2]`. Pentru `n = 7`,
se afișează `[1, 2, 2, 3, 3, 3, 4]`.

P1.2. **(1p)** Citiți de la tastatură un număr `n`, o listă de `n` persoane
și un număr `c`. Afișați persoanele din listă circular, din `c` în `c`. Numărătoarea
se consideră 1-indexată. Includeți condiții de validare a datelor.

Exemplu:

```
IN: n = 5
IN: Ana
IN: Ionel
IN: Maria
IN: George
IN: Cristi
IN: c = 3
OUT: Maria
OUT: Ana
OUT: George
OUT: Ionel
OUT: Cristi
```

P1.3. **(2p)** Doi jucători dau cu 2 zaruri. Cîștigă jucătorul care
dă o dublă în cele mai puține aruncări. Aruncarea zarurilor se va realiza folosind
modulul `random` și se contorizează numărul de aruncări pînă la realizarea unei duble.

Exemplu:

```
- Jucătorul 1, aruncarea 1: [3, 5]
- Jucătorul 1, aruncarea 2: [1, 5]
- Jucătorul 1, aruncarea 3: [2, 2]
- Jucătorul 1 a dat o dublă din 3 aruncări.
- Jucătorul 2, aruncarea 1: [5, 1]
- Jucătorul 2, aruncarea 2: [3, 5]
- Jucătorul 2, aruncarea 3: [4, 5]
- Jucătorul 2, aruncarea 4: [1, 1]
- Jucătorul 2 a dat o dublă din 4 aruncări.
- Jucătorul 1 a cîștigat.
GAME OVER
```

Opțional, dacă se atinge numărul de aruncări ale primului jucător și jucătorul 2 nu a dat dublă,
jocul deja se termină. Astfel, la aruncarea 3, deoarece jucătorul 2 nu a dat dublă,
deja s-a terminat jocul.

P1.4. **(1p)** Se citește de la tastatură un număr `n` (cel puțin egal cu 1000) și se afișează
ce factori primi are în descompunere, care apar la putere mai mare decît 1. Se afișează apoi
numărul liber de pătrate rezultat, adică compus din factorii primi ai lui `n`, fiecare la puterea 1.

Exemplu: `n = 1000`, se afișează `1000 are factorul 2 la puterea 3 și factorul 5 la puterea 3`.
Se afișează apoi `Numărul liber de pătrate rezultat este 2 * 5 = 10`.

Alt exemplu: `n = 7000`, se afișează `6000 are factorul 2 la puterea 3 și factorul 5 la puterea 3`.
Se afișează apoi `Numărul liber de pătrate rezultat este 2 * 5 * 7 = 70`.

P1.5. **(1p)** Citiți de la tastatură `n` și afișați primele `n` sume ale lui Gauss, cu tot cu valoarea lor.

Exemplu:

```
n = 4
1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
```

P1.6. **(2p)** Se generează aleatoriu o listă `numere` de 1000 numere întregi, între 100 și 1000.
Se extrag din listă doar numerele care apar o singură dată și se salvează într-o listă, `unice`.
Se generează o listă de ponderi întregi între 0 și 10, de lungime egală cu lungimea listei `unice`,
numită `ponderi_unice`.
Să se afișeze:
- media aritmetică a valorilor din lista `unice`;
- media ponderată a valorilor din lista `unice`, cu ponderile din `ponderi_unice`;
- mediana listei `unice`;
- modul/modurile listei `unice`;
- abaterea medie pătratică a listei `unice`.

## Python, secțiunea 2: Grafice

**Observație:** Dacă nu se precizează explicit, puteți folosi orice setări vizuale 
pentru grafice (culoare, opacitate, stilul liniei etc.). Dacă există o precizare explicită, 
(ne)respectarea ei va fi (de)punctată.

P2.1. **(2p)** Generați aleatoriu o listă de 1000 de numere întregi, între 1 și 100.
Salvați, apoi, în variabile diferite, numărul de numere din listă:
- divizibile cu 3, de exemplu în variabila `div3`;
- divizibile cu 5, de exemplu în variabila `div5`;
- divizibile cu 3 și cu 5, de exemplu în variabila `div35`;
- divizibile cu 3, dar nu cu 5, de exemplu în variabila `div3n5`;
- prime, de exemplu în variabila `prime`.

Reprezentați apoi printr-un grafic de tip "bar", cu bare negre de opacitate 25%, aceste variabile.
Pe axa OX veți avea etichetele `[div3, div5, div35, div3n5, prime]`, iar pe axa OY, valorile acestor variabile.

P2.2. **(2p)** Generați aleatoriu o listă de 1000 de numere întregi, între 1 și 100.
Salvați, apoi, în variabile diferite, numărul de numere din listă care sînt pătrate perfecte
(de exemplu, în variabila `pp`) și numărul de numere din listă care nu sînt pătrate perfecte
(de exemplu, în variabila `nopp`). Reprezentați apoi, folosind un grafic de tip "pie chart",
procentul reprezentat de `pp` și `nopp` din numărul total de numere.

Plasați și legenda graficului, precum și etichetele și valorile pe feliile graficului.

P2.3. (**NOTA 10**) Se dă funcția `f(x) = x**3 + sin(x)**3`.
- **(1p)** Reprezentați-o grafic, cu linie roșie, de opacitate 23%, pe domeniul `[-4, 4]`, folosind cel puțin 100 de puncte;
- **(1p)** Folosind același domeniu, trasați graficul funcției `g(x) = sin(x)`, cu o linie verde, de opacitate 80%;
- **(1p)** Găsiți coordonatele punctelor de intersecție între cele două grafice și afișați-le, pentru intervalul `[-4, 4]`.