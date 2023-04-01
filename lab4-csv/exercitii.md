# Exerciții

## Ușoare
Scrieți în fișiere CSV:

1. Primele 10 numere naturale pe o linie și pătratele lor pe a doua linie:

```csv
1,2,3,4,5,6,7,8,9,10
1,4,9,16,25,36,49,64,81,100
```

2. Primele 10 numere naturale pe o linie și lista inversată pe linia a doua:

```csv
1,2,3,4,5,6,7,8,9,10
10,9,8,7,6,5,4,3,2,1
```

3. Primele 10 numere naturale pe o linie și primele 10 numere prime pe linia a doua:

```csv
1,2,3,4,5,6,7,8,9,10
2,3,5,7,11,13,17,19,23,29
```

4. Primele 10 numere naturale pe o linie și suma lor, ca acumulator, pe linia a doua:

```csv
1,2,3,4,5,6,7,8,9,10
1,3,6,10,15,21,28,36,45,55
```

5. Citiți de la tastatură `n` și `l` și scrieți într-un fișier CSV `l` linii de `n` numere aleatorii între 1 și 100.

Exemplu:

```
n = 3
l = 5

31,64,11
4,65,12
45,66,11
53,6,1
4,29,41
```

*Indicație:* Pentru numere aleatorii, folosiți modulul `random` și funcția `random.randint(a,b)`, care returnează un întreg aleatoriu în intervalul `[a,b]`.

```python
import random

x = random.randint(1,100)       # x = 14, ales aleatoriu între 1 și 100 (inclusiv)
```

6. Citiți din fișierul CSV de la exercițiul 5 și afișați într-un alt fișier maximul de pe fiecare linie.

---

## Medii

Scrieți în fișiere CSV:

1. 10 numere aleatorii între 1 și 100 pe prima linie și literele din alfabet care corespund pozițiilor respective pe linia a doua.
2. 10 numere aleatorii între 1 și 100 pe prima linie și pe a doua linie, 0 dacă numărul de deasupra este par și 1, dacă este impar.
3. 10 numere aleatorii între 1 și 100 pe prima linie și pe linia a doua, 0 dacă numărul de deasupra este prim și 1, dacă este compus.
4. Conținutul:
```csv
1,2,3,4,5,6,7,8,9,10
1,2,3,4,5,6,7,8,9
1,2,3,4,5,6,7,8
1,2,3,4,5,6,7
1,2,3,4,5,6
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1
```
5. Citiți de la tastatură `bilete` și afișați, pe prima linie, un număr de `bilete` care conțin numere aleatorii și unice între 1 și 49.
6. Adăugați o linie goală, apoi încă o linie la fișierul de la exercițiul 5 corespunzător unei extrageri: o listă de 6 numere aleatorii între 1 și 49, apoi afișați pe ecran cîte numere a ghicit fiecare bilet.
Exemplu:
```csv

bilete.csv
3,5,6,19,45,1
35,34,12,4,5,6
24,32,14,9,3,1

3,5,6,9
```

Se afișează pe ecran:

```
Jucătorul 1 a ghicit 3 numere.
Jucătorul 2 a ghicit 2 numere.
Jucătorul 3 a ghicit 2 numere.
```

7. Îmbunătățiți exercițiul anterior astfel:
- să se afișeze un fel de log într-un fișier separat (biletele, numerele extrase, numărul de numere ghicite și care sînt acelea);
- să se reia extragerea pînă cînd cel puțin un jucător nimerește cel puțin 4 numere.

8. Populați un fișier CSV cu `l` linii și `c` coloane, conținînd numere aleatorii de la 1 la 100. Citiți de la tastatură `n` și afișați linia `n` și coloana `n`.