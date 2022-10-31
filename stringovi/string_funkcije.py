ime = "Pero"
zanimanje = "developer"

"""
#Niže funkcije se primjenjuje samo sa stringovima. Ne sa brojevima
#lower ispisuje mala slova. Funkcija nije promjenila original string već je kreirala novi sa malim slovom.
print(ime.lower())

#upper ispisuje velika slova
print(zanimanje.upper())

#capitalize ispisuje prvo početno sloovo
print(zanimanje.capitalize())

#len ispisuje koliko string ima znakova
print(len(ime))
"""
#string je niz znakova. 
#svakom znaku možemo pristupiti putem njegovog indeksa.
#indexi kreću od 0. Pero- p je na poziciji 0.
# sintaksa za index je uglata zagrada []

"""
print(ime[0])
print(ime[1])
print(ime[2])
print(ime[3])
"""

#ispisujemo duljinu stringa u varijabli zanimanje
#te slova na prvoj, trećoj i petoj poziciji
"""
print(len(zanimanje))
print(zanimanje[0])
print(zanimanje[2])
print(zanimanje[4])
print(zanimanje[0], zanimanje[2], zanimanje[4])
"""
#String je nepromjenjiv. U istu varijablu (ime) dodali smo novi string(pepo) ali prvi, original se ne može promijeniti.
ime = "Pepo"

#ime[2] = "p"
#print(ime)

#ime_mala_slova = ime.lower()
#print(ime.lower())
#ime[0] = "p"
#print(ime)

ime_2 = "Pepo"

#želimo prebrojiti koliko se puta pojavilo određeno slovo
print(ime.count("e"))
print(zanimanje.count("e"))
print(ime_2.count("p"))
print(ime_2.lower().count("p"))

#želimo naći gdje nam se u našem stringu zanimanje pojavljuje slovo "e"

print(zanimanje.find("e"))  #vraća 1 - indeks prvog pojavljivanja slova "e" u riječi "developer"