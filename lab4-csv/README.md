# Lucrul cu fișiere CSV

Formatul CSV (eng. *Comma Separated Variables*, adică valori separate prin virgulă) se folosește
ca o variantă simplificată a tabelelor de tip Excel. Informațiile sînt scrise pe linii, iar coloanele
se separă prin virgulă. De exemplu, într-un fișier CSV putem avea:

```csv
titlu_col1, titlu_col2, titlu_col3, titlu_col4
val1_col1, val1_col2, val1_col3, val1_col4
val2_col1, val2_col2, val2_col3, val2_col4
...
```

Ceea ce este echivalent cu tabelul:

| titlu_col1 | titlu_col2 | titlu_col3 | titlu_col4 |
|------------|------------|------------|------------|
| val1_col1  | val1_col2  | val1_col3  | val1_col4  |
| val2_col1  | val2_col2  | val2_col3  | val2_col4  |

Orice separator în afara virgulei se ignoră, deci pentru lizibilitate, multe editoare folosesc
spații sau tab-uri pentru separare vizuală. Deci putem scrie, de exemplu:

```csv
Oraș,       Județ,      Populație
Iași,       Iași,       100000
București,  București   2000000
Craiova,    Olt,        2000
```

## Preluarea datelor în Python
Putem prelua datele dintr-un fișier CSV folosind modulul `csv`.
Apoi, avem funcțiile `reader` și `writer`, care creează obiecte corespunzătoare.

**Observație:** Dacă primiți o eroare privitoare la modulul CSV, instalați-l în terminal, cu comanda:
```shell
pip install csv
```

Exemplu de citire:
```python
import csv

with open('inFile.csv', 'r') as fisierCSV:
    listaDate = csv.reader(fisierCSV)
    # acum lista listaDate conține toate elementele
    for linie in listaDate:
        print(linie)
```

Exemplu de scriere:
```python
import csv

linia1 = ['Oraș', '1-10', '11-20', '21-30', '31-40', '41-50']
linia2 = ['București', '4', '63', '31', '44', '55']
linia3 = ['Cluj', '42', '32', '55', '22', '11']
linia4 = ['Iași', '44', '66', '11', '22', '55']

# deschidem (sau creăm) fișierul în care vrem să scriem
with open('outFile.csv', 'w+') as fisierCSV:
    # creăm obiectul care va scrie, linie cu linie
    scriere = csv.writer(fisierCSV)
    # scriem liniile, pe rînd
    scriere.writerow(linia1)
    scriere.writerow(linia2)
    scriere.writerow(linia3)
    scriere.writerow(linia4)
```

## Resurse
- documentația oficială a modulului `csv` este [aici](https://docs.python.org/3/library/csv.html);
- un scurt tutorial, [aici](https://www.geeksforgeeks.org/working-csv-files-python/);
- **seturi de date**:
  + [data.gov](https://catalog.data.gov/dataset/) -- seturi de date publice de la Guvernul American;
  + [data.world](https://data.world/datasets/free) -- necesită cont, gratis;
  + [datahub](https://datahub.io/collections) -- gratis;
  + [Kaggle datasets](https://www.kaggle.com/datasets) -- necesită cont, gratis;
  + [Google datasets](https://datasetsearch.research.google.com/) -- gratis;
  + Direct de pe GitHub, căutați "dataset" și găsiți, de exemplu, [acest repository](https://github.com/nytimes/covid-19-data), de la NY Times.
