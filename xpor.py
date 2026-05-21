# Exercice 1 : Géométrie
import math

class Circle:

    def __init__(self, rayon=1.0):
        self.rayon = rayon

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def definition(self):
        print("Un cercle est une figure géométrique ronde dont tous les points sont à la même distance du centre.")


# Créer un cercle
cercle1 = Circle(5)

# Afficher les résultats
print("Périmètre :", cercle1.perimetre())
print("Aire :", cercle1.aire())
cercle1.definition()

# Exercice 2 : Classe de liste personnalisée
import random

class MyList:

    def __init__(self, letters):
        self.letters = letters

    # Liste inversée
    def reverse_list(self):
        return self.letters[::-1]

    # Liste triée
    def sort_list(self):
        return sorted(self.letters)

    # Bonus : liste aléatoire
    def random_numbers(self):
        return [random.randint(1, 100) for i in range(len(self.letters))]


# Créer un objet
my_list = MyList(["b", "g", "a", "d", "f"])

# Tester les méthodes
print("Liste originale :", my_list.letters)
print("Liste inversée :", my_list.reverse_list())
print("Liste triée :", my_list.sort_list())
print("Liste aléatoire :", my_list.random_numbers())

# Exercice 3 : Gestionnaire de menu de restaurant

class MenuManager:

    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    # Ajouter un plat
    def add_item(self, name, price, spice, gluten):

        new_dish = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }

        self.menu.append(new_dish)
        print(f"{name} ajouté au menu.")

    # Modifier un plat
    def update_item(self, name, price, spice, gluten):

        for dish in self.menu:

            if dish["name"] == name:
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten

                print(f"{name} a été mis à jour.")
                return

        print("Ce plat n'est pas au menu.")

    # Supprimer un plat
    def remove_item(self, name):

        for dish in self.menu:

            if dish["name"] == name:
                self.menu.remove(dish)

                print(f"{name} supprimé du menu.")
                print(self.menu)
                return

        print("Ce plat n'est pas au menu.")


# Créer le menu
restaurant = MenuManager()

# Ajouter un plat
restaurant.add_item("Pizza", 20, "B", True)

# Modifier un plat
restaurant.update_item("Soup", 12, "C", False)

# Supprimer un plat
restaurant.remove_item("Salad")

