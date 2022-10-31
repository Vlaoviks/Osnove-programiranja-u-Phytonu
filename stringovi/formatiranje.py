"""
ime ="Pero"
prezime = "Peric"
print("Bok {} {}. Kako si danas?".format(ime, prezime))
print("Bok {} {}. Kako si danas?".format(ime,)) #ovo je krivo. dvije viticaste zagrade a jedna varijabla (ime)
print("Bok {}. Kako si danas?".format(ime, prezime))
"""


ime = "Pero"
godine = 20
punoljetan = True
zanimanje = "developer"

#print("{}, {}, {}, {} ". format(ime, godine, punoljetan, zanimanje))
#print("On se zove {}, ima {} godina, {}, Njegovo zanimanje je {} .". format(ime, godine, punoljetan, zanimanje))

#f-string

print(f"{ime} ima {godine} godina. Njegovo zanimanje je {zanimanje}")