#Google boje i logotipa.
#pomoću odgovarajućih naredbi za konverziju pokušajte
#Primjer:
#Naziv boje HEX zapis RGB (Red Green Blue)
#Crvena  #EA$335  (243,67,53)
#Znači, za HEX zapis EA-43-35 trebate dobiti RGB zapis 234-67-53
#zanemarite početni # znak u HEX zaspisu sa stranice
#HEX zapis čine tri grupe po dva znaka EA-43-35, svaka dva znaka čine jednu boju RGB
# 66 133 244
#  R  G   B



Blue = 4285F4

Blue_r = "42"
Blue_g = "85"
Blue_b = "F4"
RGB = 66 133 244

Red = DB4437
red_r = "DB"
red_g = "44"
red_b = "37"
RGB = 219 68 55
Yellow = F4B400
yellow_r = "F4"
yellow_g = "B4"
yellow_b = "00"
RGB = 244 180 0

Green = 0F9D58
green_r = "0F"
green_g = "9D"
green_b = "58"
RGB= 15 157 88

print("Hex Blue_1", blue_r, blue_g, blue_b, "=>RGB", int(blue_r, 16), int(blue_r, 16), int(blue_b, 16))
