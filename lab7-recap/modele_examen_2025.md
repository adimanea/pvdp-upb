# Modele Examen 2025

Examenul se structurează astfel:
- un exercițiu standard Python (liste, șiruri de caractere, fișiere);
- un exercițiu cu statistică (folosind modulul `statistics`);
- pentru note 8+: reprezentări grafice, folosind modulul `matplotlib`.

**DURATA EXAMEN: 45 MINUTE**.

## MODEL 1
1. Citiți de la tastatură un cuvînt `cuv` și un număr `k`. Apoi afișați cuvîntul obținut cu următoarele modificări ale fiecărui caracter `c` din `cuv`:
- dacă este majusculă, nu se modifică;
- dacă este minusculă, se modifică cu `+k` poziții în alfabet.

Exemplu: `cuv = EXamEn, k = 3`. Output: `EXdpEq`.

2. Presupunem că avem o populație de 1,000,000 locuitori, care participă la alegeri cu 2 candidați, `A` și `B`.

Presupunem mai departe populația împărțită în grupe de vîrstă: 18-27, 28-37, 38-47, 48-57, 58-67, 68-77, 78-87, 88-97, 98-107.

Generați aleatoriu un număr de voturi pentru candidatul `A`, pentru fiecare grupă de vîrstă, un număr aleatoriu de voturi invalidate (maximum 10%) și restul de voturi pentru candidatul `B`, pe fiecare grupă de vîrstă.

Reprezentați ca pie chart voturile (pentru `A`, pentru `B` și cele anulate), iar pentru candidatul cîștigător, reprezentați ca bar chart distribuția votanților.

---

## MODEL 2
1. Citiți de la tastatură două numere naturale `a` și `b` (ambele mai mici decît 1,000) și un număr natural `k`. Scrieți într-un fișier `prime.txt` numerele prime din intervalul `[a,b]`.

2. Generați aleatoriu o listă de 100,000 numere întregi între 50,000 și 100,000. Afișați-le media, mediana, modul, abaterea standard și reprezentați-le sub formă de scatter plot, cu puncte verzi.

---

## MODEL 3
1. Copiați cerințele din acest examen într-un fișier text `text.txt`. Afișați cîte vocale se află în text, cîte numere, și cîte semne de punctuație (excluzînd spațiile).

2. Generați aleatoriu o listă de 100,000 numere întregi între 70,000 și 100,000 și o listă de 100,000 ponderi (între 0 și 1). Afișați-le media aritmetică, media ponderată, folosind ponderile respective, mediana, modul, abaterea standard și reprezentați-le sub formă de scatter plot, cu steluțe roșii, iar valorile mai mari de 90,000, reprezentați-le cu triunghiuri albastre.
