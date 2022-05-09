# Exerciții recapitulative (Model examen)

Rezolvați, din exercițiile de mai jos, la alegere, dar astfel încît să totalizați
maximum 2 puncte din prima secțiune și maximum 2 puncte din a doua secțiune.

Exercițiile rezolvate peste punctaj se vor ignora.

## Secțiunea 1: Calcule (maximum 2p, la alegere)

1.1. **(0.5p)** Scrieți un program care să primească de la tastatură unul dintre prenumele dumneavoastră
și să afișeze două șiruri de caractere, unul alcătuit doar din vocalele din prenume,
iar celălalt alcătuit doar din consoanele din prenume.
Includeți și condițiile corespunzătoare de validare a datelor de intrare.

Exemplu: Pentru "Adrian", se afișează "aia" și "drn".

1.2. **(0.5p)** Scrieți un program care să primească drept date de intrare `z, l, a`, unde `z` este ziua dumneavoastră
de naștere, `l` este luna și `a` este anul și să afișeze descompunerea în factori primi a produsului lor.
Includeți și condițiile corespunzătoare de validare a datelor de intrare.

Exemplu: Pentru `z = 5, l = 11, a = 1999`, se afișează `109945 = 5^1 * 11^1 * 1999^1`.

1.3. **(0.5p)** Scrieți un program care să primească de la tastatură `n` și `k` și să calculeze combinări de `n`
luate cîte `k`. Includeți și condițiile corespunzătoare de validare a datelor de intrare.

1.4. **(0.5p)** Scrieți un program care să citească un text dintr-un fișier (exemplu: un articol de pe Wikipedia)
și unul dintre prenumele dumneavoastră de la tastatură și să afișeze de cîte ori apare în text fiecare literă
din prenume, *ținînd cont de majusculă/minusculă* (i.e. apariția lui "a" este diferită de apariția lui "A").

1.5. **(1.5p)** Scrieți un program care să primească de la tastatură patru numere, `a, b, m, n` și să determine
ecuația dreptei perpendiculare pe dreapta `y = ax + b`, punctul de perpendicularitate fiind `(m,n)`.
Includeți și condițiile corespunzătoare de validare a datelor de intrare.

1.6. **(1p)** Scrieți un program care să primească de la tastatură un număr natural `n > 2` și să afișeze
toate submulțimile mulțimii `{1, 2, 3, ..., n}`. Exemplu: `n = 3`, se afișează `{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}`.
Includeți și condițiile corespunzătoare de validare a datelor de intrare.

1.7. **(1p)** Scrieți un program care să citească de la tastatură `n`, care reprezintă anul nașterii
dumneavoastră și să genereze aleatoriu o listă de `n` numere naturale, cu valori între luna nașterii și ziua de naștere.
Afișați media numerelor generate și ce procent din numărul de numere generate este mai mare decît media.

1.8. **(1p)** Scrieți un program care să genereze aleatoriu o listă de 100 de numere întregi între 0 și 20 (`numere`)
și o listă de 100 de ponderi (`ponderi`), cu următoarele reguli:
- ponderile sînt numere reale, mai mari sau egale cu 0 și mai mici strict ca 1;
- ponderile corespund 1-1 numerelor din listă (`ponderi[i]` corespunde `numere[i]`, pentru orice `i`);
- dacă `numere[i]` este între 0 (nestrict) și 10 (nestrict), `ponderi[i]` nu poate depăși 0.3;
- dacă `numere[i]` este între 10 (strict) și 15 (nestrict), `ponderi[i]` trebuie să fie între 0.3 (strict) și 0.6 (nestrict);
- dacă `numere[i]` esate între 15 (strict) și 20 (nestrict), `ponderi[i]` trebuie să fie între 0.6 (strict) și 1 (strict).

Calculați și afișați apoi media ponderată a numerelor din lista `numere`, cu ponderile din lista `ponderi`.
Afișați numerele cu ponderea cea mai mare și numerele cu ponderea cea mai mică.

1.9. **(1.5-2p)** Scrieți un program care să preia dintr-un fișier (sau dintr-un URL) un text de cel puțin 100 de cuvinte
și care să alcătuiască două liste (sau un dicționar) care să contorizeze aparițiile caracterelor alfanumerice în text,
*fără a face distincția între majuscule și minuscule*. De exemplu, va rezulta un dicționar de forma 
`caractere = {'a': 100, 'b': 124, 'c': 511, '0': 411, ...}` sau două liste de forma `caractere = ['a', 'b', 'c', 'd', ..., '0', '1', ...]`
și `aparitii = [1344, 512, 522, 514]` (`aparitii[i]` înseamnă de cîte ori apare `caractere[i]` în text).
Calculați:
- media (`medie`) listei de apariții și afișați caracterele care apar într-un interval de lungime 20% în jurul mediei (adică între `medie + 10% * medie` și `medie - 10% * medie`);
- mediana listei de apariții și afișați caracterul/caracterele corespunzător/corespunzătoare;
- modul/modurile listei de apariții și afișați caracterul/caracterele corespunzător/corespunzătoare;
- abaterea standard `stdev` și afișați caracterele care corespund intervalului `[medie + stdev, medie - stdev]`.

