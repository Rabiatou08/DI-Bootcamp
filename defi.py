# Défi 1
# Demander un nombre et une longueur
number = int(input("Entrez un nombre : "))
length = int(input("Entrez une longueur : "))

# Créer une liste vide
multiples = []

# Ajouter les multiples
for i in range(1, length + 1):
    multiples.append(number * i)

# Afficher la liste
print(multiples)


# Défi 2
# Demander une chaîne à l'utilisateur
chaine = input("Entrez une chaîne de caractères : ")

# Créer une nouvelle chaîne
nouvelle_chaine = ""

# Parcourir les caractères
for lettre in chaine:
    # Ajouter seulement si différente de la précédente
    if len(nouvelle_chaine) == 0 or lettre != nouvelle_chaine[-1]:
        nouvelle_chaine += lettre

# Afficher le résultat
print("Nouvelle chaîne :", nouvelle_chaine)