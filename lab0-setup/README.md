# Laborator 0: Setup inițial

Ne vom ocupa aici de setup-ul inițial, pentru a putea să începem lucrul cu Python.
Dacă preferați un alt mediu de lucru sau chiar un alt limbaj de programare,
sînteți liberi să alegeți, însă ghidul de aici se va concentra pe Python și cîteva
dintre editoarele disponibile, plus IDE-ul PyCharm.

## Cod exemplu
Orice variantă veți alege, mai jos aveți două linii de cod pe care să le testați.
Copiați-le într-un fișier text, salvați-l cu extensia `py` (de exemplu, `test.py`)
și rulați-l cu metodele specifice.

```py
nume = input("Cum te cheamă? ")
print(f'Salut, {nume}!')
```

Output-ul așteptat este să introducem numele de la tastatură și vom vedea:

```
Cum te cheamă? Adrian
Salut, Adrian!
```

Dacă aveți un astfel de rezultat, ați finalizat setup-ul.

Aveți un fișier-exemplu și [aici](./test-setup.py).

## Varianta 1: PyCharm
Avantajul utilizării PyCharm este că vine la pachet cu cele necesare pentru a rula
fișierele Python (interpretorul, manager-ul de pachete și biblioteca standard, în mare).

PyCharm este, de asemenea, un **IDE** (Integrated Development Environment), adică
o unealtă mult mai complexă, în care se scrie cod, se interpretează, se rulează,
se face debugging și, în plus, vine și cu elemente ajutătoare precum autocomplete,
sugestii, analiză pe cod, profiling, testare ș.a.m.d.

Puteți citi toate caracteristicile PyCharm pe [site-ul oficial](https://www.jetbrains.com/pycharm/).

De asemenea, dacă aplicați cu adresa de email instituțională, e posibil să primiți
și acces gratuit la versiunea pro.

Deocamdată, ne vom concentra pe versiunea gratuită, Community Edition, pe care
o puteți descărca de [**aici**](https://www.jetbrains.com/pycharm/download/#section=windows), pentru orice sistem de operare. În unele distribuții
de Linux, se găsește direct în repository-urile oficiale ale package manager-ului,
deci puteți rula direct comenzile corespunzătoare, precum:

```sh
$ sudo pacman -S pycharm
$ sudo apt-get install pycharm
$ yum install pycharm
```

Documentația oficială este [aici](https://www.jetbrains.com/help/pycharm/quick-start-guide.html#create).

**Observație:** PyCharm, ca majoritatea IDE-urilor, lucrează cu *proiecte*, astfel
că pentru fiecare program pe care îl scrieți, va trebui să creați cîte un folder
în care să le țineți, iar PyCharm va stoca tot acolo fișierele sale ajutătoare.

Alternativ, puteți crea un singur proiect și mai multe fișiere-sursă și să le
rulați individual. Pentru aceasta, faceți click dreapta pe numele fișierului
pe care vreți să-l rulați și alegeți opțiunea `Run [filename]` sau apăsați
`ctrl + shift + f10`.

Puteți acum să încărcați fișierul-exemplu de mai sus sau să scrieți liniile
respective într-un fișier-sursă nou (*nu uitați de extensia `.py` la salvare!*).

## Varianta 2: VSCode
Dacă alegeți să instalați un editor text, va trebui să instalați manual și
separat limbajul (interpretorul, uneltele și biblioteca standard).

### Instalarea limbajului
- Pe Linux, Python este deja instalat. Testați scriind în terminal `python --version`
  și ar trebui să vedeți un rezultat precum `Python 3.9.4`. Dacă nu, instalați cu package
  package manager-ul corespunzător;
- Pe macOS, Python este deja instalat și puteți testa similar. Opțional, puteți instala
  Xcode *și să-l deschideți după*, pentru a asigura și instalarea Xcode developer tools.
- Pe Windows, Python trebuie instalat. Alegeți versiunea cea mai recentă din Microsoft Store
  (actualmente, 3.9) și instalați. Alternativ, descărcați de pe [site-ul oficial Python](https://www.python.org/downloads/).

**Important:** Asigurați-vă că interpretorul, dar și manager-ul de pachete (de fapt, toate
binarele importante) sînt în variabila `PATH` a sistemului, adică le poate găsi orice comandă,
lansată de oriunde.

Pe Linux și macOS, scrieți în terminal:
```sh
$ which python
/path/to/python

$ which pip
/path/to/pip

# alternativă
$ echo $PYTHONPATH
/path/to/python
```
și dacă sistemul răspunde cu o cale de director, înseamnă că setup-ul este făcut. Altfel,
citiți ghidurile corespunzătoare (care se rezumă, în mare, la `export PATH=$PATH:/new/path`).

Pentru Windows, citiți [instrucțiunile oficiale](https://docs.python.org/3/using/windows.html). TL;DR: 
- găsiți unde este instalat limbajul (default este `C:\Users\[user]\AppData\Local\Programs\Python\Python39`);
- copiați calea respectivă;
- Start -> Edit environment variables for your account -> Path -> Edit -> New -> `C:\Users\[user]\AppData\Local\Programs\Python\Python39`.

Indiferent de sistem de operare sau de metoda aleasă, puteți testa, de exemplu, cu

```sh
$ pip --version
pip 21.1.1
$ python --version
Python 3.9.4
```

**NU CONTINUAȚI PÎNĂ NU REZOLVAȚI PASUL ACESTA!**

Dacă ați reușit, puteți acum instala editorul VSCode, pentru orice sistem de operare de pe [site-ul oficial](https://code.visualstudio.com/).

Odată instalat, puteți căuta în extensii pachete pentru Python sau puteți rula direct.
Scrieți/copiați codul din exemplu, apoi apăsați butonul "Play" din dreapta sus 
(sau `shift + ctrl + p > Run Python file in terminal`) și veți vedea rezultatele în partea de jos a ecranului.

Alternativ, puteți deschide aplicația de Terminal, navigați unde ați salvat fișierul `test.py` (sau cum l-ați denumit)
și scrieți în terminal `python test.py`, care vă va rula programul.

## Interacțiunea, în general
Python este un *limbaj interpretat*, spre deosebire de C sau C++, care sînt *compilate*. Principala diferență
este că puteți rula direct fișierul-sursă, nu mai trebuie să lansați o comandă separată de compilare,
apoi să rulați executabilul.

Acest lucru are și avantajul că puteți rula *bucăți din fișierul-sursă*, dacă au sens independent.

În plus, un alt avantaj este că Python poate fi folosit și pentru a „asculta“ comenzi interactive.
Dacă scrieți în terminal `python` și apăsați `enter`, veți deschide interpretorul în modul interactiv.

Veți primi un mesaj precum cel de mai jos:

```sh
$ python3.10
Python 3.10 (default, June 4 2019, 09:25:04)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Astfel, puteți introduce comenzi pe rînd și să le rulați cu `enter`.
```sh
>>> 2 + 3
5
>>> import math
>>> math.sin(30)
-0.9880316240928618
```

Puteți ieși cu `exit()`.

Mai multe detalii puteți citi în [documentația oficială](https://docs.python.org/3/tutorial/interpreter.html).