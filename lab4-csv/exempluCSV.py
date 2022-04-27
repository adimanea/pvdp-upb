import csv

# citire din fișier
with open("inFile.csv", "r") as fisierCSV:
    listaDate = list(csv.reader(fisierCSV))
    print("Liniile din fișier, ca liste:")
    for linie in listaDate:
        print(linie)
    print(f"Elementul de pe poziția (1, 3) este {listaDate[1][3]}")

# scriem în fișier
linia1 = ['Oraș', '1-10', '11-20', '21-30', '31-40', '41-50']
linia2 = ['București', '4', '63', '31', '44', '55']
linia3 = ['Cluj', '42', '32', '55', '22', '11']
linia4 = ['Iași', '44', '66', '11', '22', '55']

# adăugăm encoding pentru probleme cu diacriticele
with open("outFile.csv", "w+",encoding="utf-8") as fisierCSV:
    scriere = csv.writer(fisierCSV)
    scriere.writerow(linia1)
    scriere.writerow(linia2)
    scriere.writerow(linia3)
    scriere.writerow(linia4)