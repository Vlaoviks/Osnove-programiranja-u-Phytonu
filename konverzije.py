broj = "5"
rijec = "bla"

broj_int = int(broj)
print(type(broj_int)) #funkcija type nam ispisuje kojeg je varijabla

broj_float = float(broj)
print(broj_float, type(broj_float))

broj_2= 10
broj_2_string = str(broj_2)
print(broj_2_string, type(broj_2_string))

print(bool(broj))
print(bool(rijec))
print(bool(broj_2))
print(bool("False"))
print(bool("")) #prazan string "", boolean će dati odgovor False, sve ostale kombinacije su True.
print(bool(" "))
print(bool(0))  # ako ubacimo 0 boolean će dati odgovor False


broj_2_binarni = bin(broj_2)
print(bin(broj_2))
broj_2_heksadekadski = hex(broj_2)
print(broj_2_heksadekadski)
broj_2 oktalni = oct(broj_2)
print(broj_2_oktalni)

bla = F
bla_dekadski = int(bls, base = 16)
