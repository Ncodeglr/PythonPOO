from math import *

#--Définition de la class Cercle
class Cercle:
    def __init__(self,rayon) :
        self.rayonCercle = rayon
    
    def Aire(self):
        aireCercle = pi*pow(self.rayonCercle,2)
        return aireCercle
    
    def Périmètre(self):
        périmetreCercle = 2*pi*self.rayonCercle
        return périmetreCercle
    
#--Définition de la class Calcul
class Calcul:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def Factorielle(self):
        if self.nombre == 0 or self.nombre == 1:
            return 1
        else:
            return self.nombre * Calcul(self.nombre - 1).Factorielle()  # Recursive call
    
    def diviseurNombre(self):
        liste_diviseur = []
        k=1
        while(k<=self.nombre):
            if(self.nombre%k == 0):
                liste_diviseur.append(k)
            k+=1
        return liste_diviseur
    
    def testNombrePremier(self):
        if len(self.diviseurNombre()) == 2:
            print("Ce nombre est premier")
        else:
            print("Ce nombre n'est pas premier")


#---Définition de la class GestionCptB
class GestionCptB:
    def __init__(self,numcompte,nom,solde):
        self.nCompte = numcompte
        self.nomClient = nom
        self.soldeCompte = solde
    
    def Versement(self,montantVersement):
        print("Versement")
        self.soldeCompte +=montantVersement
        print("Solde du Compte = ",self.soldeCompte)
        return self.soldeCompte
    
    def Retrait(self,montantRetrait):
        if self.soldeCompte < montantRetrait:
            print("Impossible, pas assez d'argent sur le compte")
        else:
            print("Retrait")
            self.soldeCompte -=montantRetrait
        return self.soldeCompte
    
    def afficherInfo(self):
        print("Numéro de Compte : ", self.nCompte)
        print("Nom du Client : "+ str(self.nomClient))
        print("Solde du Compte : ", self.soldeCompte)

#--Définition de la class Eleve
class Eleve:
    def __init__(self,nom :str,prenom :str,list_note :list):
        self.nom = nom
        self.prenom = prenom
        self.list_note = list_note

    def Moyenne(self):
        return sum(self.list_note)/len(self.list_note)
    
    def __str__(self):
       return "Nom & Prenom" +self.nom +self.prenom+"\n"+"Moyenne = "+str(self.Moyenne())

#---Fonction Factorielle avec de la récursivité
def calculFactorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculFactorielle(n - 1)  # Recursive call
    
   
#--Instanciation de la class Cercle
cercle1 = Cercle(5) #Objet de type Cercle
print(cercle1.Aire())
print(round(cercle1.Périmètre(),2)) #Approximation avec 2 chifferes après la virgule

#--Instanciation de la class Calcul  
calcul1 = Calcul(4)
print(calcul1.Factorielle())
print(calcul1.diviseurNombre())
calcul1.testNombrePremier()

#--Instanciation de la class GestionCptB
compteBancaire1 = GestionCptB("Nico",19199292,1200)
compteBancaire1.afficherInfo()
compteBancaire1.Retrait(1400)
compteBancaire1.Versement(66783)

#--Instanciation de la class Eleve
eleve1 = Eleve("Dupond","Nathan",[10,16,11,12,13])
print(eleve1)
