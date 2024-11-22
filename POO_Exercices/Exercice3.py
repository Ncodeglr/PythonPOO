#https://www.youtube.com/watch?v=Y-wXK0Wu5pc&t=1024s

# POO EXERCICE DE MISE EN SITUATION 3

# ---
class Chat:
    def __init__(self, nom: str):
        if nom !="":
            self.nom = nom
        else:
            self.nom ="inconnu"

    def SePresenter(self):
       info_str = "Bonjour, je suis un chat et je m'appelle "
       print(info_str + self.nom)
     


# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je suis une personne et je m'appelle " + self.nom)

# ---
chat1 = Chat("")
chat1.SePresenter()  # Bonjour, je suis un chat et je m'appelle inconnu

chat2 = Chat("Garfield")
chat2.SePresenter()  # Bonjour, je suis un chat et je m'appelle Garfield

personne = Personne("Jean")
personne.SePresenter()  # Bonjour, je suis une personne et je m'appelle Jean
