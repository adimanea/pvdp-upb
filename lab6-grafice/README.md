# Reprezentări grafice discrete

În acest curs vom începe studiul reprezentărilor grafice, pentru cazul *discret*, adică
acele grafice care se realizează din puncte, care nu pot fi unite de linii continue.

Din punct de vedere practic, graficele discrete sînt cele care se întîlnesc în situații
experimentale sau atunci cînd se colectează date statistice ori de laborator.

Ideea principală a acestor notițe este să familiarizeze cu noțiunile generale, teoretice
privitoare la prezentarea și înțelegerea graficelor discrete.

## Interpretare matematică bidimensională
Situația pe care o vom întîlni este următoarea: presupunem că vrem să măsurăm dependența
unei mărimi `Y` (ca "rezultat") în funcție de o mărime `X` (ca "date de intrare").
Exemple concrete:
- `Y` = viteza unui automobil în coborîre liberă în pantă, `X` = unghiul de înclinare a pantei;
- `Y` = cantitatea de precipitații medii zilnice din Făurei, `X` = luna din an în care se face măsurătoarea;
- `Y` = procentul de persoane cu venit net mediu lunar de peste 1000€, `X` = orașul din România pentru care se face măsurătoarea.

Este important de remarcat că putem face aceste măsurători atît pentru cantități care în mod evident
pot fi ordonate (e.g. o dependență de timp sau de distanță), dar și oarecare, cum este cazul studiilor
geografice, unde se inferă o ordine, precum cea alfabetică după numele orașelor.

În general, scopul măsurătorilor de tipul acesta poate fi:
- pentru *experiment*: atunci cînd nu se cunoaște rezultatul, ci se va infera o relație pe baza rezultatelor culese;
- pentru *verificare*: atunci cînd rezultatul teoretic este cunoscut, iar datele se culeg doar pentru a verifica dependența teoretică.

Măsurătorile experimentale se fac de multe ori atunci cînd o teorie a fost formulată și se vrea validată
prin experiment, cum este cazul științelor care au o componentă practică (de laborator).

Graficele discrete de care ne vom ocupa pentru început vor fi de următoarele tipuri:

### Histograme
![histograma](https://matplotlibguide.readthedocs.io/en/latest/_images/histogramEx.png)

În aceste grafice sîntem interesați de evoluția mărimii `Y` atunci cînd `X` variază și de aceea
se trasează aceste bare, pentru a evidenția înălțimile relative ale rezultatului.

### Grafice din bare (Bar Charts)
![bar](https://matplotlibguide.readthedocs.io/en/latest/_images/barchartEx.png)

Aceste grafice sînt similare histogramelor, dar se utilizează atunci cînd avem mai puține date,
repartizate eventual la distanțe mai mari pe axa `X`.

O variație a lor, care poate scoate în evidență valori comparative ale variabilei `Y` pentru
aceeași valoare sau valori apropiate ale lui `X` poate fi prezentată ca mai jos.

![bar_var](https://matplotlibguide.readthedocs.io/en/latest/_images/barchartCombineEx.png)

### Scatter Plot
![scatter](https://matplotlibguide.readthedocs.io/en/latest/_images/fig_scatterEx.png)

În exemplul de mai sus s-a reprezentat și curba teoretică pe care ar trebui să o verifice punctele culese
experimental, după care se poate face, eventual, studiul erorilor (abaterilor) punctelor față de teorie.
Un astfel de grafic fie este folosit pentru verificare, fie este interesat în primul rînd de "aspectul general"
al dependenței, pentru a-l încadra într-o funcție matematică cunoscută (în desenul de mai sus pare a fi o sinusoidă).

### Pie Chart
![pie](https://matplotlibguide.readthedocs.io/en/latest/_images/pieEx.png)

Astfel de exemple se folosesc în studii procentuale, de obicei, pentru a evidenția ce procente
din totalul datelor culese reprezintă diverse sectoare. Așadar, în acest caz, nu avem nevoie
de a reprezenta într-un sistem de axe, ci doar cantitativ, pentru a putea prezenta statistici
de tipul "P% din datele culese arată A, Q% arată B etc.".

-----------------

Vom exemplifica toate aceste tipuri de grafice în laborator. Pentru partea de Python, vom folosi
biblioteca `matplotlib`, integrată în foi Jupyter. Seturile de date, deocamdată, pot fi fictive,
date la intrare ca liste sau generate aleatoriu cu diverse proceduri.

Foaia Jupyter cu mai multe exemple [aici](grafice-discrete.ipynb).

Exerciții [aici](exercitii-grafice.md).