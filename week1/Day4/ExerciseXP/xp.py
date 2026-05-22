# Exercice 1 : Animaux de compagnie

import random

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Étape 1 : Classe Siamese
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Étape 2 : Créer les objets
bengal_obj = Bengal("Simba", 3)
chartreux_obj = Chartreux("Luna", 5)
siamese_obj = Siamese("Milo", 2)

# Étape 3 : Créer la liste
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Étape 4 : Créer sara_pets et se promener
sara_pets = Pets(all_cats)
sara_pets.walk()

# Exercice 2 : Chiens
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} says woof!"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight
        if my_score > other_score:
            return f"{self.name} a gagné le combat !"
        else:
            return f"{other_dog.name} a gagné le combat !"

Dog1 = Dog("Rex", 5, 20)
Dog2 = Dog("Buddy", 3, 15)
Dog3 = Dog("Charlie", 4, 25)

print(Dog1.bark())
print(Dog2.run_speed())
print(Dog1.fight(Dog2))

# Exercice 3 : Chiens domestiqués

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = [self.name] + list(args)
        print(f"{', '.join(names)} sont tous en train de jouer ensemble !")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs",
                      "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} n'est pas encore dressé !")

# Test
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()

# Exercice 4 : Cours en famille et par personne
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18
class Family:
    def __init__(self, last_name, parent1, parent2):
        self.last_name = last_name
        self.parent1 = parent1
        self.parent2 = parent2
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)
        print(f"{first_name} {self.last_name} est né !")

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents {self.parent1} and {self.parent2} accept that you will go out with your friends")
                else:
                    print(f"Sorry, you are not allowed to go out with your friends.")
                return

    def family_presentation(self):
        print(f"Famille {self.last_name}")
        for member in self.members:
            print(f"  - {member.first_name}, {member.age} ans")

# Test
family = Family("Ouedraogo", "Aminata", "Moussa")
family.born("Rabiatou", 22)
family.born("Ridi", 3)
family.check_majority("Rabiatou")
family.check_majority("Ridi")
family.family_presentation()