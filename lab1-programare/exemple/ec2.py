# Programul rezolvă ecuații de gradul al doilea, 
# cu coeficienți și rădăcini reale.

import math

print("Programul rezolvă ecuații de gradul al doilea, de forma a * x^2 + b * x + c = 0.")
a = int(input("Introduceți coeficientul a: "))
b = int(input("Introduceți coeficientul b: "))
c = int(input("Introduceți coeficientul c: "))

delta = b**2 - 4 * a * c
if delta < 0:
	print(f"Delta = {delta} < 0, deci ecuația nu are rădăcini reale.")
	exit()

x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b + math.sqrt(delta)) / (2*a)

# afișăm rădăcinile cu doar 3 zecimale, pentru simplitate
print(f"Delta = {delta}.")
print(f"Rădăcinile ecuației sînt: x1 = {round(x1, 3)}, x2 = {round(x2, 3)}")