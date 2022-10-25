from __future__ import print_function


ime = "Sara" # String
prezime = "Maric" # string
godina_rodenja = 2009 # integer
drzava_rodenja = "Hrvatska" # string
status_radnog_odnosa = "student" # string
tezina = 45.1 # float
spol = "Z" # string
#TODO ovo odraditi kasnije
punoljetan = True #boolean tip podataka, True or False 

print(ime, prezime, godina_rodenja, drzava_rodenja, tezina, status_radnog_odnosa, spol)

broj_a = 12
broj_b = 4
povrsina = broj_a * broj_b
print (povrsina)

#moze se racunati na vise nacina
a, b = 12, 4
povrsina = a * b
print (povrsina)

snaga_mikrovalne = 1.3 # kw_struje
dnevna_upotreba = 2 #h
pmjesecna_upotreba = 30
cijena_struje= 0.56
mjesecna_upotreba = dnevna_upotreba * 30
mjesecna_potrosnja = mjesecna_upotreba * snaga_mikrovalne
mjesecni_trosak = mjesecna_potrosnja * cijena_struje