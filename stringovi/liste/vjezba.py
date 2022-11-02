# 1. kreirati listu u kojoj će biti
#svaki treći broj između 1 i 30

lista = []
for broj in range (1, 31, 3):
    lista.append(broj)
    print(lista)



# 2. Kreirajte novu listu na temelju liste iz
#prethodnog zadatka tako da vrijednog svakog
#elementa uvećate dvostruko.

lista_1_30 = []
for broj in lista:
    lista_1_30.append(broj*2)
    print(lista_1_30)

# 3.Napisati program koji ispisuje zbroj svih elemenata
#iz liste u drugom zadatku

zbroj = 0
for broj in lista_1_30:
    zbroj = zbroj + broj
    print(lista_1_30)
    print(sum(lista_1_30))
    print(zbroj)



#4. Napisati program koji od korisnika traži unos jednog
#broja koji želi izbaciti iz liste iz zadatka 2.
#izbaciti uneseni broj i ispišite novo stanje liste

broj = int(input( "unesite broj koji želite izbaciti s liste"))
lista_1_30.remove()
print(lista_1_30)





