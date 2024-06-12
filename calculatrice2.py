def caladd(xA,yA):
    resultatA = xA+yA
    return resultatA

def calsous(xA,yA):
    resultatB = xA-yA
    return resultatB

def calmul(xA,yA):
    resultatC = xA*yA
    return resultatC

def caldiv(xA,yA):
    resultatD = xA/yA
    return resultatD

print("quelle opération veux-tu faire ?")
print("1- addition")
print("2-soustraction")
print("3-multiplication")
print("4-division")


choix = input("choississez entre 1/2/3/4 : ")
xA = int(input("le num 1 est:"))
yA = int(input("le num 2 est:"))

print ("le resultat est :")

if choix == '1' :
    print(caladd(xA,yA))
elif choix == '2' :
    print(calsous(xA,yA))
elif choix == '3' :
    print(calmul(xA,yA))
elif choix == '4' :
    print(caldiv(xA,yA))
else:
    print("choix invalide")
    
    