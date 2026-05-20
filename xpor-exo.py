
# Exercice 1 : Anniversaires


birthdays = {
    "Rabiatou": "2004/06/08",
    "Noura": "2003/12/28",
    "Mariam": "2003/01/10",
    "Djemila": "2005/11/10",
    "Frean": "2005/03/30"
}

print("Bienvenue !")
print("Vous pouvez consulter les dates d'anniversaire des personnes de la liste.")

name = input("Entrez un nom : ")

if name in birthdays:
    print(f"La date d'anniversaire de {name} est {birthdays[name]}")
else:
    print(f"Désolé, nous n'avons pas d'informations sur {name}")


# Exercice 2 : Anniversaires avancé

print("\nListe des personnes :")

for person in birthdays:
    print(person)

name = input("Choisissez un nom : ")

if name in birthdays:
    print(f"La date d'anniversaire de {name} est {birthdays[name]}")
else:
    print(f"Désolé, nous ne disposons pas des informations concernant la date de naissance de {name}")


# Exercice 3 : Consultez l'index


names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Entrez un nom : ")

if user_name in names:
    print(names.index(user_name))
else:
    print("Nom non trouvé")


# Exercice 4 : Double dés


import random

# Fonction pour lancer un dé
def throw_dice():
    return random.randint(1, 6)

# Fonction jusqu'à obtenir un double
def throw_until_doubles():

    throws = 0

    while True:

        dice1 = throw_dice()
        dice2 = throw_dice()

        throws += 1

        if dice1 == dice2:
            return throws

# Fonction principale
def main():

    results = []

    # Faire 100 essais
    for i in range(100):
        result = throw_until_doubles()
        results.append(result)

    # Calcul total
    total_throws = sum(results)

    # Moyenne
    average = total_throws / len(results)

    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {round(average, 2)}")

# Exécuter le programme
main()