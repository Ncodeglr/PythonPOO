#---Définition class DateNaissance
class DateNaissance:
    def __init__(self,jour :int,mois :int,année :int):
        self.jour = jour
        self.mois = mois
        self.année = année
    def ToString(self):
        return str(self.jour) + "/" + str(self.mois) + "/" + str(self.année) 

#---Définition class Personne
class Personne:
    def __init__(self,nom :str,prenom :str,date_naissance :DateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    def Afficher(self):
        print("Nom & Prenom : " +self.nom + " "+self.prenom) 
        print("Date de naissance : " + self.date_naissance.ToString())

#---Définition class Employé qui hérite de la class Personne
class Employé(Personne):
    def __init__(self, nom: str, prenom: str, date_naissance: DateNaissance, salaire :int):
        super().__init__(nom, prenom, date_naissance)
        self.salaire = salaire
    def Afficher(self):
        super().Afficher()
        print("Salaire = " + str(self.salaire))

 #---Définition class Chef qui hérite de la class Employé
class Chef(Employé):
    def __init__(self, nom: str, prenom: str, date_naissance: DateNaissance, salaire: int, service :str):
        super().__init__(nom, prenom, date_naissance, salaire)
        self.service = service
    def Afficher(self):
        super().Afficher()
        print("Service : " + self.service)



#--Instanciation de la class Employé
emplo1 = Employé("Dupond","Etienne",DateNaissance(18,11,24),50000)
emplo1.Afficher()

#--Instanciation de la class Chef
chef1 = Chef("Durand","Lola",DateNaissance(8,3,94),100000,"IT")
chef1.Afficher()