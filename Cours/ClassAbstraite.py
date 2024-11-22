from abc import ABC, abstractmethod

#--Class Abstraite
class Widget(ABC):
    def test(self):
        print("Test !")
    
    @abstractmethod #Méthode Abstraite
    def render(self):
        pass

#--Class Concrète 
class Button(Widget):
    
    def render(self): #Récriture de la méthode abstraite hérité de la class abstraite Widget
        print("Rendu d'un button")

