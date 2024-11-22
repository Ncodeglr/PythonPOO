#https://www.youtube.com/watch?v=Y-wXK0Wu5pc&t=1024s


# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        info_personne = "Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans"
        
        print(info_personne)
        genre_str = "Masculin" if self.genre else "Feminin"
        print("Genre :" + genre_str)
        
        e_optionnel ="" if self.genre else "e"
        if self.EstMajeur():      
            print("Je suis majeur" + e_optionnel)
        else: 
            print("Je suis mineur" + e_optionnel)
        

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25,True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17,False)
personne2.SePresenter()