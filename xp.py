# Exercice 1 : Les chats
# Créer la classe Cat
class Cat:

    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# Étape 1 : créer 3 chats
cat1 = Cat("wow", 4)
cat2 = Cat("wa", 5)
cat3 = Cat("wi", 6)


# Étape 2 : fonction pour trouver le plus vieux chat
def find_oldest_cat(cat1, cat2, cat3):

    oldest = cat1

    if cat2.age > oldest.age:
        oldest = cat2

    if cat3.age > oldest.age:
        oldest = cat3

    return oldest


# Étape 3 : afficher le chat le plus vieux
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

print(
    f"Le chat le plus âgé est {oldest_cat.name}, "
    f"et a {oldest_cat.age} ans."
)

# Exercice 2 : Chiens
class Dog:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} fait ouaf !")

    def jump(self):
        print(f"{self.name} saute {self.height * 2} cm de haut !")


# Étape 2 : créer les chiens
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 40)


# Étape 3 : afficher infos + appeler méthodes
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()


# Étape 4 : comparer les tailles
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} est le plus grand")
else:
    print(f"{sarahs_dog.name} est le plus grand")



    #  Exercice 3 : Qui est le producteur de la chanson ?

   
class Song:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# Créer une chanson
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Afficher les paroles
stairway.sing_me_a_song()

#  Exercice 4 : Après-midi au zoo
class Zoo:

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    # Ajouter animal
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    # Afficher animaux
    def get_animals(self):
        print(self.animals)

    # Vendre animal
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    # Trier animaux
    def sort_animals(self):
        self.animals.sort()

        groups = {}

        for animal in self.animals:
            first_letter = animal[0]

            if first_letter not in groups:
                groups[first_letter] = []

            groups[first_letter].append(animal)

        self.groups = groups

    # Afficher groupes
    def get_groups(self):
        for letter, animals in self.groups.items():
            print(letter, ":", animals)


# Créer le zoo
brooklyn_safari = Zoo("Brooklyn Safari")

# Ajouter animaux
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")

# Voir animaux
brooklyn_safari.get_animals()

# Vendre un animal
brooklyn_safari.sell_animal("Bear")

# Voir animaux après suppression
brooklyn_safari.get_animals()

# Trier et grouper
brooklyn_safari.sort_animals()

# Afficher groupes
brooklyn_safari.get_groups()

            