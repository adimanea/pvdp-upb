# Jupyter

Sistemul Jupyter, cunoscut anterior sub numele IPython (de la *Interactive Python*)
este foarte folositor pentru *programare interactivă*. Cu alte cuvinte, în loc să
scriem separat codul, în cîte un fișier, pe care să-l rulăm și documentația separat,
Jupyter ne oferă posibilitatea de a combina codul cu documentația în același document.

Și Markdown -- sistemul folosit pentru a scrie această documentație -- poate afișa cod,
ca de exemplu:
```python
print("Salut!")
```
Dar acest cod *nu poate fi executat*, ci doar afișat.

Denumirea de Jupyter provine de la faptul că în cadrul acestui sistem se pot folosi
cu ușurință 3 limbaje foarte folositoare:
- [Julia](https://julialang.org/) -- esențial în fizică și alte discipline care prelucrează date experimentale;
- [Python](https://www.python.org/) -- limbaj flexibil, general;
- [R](https://www.r-project.org/) -- limbaj foarte folosit în statistică și inteligență artificială, unde se lucrează cu instrumente statistice avansate.

Între timp, proiectul a avansat și acceptă foarte multe alte limbaje,
dar ele trebuie instalate individual. Vezi [aici](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

**Noi vom lucra doar cu Python, care este instalat automat.**

## Instalare și mod de lucru
Site-ul proiectului Jupyter este [aici](https://jupyter.org/).

Aveți, în secțiunea [Install](https://jupyter.org/install) indicațiile corespunzătoare.

Vom instala pachetul `Jupyterlab`, care conține tot ce este necesar:
- deschideți Terminal-ul din PyCharm (sau consola din Windows);
- introduceți comanda `pip install jupyterlab` și apăsați `Enter`, urmărind progresul instalării.

Pentru test și utilizare, creați un fișier cu extensia `.ipynb` (exemplu: `test.ipynb`).
PyCharm îl va recunoaște ca folosind Jupyter și veți vedea o interfață nouă, ca mai jos:

![img.png](img.png)

Imaginea corespunde fișierului de [aici](./jupyter-notebooks/test.ipynb).

**Observație 1:** Codurile „comunică“ între ele, astfel că, la blocul `In 3`, unde am folosit din nou
variabila `i`, este folosită cea din blocul `In 2`.

Observați că sursa este evaluată cu ajutorul *blocurilor*. În stînga, blocurile sînt indicate ca fiind
blocuri de intrare `In`, iar dedesubt, găsiți rezultatul execuției lor. Mai mult, în partea de sus
puteți vedea o selecție care corespunde tipului blocului: `Code` sau `Markdown`.

Urmăriți [documentația PyCharm](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html) 
sau demonstrația din cadrul cursului (și rezultatul în [demo.ipynb](./jupyter-notebooks/demo.ipynb)).

Veți avea nevoie și de [sintaxa Markdown](https://www.markdownguide.org/basic-syntax).

## Exerciții
Scopul acestui curs & laborator este să vă familiarizați cu noul mod de lucru.
Astfel că principala cerință va fi să lucrați exemple simple în noul format,
folosind cît mai multe elemente.

De exemplu, **elemente de bază**:
- asigurați-vă că ați instalat corect Jupyter;
- creați o foaie de lucru `ipynb`;
- introduceți un bloc de text și „rulați-l“ cu `Shift + Enter` (exemplu `Test bloc text.`);
- introduceți un bloc de cod și rulați-l cu `Shift + Enter` (exemplu `print("Salut!")`).

Apoi, **elemente intermediare**:
- folosiți cît mai multe tipuri de conținut în blocul text:
  + heading (titlu, subtitlu etc., cu sintaxa `# Titlu` pentru titlu, `## Subtitlu` pentru subtitlu etc.);
  + text **bold**, cu sintaxa `**text**`;
  + text *italic*, cu sintaxa `*text*`;
  + text `preformatat`, stil cod, cu sintaxa `` `text` ``;
  + [link](https://tcsi.ro/), cu sintaxa `[text](URL)`;
  + liste numerotate și nenumerotate;
- blocurile de cod să facă unele calcule simple: 
  + afișați toți multiplii de 13 de la 1 la 100;
  + afișați numerele prime de la 1 la 100;
  + afișați toate pătratele perfecte de la 1 la 1000.
  + afișați toate numerele prime dintr-un interval `[a,b]`, cu capetele citite de la tastatură (puteți folosi `input()` într-un bloc de cod);
  + afișați 10 numere aleatorii *diferite* între 1 și 100.