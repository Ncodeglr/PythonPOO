#https://www.youtube.com/watch?v=Y-wXK0Wu5pc&t=1024s

# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
       print("Bonjour, je m'appelle " + self.nom)
       

# ---
nombre_personnes = 3
liste_personnes = []
for i in range(nombre_personnes):
    nom = input("nom de la personne")
    liste_personnes.append(Personne(nom))

for personne in liste_personnes:
    personne.SePresenter()