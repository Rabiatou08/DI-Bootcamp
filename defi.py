
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
