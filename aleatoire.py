import random
nombre=random.randint(1,100)

essaie = 0

while True:
    essaie =+ 1
    x = int(input("Rentrez le nombre de votre choix : "))
    
    if nombre > x :
       print("plus grand")
    elif nombre < x :
       print("plus petit")
    else :
       print("vous avez trouvez le nombre!!!")
       print(nombre)
       break