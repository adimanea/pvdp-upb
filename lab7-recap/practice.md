# Exerciții diverse

Toate exercițiile de mai jos pot fi rezolvate în fișiere separate sau într-o singură foaie Jupyter.

De asemenea, datele se pot prelua de la tastatură sau dintr-un fișier sau, unde este cazul, se pot genera aleatoriu.

## Calcule și elemente de bază Python
1. Se dă un număr de maximum 10 cifre. Să se obțină numărul format prin eliminarea cifrelor de pe poziții impare.
Exemplu: `input = 12345678, output = 2468`.

2. Se dă un număr de maximum 10 cifre. Să se obțină răsturnatul lui.
Exemplu: `input = 12799874, output = 47899721`.

3. Se dă un număr de maximum 10 cifre. Să se verifice dacă este divizibil cu suma divizorilor săi.
Exemplu: `input = 100, suma divizorilor = 1 + 2 + 4 + 5 + 10 + 20 + 25 + 50 = 117, 100 nu este divizibil cu 117`.

4. Se dau două numere de maximum 5 cifre fiecare. Să se obțină numărul obținut prin întrepătrunderea cifrelor lor.
Exemplu: `a = 12345, b = 24680, output = 1224364850`.

5. Se citește de la tastatură un număr. Dacă acesta este par, se înjumătățește. Dacă este impar, se înmulțește cu 3 și se adună 1. Procedura se repetă pînă se ajunge la 1. Afișați acești pași.
Exemplu: `input = 20, output = 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.`

6. Se dau două numere naturale. Să se afișeze lista multiplilor primului număr, strict mai mici decît cel de-al doilea.
Exemplu: `a = 20, b = 200, output = 20 40 60 80 100 120 140 160 180`.

7. Se dă un număr de maximum 10 cifre. Să se afișeze dacă prima cifră a numărului este un divizor al ultimei cifre.
Exemplu: `input = 343489889, "da", deoarece 3 divide 9`.

8. Se dă un număr `x` de maximum 10 cifre și un indice `n`. Să afișeze a `n`-a cifră de la stînga a lui `x`.
Exemplu: `x = 128907478, n = 3, output = 8`.

9. Se dă un număr `x` de maximum 10 cifre și un indice `n`. Să se afișeze numărul format din a `n`-a cifră de la stînga și a `n`-a cifră de la dreapta ale lui `x`, în această ordine.
Exemplu: `x = 127987987, n = 3, output = 79`.

10. Se dă un număr `x` de maximum 10 cifre. Să se afișeze toți divizorii săi primi.
Exemplu: `x = 100, output = 2, 5`.

11. Se dă un număr `x` de maximum 10 cifre. Să se afișeze toți divizorii săi primi, cu tot cu puterea la care apar în descompunerea numărului.
Exemplu: `x = 100, output = (2, 2) (5, 2)`, pentru că `100 = 2^2 * 5^2`.

12. Se dă un număr `n` de la tastatură. Să se afișeze divizorii lui și numărul lor. Exemplu: `n = 20`, se afișează `1, 2, 4, 5, 10, 20` și `6 divizori`.
13. Se dă un număr `n` de la tastatură. Să se afișeze dacă este pătrat perfect. Exemplu: `n = 169`, se afișează `da`.
14. Se dă un număr `n` de la tastatură. Să se afișeze dacă este prim (nu are alți divizori în afară de 1 și el însuși). Exemplu: `n = 13`, se afișează `da`, `n = 20`, se afișează `nu`.
15. Se dau două numere `baza` și `exponent` de la tastatură. Să se afișeze `baza` la puterea `exponent`. Exemplu: `baza = 3`, `exponent = 4`, se afișează `81`.
16. Se dau două numere `n` și `p`. Să se afișeze cel mai mare multiplu al lui `n`, mai mic sau egal cu `p`. Exemplu: `n = 3, p = 20`, se afișează `18`.
17. Se dau două numere de la tastatură. Să se afișeze divizorii lor comuni. Exemplu: `n = 20, m = 12`, se afișează `1, 2, 4`.
18. Se dau două numere de la tastatură. Să se afișeze divizorii primi ai primului număr, care nu sînt și divizori ai celui de-al doilea număr. Exemplu: `n = 28, m = 30`, se afișează `7`.
19. Se dă un număr `n` de la tastatură și o listă de `n` numere naturale. Să se afișeze numărul din listă care are cei mai mulți divizori primi. Exemplu: `n = 5, [10, 20, 30, 40, 50]`, se afișează `30`.
20. Se dă un număr `n` de la tastatură. Să se afișeze toate numerele prime mai mici sau egale cu `n`. Exemplu: `n = 20`, se afișează `2, 3, 5, 7, 11, 13, 17, 19`.
21. Se dă un număr `n` de la tastatură. Să se afișeze suma divizorilor săi, precum și lista divizorilor acestei sume. Exemplu: `n = 20`, se afișează `Suma divizorilor: 1 + 2 + 4 + 5 + 10 + 20 = 42` și `[1, 2, 3, 6, 7, 14, 21, 42]`. 
22. Se dă un număr `n` de la tastatură, o listă de `n` numere naturale și un număr prim `p`. Să se afișeze care elemente ale listei sînt divizibile cu `p`. *Atenție:* Dacă numărul `p` introdus de la tastatură nu este prim, se afișează un mesaj și programul se închide. Exemplu: `n = 5, lista = [10, 20, 30, 40, 50], p = 3`. Se afișează `30`. Dacă `n = 5, lista = [10, 20, 30, 40, 50], p = 6`, se afișează `EROARE: reîncercați cu un număr prim!`.
23. Se dă un număr `n` de la tastatură și un număr `p`, prim. Să se afișeze dacă suma cifrelor lui `n` este divizibilă cu `p`. Ca în exemplul anterior, dacă `p` nu este prim, se afișează `EROARE`. Exemplu: `n = 1222, p = 7`, se afișează `DA`. Dacă `n = 1234442, p = 10`, se afișează `EROARE: Reîncercați cu un număr prim!`.
24. Se dă un număr `n` de la tastatură. Să se afișeze cel mai mare divizor prim al său. Exemplu: `n = 100`, se afișează `5`.
25. Se dă un număr `n` de la tastatură și o listă de `n` numere naturale. Să se afișeze lista cu numărul divizorilor lor. Exemplu: `n = 5, lista = [10, 20, 30, 40, 50]`, se afișează `[4, 6, 7, 8, 6]`.
26. Se dau două numere `n` și `m` de la tastatură. Să se afișeze cîte numere prime există între `n` și `m`, precum și lista acestora. Exemplu: `n = 10, m = 20`, se afișează `[11, 13, 17, 19]` și `4 numere prime`.

## Statistică și CSV
TBA.

## Grafice discrete
TBA.