# Exerciții Laborator 1

## Ușoare
1. Scrieți un program care să citească de la tastatură două numere `a` și `b` și să afișeze toate numerele pare din intervalul `[a, b]`. Exemplu: `a = 3, b = 7`, se afișează `4, 6`.
2. Scrieți un program care să citească de la tastatură un cuvînt și să afișeze cîte vocale conține. Exemplu: se citește `Adrian`, se afișează `2`.
3. Scrieți un program care să citească `n`, apoi o listă de `n` numere naturale și să afișeze cîte sînt multiplu de 3 din listă. Exemplu: se citește `n = 3`, apoi lista `[1, 7, 9]`, se afișează `1`.
4. Scrieți un program care să citească `n`, apoi o listă de `n` numere naturale și să afișeze cîte sînt pătrate perfecte din listă. Exemplu: se citește `n = 3`, apoi lista `[5, 11, 21]`, se afișează `0`.
5. Scrieți un program care să citească `n`, apoi să afișeze primele `n` puteri nenule ale lui `n`. Exemplu: se citește `n = 3`, se afișează `3, 9, 27`.
6. Scrieți un program care să citească de la tastatură `n`, apoi `n` numere reale și să afișeze media lor aritmetică și media lor geometrică.
7. Scrieți un program care să rezolve o ecuație de gradul al doilea: se citesc trei numere `a, b, c`, ca fiind coeficienții ecuației `a * x^2 + b * x + c = 0` se afișează rădăcinile `x1` și `x2` sau mesajul `Ecuația nu are soluții.` dacă este cazul.
8. Scrieți un program care să răstoarne un număr. Se citește, de exemplu, numărul `4215653` și se afișează `3565124`.
9. Scrieți un program care să citească de la tastatură `n` și `k` și să afișeze combinări de `n` luate cîte `k`. Formula de calcul este `n! / (k! * (n - k)!)`.
10. Scrieți un program care să citească de la tastatură `a` și `b` și să afișeze cîtul și restul împărțirii lui `a` la `b`.

## Medii
1. Scrieți un program care citește de la tastatură `n` și afișează primele `n` numere prime. Exemplu: se citește `n = 5`, se afișează `2, 3, 5, 7, 11`.
2. Scrieți un program care citește de la tastatură `n` și afișează primul număr prim strict mai mare decît `n`. Exemplu: se citește `n = 20`, se afișează `23`.
3. Scrieți un program care citește de la tastatură `n`, o listă de `n` șiruri de caractere, apoi afișează cuvîntul obținut din inițialele șirurilor din listă. Exemplu: se citește `n = 4`, apoi lista `['ana', 'are', 'mere', 'dulci']`. Se afișează `aamd`.
4. Scrieți un program care citește de la tastatură `n`, apoi o listă de `n` numere întregi diferite și afișează media numerelor din listă, apoi cîte numere sînt mai mici decît media și cîte sînt mai mari decît media. Exemplu: se citește `n = 4`, apoi lista `[1, 6, -2, 4]`. Se afișează `media = 2.25`, apoi `2 numere mai mici` și `2 numere mai mari`.
5. Scrieți un program care citește de la tastatură un număr `n` de maximum 10 cifre și afișează dacă acesta este palindrom (adică dacă este egal cu răsturnatul său). Exemplu: se citește `n = 44155144` și se afișează `DA`.
6. Scrieți un program care să citească de la tastatură două numere `a` și `b` și să afișeze cele mai îndepărtate numere prime din intervalul `[a, b]`, precum și cele mai apropiate numere prime din acest interval. Dacă există mai multe perechi de numere prime la aceeași distanță minimă sau maximă, se afișează toate.
7. Listă de invitați: Scrieți un program care alcătuiește o listă de invitați, cu următorii pași:
	- se citește mai întîi lista de persoane pe care NU le vrem invitate ("lista neagră");
	- se citesc apoi invitații;
	- se respinge un invitat dacă este pe "lista neagră";
	- se respinge un nume dacă a mai fost deja invitat;
	- se adaugă invitați pe listă pînă la introducerea unui caracter special (de exemplu, `q` de la `quit` sau `x` de la `exit`);
	- se afișează lista finală de invitați permiși.
8. Scrieți un program care citește `n`, apoi o listă de `n` numere naturale, apoi un număr `a` și afișează lista citită, în care toți multipli de `a` au fost înlocuiți cu `*`.
9. Progresii aritmetice sau geometrice:
	- citiți de la tastatură o opțiune, `a` sau `g`;
	- citiți primul termen, `x`, rația `r` și numărul de termeni `n`;
	- afișați primii `n` termeni ai unei progresii aritmetice dacă s-a citit `a` la început sau geometrice dacă s-a citit `g`, care să înceapă cu `x` și să aibă rația `r`.
10. Scrieți un program care citește de la tastatură două perechi de numere reale, `(x1, y1)` și `(x2, y2)` și afișează lungimea segmentului determinat de cele două puncte. Formula de calcul este `sqrt((x1 - x2)^2 + (y1 - y2)^2)`.

## Grele
1. Implementați cifrul Caesar pe blocuri: citiți un cuvînt, apoi lungimea blocurilor și cheile, apoi afișați codul. Exemplu: cuvîntul este `laborator`, lungimea blocurilor este `4`, deci avem blocurile `labo`, `rato`, `r`. Așadar, vom citi 3 chei: `k1, k2, k3`. Pentru primul bloc se folosește `k1`, pentru al doilea, `k2`, iar pentru al treilea, `k3`. Lucrăm în `Z26`.
2. Scrieți un program care citește de la tastatură `n, a, b` și rezolvă ecuația `a * x + b = 0` în `Zn`.
3. Scrieți un program care citește de la tastatură `n` și afișează elementele inversabile din `Zn`, precum și inversele respective ale acestora.
4. Implementați cifrul afin: citiți un cuvînt, apoi două chei, `k1` și `k2`. Codul rezultat este `c * k1 + k2`, pentru fiecare caracter `c` din cuvînt. Lucrăm în `Z26`.
5. Implementați jocul *Spînzurătoarea*: computerul alege un cuvînt aleatoriu (nu trebuie să aibă sens), afișează numărul de litere, iar utilizatorul încearcă să ghicească literă cu literă, avînd dreptul la maximum 10 greșeli (de exemplu). Cînd jucătorul ghicește o literă, computerul afișează starea cuvîntului curent, cu literele ghicite și `_` pentru ce nu a ghicit încă. Cînd jucătorul greșește o literă, computerul îi spune cîte greșeli mai poate face.
