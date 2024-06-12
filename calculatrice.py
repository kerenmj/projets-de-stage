def caladd(xA,yA):
    resultatA = xA+yA
    return resultatA

def calsous(xB,yB):
    resultatB = xB-yB
    return resultatB

def calmul(xC,yC):
    resultatC = xC*yC
    return resultatC

def caldiv(xD,yD):
    resultatD = xD/yD
    return resultatD

xA = int(input("xA est:"))
yA = int(input("yA est:"))
print(caladd(xA,yA))

xB = int(input("xB est:"))
yB = int(input("yB est:"))
print(calsous(xB,yB))

xC = int(input("xC est:"))
yC = int(input("yC est:"))
print(calmul(xC,yC))

xD = int(input("xD est:"))
yD = int(input("yD est:"))
print(caldiv(xD,yD))
