ime = "Pero"
godine = 20
punoljetan = True
zanimanje = "developer"

print(ime, godine, punoljetan, zanimanje, sep= "\n") # predstavlja skok u novi red sa naredbom "\n"
print(ime, end=",") # ispisuje se sve do ,
print(ime, godine, punoljetan, sep=":", end=";")

print(ime, "ima", godine, "godina.", end= " ")
print("Njegovo zanimanje je", zanimanje)
print("to je to za danas.")