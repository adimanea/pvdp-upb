# Exerciții cu reprezentări grafice discrete

Toate exercițiile de mai jos este preferabil să fie rezolvate în foi Jupyter, toate la un loc sau cîte
un exercițiu pe foaie, împreună cu teoria necesară.

1. Studiați și înțelegeți exemplele din documentația `matplotlib`, în special:
- [histograme colorate cu diverse modele](https://matplotlib.org/stable/gallery/lines_bars_and_markers/filled_step.html#sphx-glr-gallery-lines-bars-and-markers-filled-step-py);
- [figuri complexe cu scatter și histograme](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html#sphx-glr-gallery-lines-bars-and-markers-scatter-hist-py);
- [scatter plot cu buline stilizate și grid](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html#sphx-glr-gallery-lines-bars-and-markers-scatter-demo2-py);
- [scatter plot cu pie în loc de bulină](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_piecharts.html#sphx-glr-gallery-lines-bars-and-markers-scatter-piecharts-py);
- [scatter plot cu trifoi în loc de bulină](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_symbol.html#sphx-glr-gallery-lines-bars-and-markers-scatter-symbol-py);
- [histogramă cu calcule statistice](https://matplotlib.org/stable/gallery/statistics/histogram_features.html#sphx-glr-gallery-statistics-histogram-features-py);
- [histogramă de diverse tipuri cu `histtype`](https://matplotlib.org/stable/gallery/statistics/histogram_histtypes.html#sphx-glr-gallery-statistics-histogram-histtypes-py);
- [`histtype` pe mai multe seturi de date](https://matplotlib.org/stable/gallery/statistics/histogram_multihist.html#sphx-glr-gallery-statistics-histogram-multihist-py);
- [mai multe histograme pe aceeași figură](https://matplotlib.org/stable/gallery/statistics/multiple_histograms_side_by_side.html#sphx-glr-gallery-statistics-multiple-histograms-side-by-side-py);
- [extragerea unei felii dintr-un pie chart](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html#sphx-glr-gallery-pie-and-polar-charts-bar-of-pie-py);
- [pie charts concentrice](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html#sphx-glr-gallery-pie-and-polar-charts-nested-pie-py);
- [pie și donut](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py);
- [histogramă animată](https://matplotlib.org/stable/gallery/animation/animated_histogram.html#sphx-glr-gallery-animation-animated-histogram-py);
- [histogramă în sistem logaritmic](https://matplotlib.org/stable/gallery/scales/log_bar.html#sphx-glr-gallery-scales-log-bar-py);

2. Experimentați cu exemplele de mai sus, modificînd seturile de date, culorile, tipul reprezentărilor, rescalarea, etichetele etc.

3. Se consideră setul de date: `(X, Y) = [(1, 3), (2, 5), (3, 7), (4, 10), (5, 5), (6, 3), (7, 20), (8, 11), (9, 20), (10, -1)]`.
- realizați un grafic de tip histogramă care să arate dependența variabilei `Y` de variabila `X`;
- realizați un grafic de tip scatter plot care să arate dependența de mai sus;
- realizați un grafic de tip pie chart care să arate cîte procente din perechile `(X, Y)` de mai sus au aceeași paritate (după ce calculați procentele, tot în cod). Mai precis, trebuie să aveți 4 perechi cu aceeași paritate (`(1, 3), (3, 7), (4, 10), (5, 5)`) și 6 perechi cu parități diferite, deci graficul va avea 2 felii. Realizați-l și în varianta lipită, și în cea folosind `explode`.

4. Se realizează un sondaj, unde 10 persoane sînt întrebate cîte cărți pe an citesc. Se primesc răspunsurile
(sub forma `(sex, vîrstă, nr cărți)`): `(F1, 21, 30), (F2, 41, 40), (F3, 19, 55), (F4, 44, 4), (F5, 80, 20), (M1, 55, 25), (M2, 31, 31), (M3, 71, 21), (M4, 15, 25), (M5, 34, 31)`.
- realizați cîte un grafic de tip histogramă care să arate, separat, numărul de cărți citite de persoanele de sex feminin și cele de sex masculin;
- realizați un singur grafic de tip bar chart care să arate numărul de cărți citite de femei și bărbați, alăturînd barele după cea mai mică diferență de vîrstă (i.e. `(F1, 21)` va fi alăturată lui `(M4, 15)`, `(F2, 41)` va fi alăturată lui `(M5, 34)` etc.).

5. Se realizează un sondaj de opinie printre locuitorii unui oraș, care sînt întrebați
 ce genuri de muzică preferă și se primesc răspunsurile:

| Numărul de respondenți | Genul de muzică |
|----------------------- | --------------- |
| 200                    | clasică         |
| 171                    | jazz            |
| 311                    | blues           |
| 411                    | rock            |
| 401                    | electronică     |
| 355                    | folk            |

Realizați un grafic de tip pie chart care să arate procentele preferințelor, cu etichetele corespunzătoare.

6. Se consideră conjectura lui Collatz: dat un număr natural `n`, se aplică transformările:
- dacă `n` este par, se înjumătățește;
- dacă `n` este impar, se transformă în `3*n + 1`.

Conjectura afirmă că după un număr finit de pași, indiferent de numărul de pornire, se ajunge la 1.

Exemple:

```
10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
31 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
15 -> 46 -> 23 -> 70 -> 35 -> 106 -> 53 -> 160 -> 80 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
```

- Scrieți un program care să producă un set de date alcătuit din perechi de forma `(n, nr_pași_collatz(n))`,
pentru 1000 de valori aleatoare ale lui `n`, *diferite*. Exemplu: în cazul de mai sus avem setul:
`(10, 6), (31, 7), (15, 17)`. 
- Reprezentați grafic, pe o histogramă, dependența celor două variabile, sub forma `X = n, Y = nr_pași_collatz(n)`.
- Reprezentați grafic, pe o histogramă, pe intervale de lungime 10, numărul mediu de pași în algoritmul Collatz. Așadar, se va calcula media `M` de pași pentru numerele din intervalele `X1 = (1, 10), X2 = (11, 20), X3 = (21, 30)...` și se va reprezenta grafic dependența lui `M` de `X`.
- Reprezentați grafic pe un pie chart procentele dintre numerele care au necesitat între 1 și 100 de pași Collatz, între 101 și 200, între 201 și 300 etc., pînă la valoarea maximă din setul de date generat.

**Bonus** pentru oricare dintre exercițiile de mai sus dacă folosiți stilizări diverse: culori nestandard, modele, legende plasate non-standard, grid-uri, fonturi speciale etc.

---

## Grafice cu date preluate din fișiere CSV

7. Scrieți un fișier CSV folosind modulul specific, care să conțină cel puțin 3 liste
(corespunzătoare unui cap de tabel și două linii). Exemplu:
- `cap_tabel = ["nr_crt", "oraș/sector", "nota_parcuri", "nota_parcări", "nota_trafic", "nota_trotuar", "nota_borduri"]`
- `rasp_b = ["1", "B, Sector 3", "5", "8", "3", "10", "7"]`;
- `rasp_ct = ["2", "CT", "5", "7", "10", "3", "8"]`

Apoi reprezentați grafic pe o histogramă care să conțină alăturat datele pentru cele două orașe.
Opțional, trasați și cîte o orizontală care să arate media notelor.

8. Refaceți oricare dintre exercițiile laboratorului anterior, folosind scriere sau citire
în și din fișiere CSV. Exemple:
- L5.3.: puteți scrie cele două liste `X` și `Y` într-un CSV, cu 2 coloane și 10 linii;
- L5.4.: puteți scrie tripletele în trei liste `sex, vîrstă, nr_cărți` într-un CSV cu 3 coloane și 10 linii;
- L5.5.: puteți reface tabelul într-un CSV, cu listele `nr_rasp, gen_muzical`, apoi le scrieți într-un CSV cu 2 coloane și 7 linii;
- B5.1.: puteți scrie datele generate într-un CSV, de forma `input, pasiCollatz(input)`, cu 2 coloane și 1000 linii.

9. Preluați seturi de date de pe Internet în format CSV și realizați reprezentări grafice relevante.
Exemple:
- [Coronavirus Source Data](https://ourworldindata.org/coronavirus-source-data). Grafice posibile:
  + evoluția cazurilor noi într-o lună, pentru o țară fixată;
  + evoluția numărului total de vaccinări într-o lună, pentru o țară fixată;
  + pentru un set de cîteva (8-10 cel puțin) țări, media vaccinărilor într-o lună fixată;
 
- [Project datasets](https://perso.telecom-paristech.fr/eagan/class/igr204/datasets). Grafice posibile:
  + Alegeți o caracteristică nutritivă (e.g. proteine) și reprezentați grafic conținutul acelei caracteristici pentru tipurile de cereale incluse în CSV;
  + Evoluția lungimii filmelor versus data lansării;
  + Pie chart cu procentele de actori principali masculini/feminini pentru un deceniu.
 
- [CORGIS](https://corgis-edu.github.io/corgis/csv/). Grafice posibile:
  + Încasările medii pentru musical vs piese de teatru [de pe Broadway](https://corgis-edu.github.io/corgis/csv/broadway/) într-un pie chart;
  + Evoluția [temperaturii medii, minime, maxime](https://corgis-edu.github.io/corgis/csv/weather/) dintr-un stat din SUA;
  + Evoluția [vînzărilor de carte de pe Amazon](https://corgis-edu.github.io/corgis/csv/publishers/).