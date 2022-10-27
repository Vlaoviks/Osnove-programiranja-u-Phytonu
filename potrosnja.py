#Ako je snaga mikrovalne pećnice 1.3kW, a cijena el. energije za 1kwh je 0.95kn,
#koliko kuna, mjesečno, košta uporaba mikrovalne pećnice, ako se koristi 2h dnevno?
#zbog jednostavnosti zaokružimo svaki mjesec na 30dana
#Ispišite trošak bez i sa uračunatim PDV-om.

#Doradite program iznad tako da od korisnika tražite unos trenutne cijene električne energija
#te snagu uređaja za koji želi izračunati potrošnju

Snaga_mikrovalne = input(" kolika je snaga mikrovalne: ") 1.3 #kw
Cijena_struje_1kwh = 0.95 #kn
Dnevna_upotreba = 2 #h
Mjesečna_potrošnja = 

PDV = 25 #%


cijena = float(input("Unesite trenutnu cijenu el.energije: "))
snaga = float(input("Unesite snagu vašeg uređaja: "))
dnevna_uporaba = 2
mjesecna_uporaba = dnevna_uporaba * 30

mjesecni_trosak_bez_pdv = mjesecna_potrosnja * cijena 
mjesecni_trosak_pdv = mjesecni_trosak_bez_pdv * 1.25

print("mjesecni trosak bez PDV-a je: " mjesecni_trosak_bez_pdv, "kn")
print("mjesecni trosak sa PDV-om je: " mjescni_troska_pdv, "kn")



