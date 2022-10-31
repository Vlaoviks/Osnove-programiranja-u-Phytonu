moja_lista = ["Pero", 20, True, "developer", "bla", False]
prazna_lista = [] #prazna lista

#print(moja_lista)

#elementima liste pristupamo putem njihovih indeksa
#indeksi u listi kreću od 0

#print(moja_lista[0])
#print(prazna_lista[0]) #dobijemo grešku jer pristupamo indeksu koji ne postoji

#možemo zamijeniti vrijednost elemenata na određenom indeksu
moja_lista [0] = "Perić"
#print(moja_lista)

#Kreirajte listu sa brojevima od 1 do 5

lista_brojevi = [1, 2, 3, 4, 5]
#print(lista_brojevi[0])
#print(lista_brojevi[4])

#ispis zadnjeg elementa u listi
#print(lista_brojevi[4])

#indeksi mogu biti i negativni - znači da idemo u suprotnom smjeru po
#print(lista_brojevi[-1])

#kako prebrojiti broj elemenata u listi?

#print(len(lista_brojevi))

#print(lista_brojevi[len(lista_brojevi) - 1])

#primjer
osoba = ["Pero", "Perić", "Ilica 35", "Zagreb", "10000", "01234567"]
#print(osoba[-1])
#osoba je varijabla, iza uglate zagrade je lista

#print(osoba[])

#ako želimo ispisati sve elemente u listi, potrebna nam je for petlja
"""
for element in osoba: 
    print(element)
    print(osoba)

for element in osoba: 
        print(element)
print(osoba)
"""


"""
for index, element in enumerate(osoba):
    #print(index, element)
#print(osoba)


#kreiraj listi od deset brojeva i ispiši u istom retku.
"""


lista_bla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(brojevi)

for element in lista_bla:
    print(element, end=" ")


    