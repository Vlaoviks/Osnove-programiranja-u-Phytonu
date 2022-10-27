#Napisati program koji od korisnika traži unos
#polumjera kruznice te ispisuje njezinu povrsinu i opseg



from cmath import pi


polumjer = float(input("unesite polumjer kruznice: "))
#polumjer = input("unesite promjer kružnice: ")
#polumjer = float(polumjer)
pi = 3.14

opseg = 2 * polumjer * 3.14
povrsina = polumjer * polumjer * pi

print("opseg kruznice je", opseg)
print("povrsina_kruznice je",povrsina)
