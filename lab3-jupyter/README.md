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

### PyCharm
**Observație:** PyCharm, versiunea Community (gratuită pentru toată lumea) permite
foi Jupyter *doar în sistem read-only*, deci nu le veți putea edita.
Aveți alternativa să descărcați versiunea pro, folosind adresa de email `@upb`, cu care
vă înregistrați pentru un cont gratuit. Indicațiile de mai jos presupun această metodă.
Alternativa fără PyCharm urmează.

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

### Terminal & Browser
Puteți instala și utiliza Jupyter și fără PyCharm, astfel:
- deschideți Windows Terminal sau Command Prompt din Start;
- introduceți comanda `pip install jupyterlab` și așteptați finalizarea instalării.

Apoi, pentru utilizare, navigați în directorul unde veți păstra foile Jupyter. Puteți face aceasta
în una dintre variantele:
- navigați din terminal cu comanda `cd` (change directory) pînă în directorul dorit (exemplu: `cd D:\proiecte\pvdp`);
- navigați din Windows Explorer către directorul dorit apoi:
  + dacă aveți Windows Terminal instalat, apăsați click dreapta în directorul din Explorer și alegeți `Open in Terminal` ca în imagine: ![img_1.png](img_1.png);
  + dacă nu aveți Windows Terminal instalat, copiați calea de director din Explorer apăsînd `Ctrl + L`, apoi `Ctrl + C` și deschideți Command Prompt apăsînd `Windows + R` și scrieți `cmd`, apoi apăsați `Enter`. După ce se deschide Command Prompt, scrieți `cd` și apoi introduceți cu `Ctrl + V` calea de director copiată și apăsați `Enter`.

**Nu continuați pînă cînd Windows Terminal sau Command Prompt nu vă arată că sînteți în directorul dorit!**. 
Exemplu din Windows Terminal: ![img_2.png](img_2.png) și din Command Prompt: ![img_3.png](img_3.png).

Dacă directorul nu se schimbă în Command Prompt, modificați comanda adăugînd `/d`, 
adică, de exemplu, `cd /d D:\proiecte\pvdp`.

Din directorul respectiv, introduceți comanda `jupyter notebook` și apăsați Enter.
Se va deschide o fereastră de browser ca mai jos, care vă va arăta fișierele din directorul respectiv.

![img_4.png](img_4.png)

Din meniul `New > Python 3` veți crea o foaie nouă.

![img_5.png](img_5.png)

---

Urmăriți [documentația PyCharm](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html) 
sau demonstrația din cadrul cursului (și rezultatul în [demo.ipynb](./jupyter-notebooks/demo.ipynb)).

Veți avea nevoie și de [sintaxa Markdown](https://www.markdownguide.org/basic-syntax).