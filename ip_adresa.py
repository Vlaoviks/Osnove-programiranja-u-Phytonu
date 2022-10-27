#IP adresa je adresa svakog računala na mreži koja se sastoji od četiri broja
#između 0 do 256. Primjer IP adrese: 192.168.0.184.
#Ip adresu iz primjera ispišite u binarnom, oktalnom i heksadekadskom obliku.
#savijet: koristite zasebnu varijablu za svaki od četiri brija
#odnosno dijela ( okteta) IP adrese
#ali ispišite ih u istom obliku kako je navedeno u primjeru ( 192.168.0.184.)
#Ispis treba napraviti za sve oblike brojevnih sustava

broj_1 = 192
broj_2 = 168
broj_3= 0
broj_4 = 184


print("Binarni oblik Ip adrease je: ", end="")
print(bin(broj_1), bin(broj_2), bin(broj_3), bin(broj_4), sep=".")
print("Heksadekadski oblik Ip adrease je: ", end="")
print(hex(broj_1), hex(broj_2), hex(broj_3), hex(broj_4), sep=".")
print("Oktalni oblik Ip adrease je: ", end="")
print(oct(broj_1), oct(broj_2), oct(broj_3), oct(broj_4), sep=".")

print(broj_1, broj_2, broj_3, broj_4, sep=".")
