<<<<<<< HEAD
# Défi 1 : Dictionnaire d’index des lettres
mot = input("Entrez un mot :")
dictionnaire={}
for index, caractere in enumerate(mot):
    if caractere in dictionnaire :
        dictionnaire[caractere].append(index)
    else:
        dictionnaire[caractere]=[index]
        print(dictionnaire)


# Défi 2 : Articles abordables

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Étape 1 : Nettoyer le wallet
wallet = int(wallet.replace("$", "").replace(",", ""))

# Étape 2 : Trouver les articles abordables
basket = []

for item, price in items_purchase.items():
    price = int(price.replace("$", "").replace(",", ""))
    
    if price <= wallet:
        basket.append(item)
        wallet -= price

# Étape 3 : Afficher le résultat
if basket:
    print(sorted(basket))
else:
    print("Nothing")
    
=======
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
>>>>>>> 52b2a9315ed4a929861e3ea797fdb0f09dd86c3a