**Observație:** Se acordă maximum 1.5p dacă se fac calculele statistice cu biblioteca `statistics` și se folosesc 2 liste
și maximum 2p dacă se fac calculele fără `statistics` și se folosește un dicționar.

1.10. **(1p)** Scrieți un program care să preia dintr-un fișier (sau dintr-un URL) un text de cel puțin 100 de cuvinte
și care să returneze un dicționar sau două liste corespunzătoare caracterelor alfanumerice care apar de un număr prim de ori.
Să se afișeze dicționarul sau listele rezultate într-un alt fișier.

## Secțiunea 2: Grafice (maximum 2p, la alegere)

**Observație:** Dacă nu se precizează explicit, puteți folosi orice setări vizuale pentru grafice (culoare, opacitate, stilul liniei etc.).
Dacă există o precizare explicită, (ne)respectarea ei va fi (de)punctată.

2.1. **(1p)** Citiți de la tastatură ziua de naștere `z`, luna de naștere `l` și vîrsta `v`.
Reprezentați grafic, sub forma `pie chart`, procentele reprezentate de `z, l, v` din `z + l + v`.

2.2. **(1p)** Realizați un grafic de tip `bar` care să aibă pe axa OX literele unice din numele
dumneavoastră complet (nume + prenume), în ordinea în care apar, fără repetiții, iar pe axa OY,
pozițiile acestora din alfabet. Exemplu: Pentru "Manea Adrian-Costin", avem de reprezentat perechile
`(m, 13), (a, 1), (n, 14), (e, 5), (d, 4), (r, 18), (i, 9), (c, 3), (s, 19), (t, 20)`.

2.3. **(2p)** Generați aleatoriu o listă de numere întregi cuprinse între 0 și 100, `date`.
Generați aleatoriu o listă de ponderi, cuprinse între 0 și 1, `ponderi`. Ambele liste vor avea
un număr aleatoriu de elemente, cuprins între 1000 și 2000. Reprezentați grafic, de tip `bar`,
perechile `(i, date[i])` cu bare de culoare hex `#123456` și opacitate `13%` și, suprapus.
perechile `(i, date[i]*ponderi[i])`, cu bare de culoare hex `#654321` și opacitate `93%`.
Reprezentați cu o linie orizontală roșie continuă media primelor bare și o linie orizontală verde, punctată
media datelor ponderate. Plasați legenda pe desen.

2.4. **(2p)** Scrieți un program care să preia dintr-un fișier sau dintr-un URL un text cu cel puțin
100 de cuvinte și salvați într-un dicționar sau în două liste caracterele alfanumerice și numărul lor
de apariții. Reprezentați grafic:
- în 2 figuri sau grafice diferite caracterele alfabetice și cele numerice, sortate alfabetic, respectiv crescător, de tip `bar` plot, înălțimea barelor fiind numărul de apariții;
- calculați și trasați mediile celor două seturi ca orizontale, linie continuă albastră pentru caracterele alfabetice și linie punctată verde pentru caracterele numerice;
- calculați și trasați abaterile standard pentru cele două seturi, sub formă de intervale colorate, în jurul mediilor (colorați, deci, intervalul `[medie - stdev, medie + stdev]`).

**Observație:** Puteți folosi și două dicționare (sau 4 liste), pentru a separa caracterele numerice de cele alfabetice.

2.5. (**NOTA 10**) Se dă funcția `f(x) = x**2 * exp(-x) + sin(x)`.
- **(0.5p)** Reprezentați-o grafic, cu linie verde, de opacitate 30%, pe domeniul `[-1, 10]`, folosind cel puțin 100 de puncte.
- **(0.5p)** Folosind aceleași puncte, trasați, pe același interval, graficul funcției `g(x) = sin(x)`, cu linie albastră, de opacitate 25%.
- **(0.5p + 0.5p)** Trasați tangenta la graficul funcției `f` în punctul de abscisă `-0.5` și tangenta la graficul funcției `g` în punctul de abscisă `pi/5`.
