import random

def adverse() :
    return random.choice(['pierre','papier','ciseaux'])
     

def qui_gagne(ordinateur,people):
    if adverse == people :
        print("Vous etes à égalité!")
    elif people == "pierre" and ordinateur == "ciseaux" or people == "papier" and ordinateur == "pierre" or people == "ciseaux" and ordinateur == "papier" :
        print("vous avez gagné!")
    else :
        print("l'ordinqteur a gagné!!")    
    return

people = input("choisissez entre pierre, papier et ciseaux : ")

ordinateur = adverse()

print("votre choix est : ", people)
print("le choix de l'ordinateur est : ", ordinateur)

print(qui_gagne(ordinateur,people))