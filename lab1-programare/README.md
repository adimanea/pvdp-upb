# Laborator 1: Paradigme de programare și aplicații în Python

În această lecție, vom introduce (foarte) pe scurt paradigmele de programare
și vom începe să învățăm Python. Studenții avansați pot sări direct la
[**exercițiile**](./exercitii.md) medii sau grele.

## Introducere
O *paradigmă de programare* este o caracteristică prin care se pot
clasifica limbajele de programare, în funcție de modul în care se
exprimă programele scrise folosind limbajele respective.

Așa cum într-un limbaj natural avem propoziții și fraze de mai multe
feluri (enunțiative, interogative, exclamative etc.), la fel și în
cazul limbajelor de programare putem exprima același lucru în mai multe
moduri.

Ca o mică paranteză teoretică, trebuie ținut cont de faptul că orice limbaj
(fie el natural sau de programare) are două componente fundamentale:
*sintaxa* și *semantica*. Prima se ocupă cu „aspectul“ limbajului, cu regulile
după care se pot forma cuvintele, în sens general, iar cea de-a doua, cu
sensul acestor cuvinte.

Astfel, de exemplu, în limbajul de programare C++, expresia `itn x;` folosită
pentru a declara o variabilă întreagă `x` este *greșită sintactic*, deoarece
cuvîntul `itn` nu este acceptat de compilator (așteptînd, de fapt, `int`).
Iar expresia `x++;` este corectă sintactic, avînd *semantica* de incrementare
a valorii stocate în variabila `x` cu o unitate.

În limbajul natural, de exemplu, în limba română, cuvîntul `x12` este greșit,
pentru că sintaxa limbii române nu permite și litere, și cifre într-un cuvînt.
Iar cuvîntul `program` este corect sintactic, avînd semantica obișnuită pe care
o găsiți în dicționar.

