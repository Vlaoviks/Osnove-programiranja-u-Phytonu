#kreirajte listu sa brojevima od 1 do 100

#u ovu svrhu ćemo koristiti funkciju range

#lista = []

#u ovoj varijanti argument predstavlja gornju granicu raspona (start je po defaultu 0)
#for broj in range(100):
 #   print(broj)

#u ovoj varijanti prvi broj predstavlja donju granicu intervala (ukljucivo), a drugi broj gornju granicu (iskljucivo)
#for broj in range(1,101):
#print(broj)


#krećemo od donje granice (ukljucivo) i sa korakom (treci argument) idemo do gornje granice (iskljucivo)
#for broj in range(1, 101 ,5):


#for broj in range(1, 101):
 #   lista.append(broj)

 #   print(lista)


#kreiraj novu listu, svaki drugi broj između 100 i 200

#lista = []

#for broj in range(100, 202, 2):
 #   lista_100_200.append(broj)

 #   print(lista_100_200)


#kreirajte listu sa brojevima os 100 do 1

#lista_100_1 = []



#for broj in range(100, 0, -1):
 ##   print(lista_100_1)

#lista_100_1[0] = 1000
#print(lista_100_1)
#print(len(lista_100_1))



#slice liste jako slično range funkciji
#lista[START:STOP:STEP]



#lista_1_100 = []
 #   lista_1_100.append(broj)
  #  for broj in slice(100, 0):
   # print(lista_1_100)


test_lista = [1, 2, 3]

#test_lista.clear() #briše sve elemente iz liste
#print(test_lista)

test_lista_2 = test_lista.copy()
print(test_lista_2)


test_lista[0] = 5
print(test_lista)
print(test_lista_2)

test_lista_3 = [5,7,5,8,5]
print(test_lista_3.count(5))

print(test_lista_3.index(5))

test_lista_4 = [7, 2]
#test_lista_3.append(test_lista_4)
#print(test_lista_3)
#print(test_lista_4[4][1])

test_lista_3.extend(test_lista_4)
print(test_lista_3)

test_lista_3.insert(3, 6)
print(test_lista_3)

test_lista_3.remove(7) # mičemo po vrijednostima npr.9
test_lista_3.remove(5)
print(test_lista_3)

test_lista_3.pop() #mičemo po indeksima
test_lista_3.pop(4) #dobijeno grešku jer index 4 ne postoji
print(test_lista_3)

#test_lista_3.sort() sortira od najmanjeg prema najvećem
#test_lista_3.sort(reverse=True) obrnuto sortiranje liste
print(test_lista_3)

test_lista_3.revese()
print(test_lista_3)