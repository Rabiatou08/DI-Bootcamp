# Exercise1:Convertir des listes en dictionnaires
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)
# Exercice 2 : Cinemax n°2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# Variable pour le coût total
total_cost = 0

# Parcourir le dictionnaire
for name, age in family.items():

    # Vérifier le prix selon l'âge
    if age < 3:
        price = 0
    elif age >= 3 and age <= 12:
        price = 10
    else:
        price = 15

    # Afficher le prix du billet
    print(f"{name} doit payer {price}$")

    # Ajouter au total
    total_cost += price

# Afficher le coût total
print(f"Le coût total est : {total_cost}$")

#  Exercice 3 : Zara
# Créer le dictionnaire Zara
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Modifier le nombre de magasins
brand["number_stores"] = 2

# Afficher une phrase sur les vêtements
print("Zara vend des vêtements pour :", brand["type_of_clothes"])

# Ajouter country_creation
brand["country_creation"] = "Spain"

# Ajouter Desigual aux concurrents
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Supprimer creation_date
brand.pop("creation_date")

# Afficher le dernier concurrent
print("Dernier concurrent :", brand["international_competitors"][-1])

# Afficher les couleurs aux États-Unis
print("Couleurs aux US :", brand["major_color"]["US"])

# Nombre de clés
print("Nombre de clés :", len(brand))

# Afficher toutes les clés
print("Les clés sont :", brand.keys())

# BONUS 

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# Fusionner les dictionnaires
brand.update(more_on_zara)

# Afficher le résultat final
print(brand)


#  Exercice 4 : Un peu de géographie
def describe_city(city, country= "inconnu"):
  print(f"{city} est une ville située en {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Abidjan", "Côte d'Ivoire")

#  Exercice 5 : Aléatoire

import random

# Fonction avec un paramètre
def random_number(user_number):

    # Générer un nombre aléatoire
    random_num = random.randint(1, 100)

    # Comparer les nombres
    if user_number == random_num:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_num}")

# Appeler la fonction
random_number(50)

# Exercice 6 : Créons des t-shirts personnalisés !
# Fonction avec valeurs par défaut


def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

# Appels de la fonction
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="Custom message")

# Bonus
make_shirt(size="small", text="Hello!")

# Exercice 7 : Conseils sur la température
import random

# Étape 1 : Température aléatoire
def get_random_temp():
    return random.randint(-10, 40)

# Étape 2 & 3 : Fonction principale avec conseils
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, il fait un froid de canard ! Mets des vêtements supplémentaires.")
    elif temp < 16:
        print("Il fait assez froid ! N'oublie pas ton manteau.")
    elif temp < 24:
        print("Beau temps !")
    elif temp <= 32:
        print("Il fait un peu chaud, pense à bien t'hydrater.")
    else:
        print("Il fait vraiment chaud ! Reste au frais.")

main()
 # BONUS Étape 4 : Températures à virgule flottante
def get_random_temp():
    return round(random.uniform(-10, 40), 1)


# Exercice 8 : Garnitures de pizza
toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Entre une garniture (ou 'quit' pour terminer) : ")
    
    if topping == "quit":
        break
    
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

# Afficher le récapitulatif
print("\n--- Ta pizza ---")
print("Garnitures :")
for t in toppings:
    print(f"  - {t}")

total = base_price + (len(toppings) * topping_price)
print(f"\nPrix total : ${total:.2f}")