Așadar, revenind la paradigme de programare, nu faceți confuzia între diferențele
de sintaxă și cele de paradigmă! De exemplu, o *diferență de sintaxă* între
Python și C++ este `x += 1` și `x++;`, însă o *diferență de paradigmă* este că
într-un limbaj precum Python putem scrie *imperativ* (vezi mai jos) o incrementare
simplă sub forma:
```python
x += 1
```
în timp ce într-un limbaj funcțional ca [Haskell](https://www.haskell.org/) putem scrie o *funcție* care face
același lucru:
```haskell
Module Increment where

f :: Integer -> Integer
f = add1
```
Diferența importantă este că într-un limbaj funcțional definim *funcții*, care trebuie
*apelate* pentru a produce vreun rezultat. Mai multe detalii, mai jos.
Reținem deocamdată că diferența de paradigmă este altceva față de diferența de sintaxă.

## Paradigme de programare
Principala clasificare este între paradigma *imperativă* și cea *declarativă*.

În cazul unui program *imperativ*, programatorul scrie exact ce vrea să rezolve
și cum. Dă instrucțiuni compilatorului (sau interpretorului), care să fie urmate
imperativ.

Într-un program *declarativ*, programatorul declară, caracterizează rezultatul,
dar nu instruiește compilatorul *cum* să ajungă la acel rezultat. Din acest punct
de vedere, un limbaj de programare declarativă are o vedere superioară celor imperative.

Clasificarea continuă, iar limbajele imperative se împart în:
- *procedurale*: în care se pune accentul pe funcții și proceduri;
- *orientate pe obiecte*, în care starea mașinii este caracterizată cu ajutorul
  unor abstracții precum *clase* și *obiecte*.

Limbajele declarative se împart în:
- *funcționale*, în care se lucrează cu funcții și compunerea lor;
- *logice*, care folosesc inferențe logice în loc de instrucțiuni;
- *matematice*, concentrate pe probleme de optimizare numerică;
- *reactive*, care fac legături între obiectele de lucru și „reacționează“ la schimbări ulterioare.

Majoritatea limbajelor de programare populare suportă mai mult de o paradigmă.
De exemplu, în Python și C++ -- care sînt privite drept limbaje imperative, în general --
se poate lucra cu metode funcționale, folosind expresii `lambda`.
În Python, puteți citi [aici](https://realpython.com/python-lambda/), cum funcționează, iar în C++, [aici](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-170).

Unul dintre cele mai cunoscute limbaje funcționale este [Haskell](https://www.haskell.org/),
care are proprietatea de a fi *pur*, adică suportă numai paradigma funcțională
și se preferă un stil de codare care să nu aibă *efecte secundare*. Cu alte cuvinte,
se descurajează programarea care să afișeze valori sau să producă efecte
altfel decît prin aplicarea funcțiilor asupra argumentelor.

**IMPORTANT:** În cadrul acestui laborator, puteți lucra cu orice limbaj de programare
doriți și orice paradigmă preferați. Exemplele pe care le veți întîlni vor fi scrise
în Python, cu o paradigmă procedurală.

## Introducere în Python
[Python](https://www.python.org/) este un limbaj *interpretat*. Aceasta înseamnă că se poate rula
„dinamic“ un program scris în Python și nu este nevoie să se compileze după fiecare
modificare, iar apoi să se ruleze executabilul. Mai mult, un program scris în Python
poate fi rulat chiar și pe bucăți, dacă are sens.

În general, Python, la bază, nu este un limbaj axat pe performanță, însă poate fi
compilat către C sau C++ (folosind, de exemplu, [Cython](https://cython.org/)) și se pot folosi 
diverse alte metode de optimizare.

Principala caracteristică a Python este *lizibilitatea*. Este o trăsătură de design
impusă de la început de [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum), cel care a creat limbajul. Astfel,
codul în Python este ușor de citit și nu folosește foarte multe semne de delimitare.
În locul acoladelor din C și C++ se folosește *indentarea de 4 spații*. În exemplul
de mai jos, puteți ghici ușor ce se întîmplă, chiar dacă nu sînteți familiarizați
cu limbajul:
```py
import math

def estePrim(x):
	for d in range(2, math.sqrt(x) + 1):
		if x % d == 0:
			return 0
	return 1

x = int(input("Introduceți un număr: "))
if estePrim(x):
	print(f"{x} este prim.")
else:
	print(f"{x} nu este prim.")
```

Mai departe, pentru a vă familiariza cu limbajul, propun să parcurgeți [exemplele](./exemple) incluse.
Acestea conțin și suficiente comentarii care clarifică ce se întîmplă și vă încurajez să
*scrieți* (nu să copiați) codul și să-l rulați pe calculatorul vostru. De asemenea,
după ce ați înțeles modul de funcționare, vă puteți gîndi și la variații, adică să faceți
modificări în cod care să rezolve o problemă similară.

### Exemple
- [cmmdc pentru o listă de elemente](./exemple/n-cmmdc.py);
- [operații simple cu `string`](./exemple/litere.py);
- [criptosistemul Caesar](./exemple/caesar.py);
- [rezolvarea ecuației de gradul al doilea, cazul rădăcinilor reale](./exemple/ec2.py);
- [6/49](./exemple/6din49.py).

## Tutoriale
Cei care preferă să citească și să exerseze pornind de la tutoriale, recomand cîteva:
- [@ w3 Schools](https://www.w3schools.com/python/);
- [@ python.org](https://docs.python.org/3/tutorial/index.html);
- [@ tutorialspoint](https://www.tutorialspoint.com/python/index.htm);
- [@ learnpython.org](https://www.learnpython.org/);
- [@ pythontutorial.net](https://www.pythontutorial.net/);
- [@ geeksforgeeks](https://www.geeksforgeeks.org/python-programming-language/learn-python-tutorial/);
- [@ Harvard](http://tdc-www.harvard.edu/Python.pdf).

Sau, dacă preferați o carte, recomand pe cea a lui [Gaddis](https://www.pearson.com/us/higher-education/program/Gaddis-My-Lab-Programming-with-Pearson-e-Text-Access-Card-for-Starting-out-with-Python-5th-Edition/PGM2889368.html).

## Exerciții
[Aici](./exercitii).
