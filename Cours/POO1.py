#------Définition des class----------------#

#---
class ÊtreVivant:
    ESPECE_ÊTRE_VIVANT = "Être vivant non identifié" #Variable de class (1 pour toutes les instances)
    def afficherInfo(self):
        print("Info être vivant : "+ Personne.ESPECE_ÊTRE_VIVANT)

#---
class Chat(ÊtreVivant):
    ESPECE_ÊTRE_VIVANT = "Chat (Mamifère félin )" #Variable de class (1 pour toutes les instances)

#---
class Personne(ÊtreVivant):
    ESPECE_ÊTRE_VIVANT = "Humain (Mamifère Homo sapiens)" #Variable de class (1 pour toutes les instances)
    
    def __init__(self,nom: str="",age: int=0): #Constructeur de la class
        self.nom = nom
        self.age = age
        if nom =="":
            self.demanderNom()
        
    def sePresenter(self): #Méthode d'instance
        info_personne = "Bonjour, je m'appelle " + self.nom
        if self.age!=0: info_personne += ", j'ai " + str(self.age) + "ans"
        print(info_personne)
        
        if self.age!=0:
            if self.estMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
    
    def estMajeur(self):
        return self.age>=18
    
    def demanderNom(self):
        self.nom = input("Qu'elle est ton nom ? ")
   
#---
class Étudiant(Personne):
    def __init__(self,nom: str,age: int, etudes: str): #Constructeur de la class
        super().__init__(nom,age) #herite du constructueur du type Personne
        self.etudes = etudes
       
    
    def sePresenter(self):
        super().sePresenter() #Utilise la methode Personne puis rajoute des fonctions 
        print("Je suis étudiant en :" + self.etudes)


#----------------Utilisation-----------#
liste_personnes = [Personne("Nico",17),
                   Personne("Walhid",22),   #Liste d'objet Personne
                   Personne("Matt",21)] 

for Personne in liste_personnes:
    Personne.sePresenter()
    Personne.afficherInfo()

etudiant1 = Étudiant("Jean",20,"école d'ingénieur en informatique")
etudiant1.sePresenter()


