
# Exercice 1 : Voitures

cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Convertir en liste
manufacturers = cars.split(", ")

# Nombre de fabricants
print(f"Il y a {len(manufacturers)} fabricants.")

# Ordre inverse (ZA)
manufacturers.sort(reverse=True)
print(manufacturers)

# Combien contiennent la lettre "o"
count_o = 0

for car in manufacturers:
    if "o" in car.lower():
        count_o += 1

print(f"{count_o} fabricants contiennent la lettre o.")

# Combien ne contiennent pas la lettre "i"
count_i = 0

for car in manufacturers:
    if "i" not in car.lower():
        count_i += 1

print(f"{count_i} fabricants ne contiennent pas la lettre i.")


# ===== Bonus 1 =====

cars_duplicate = [
    "Honda", "Volkswagen", "Toyota",
    "Ford Motor", "Honda",
    "Chevrolet", "Toyota"
]

# Supprimer doublons
unique_cars = list(set(cars_duplicate))

# Afficher en chaîne
print(", ".join(unique_cars))

print(f"Il y a maintenant {len(unique_cars)} entreprises.")


# ===== Bonus 2 =====

# Trier A-Z
unique_cars.sort()

print("Fabricants inversés :")

for car in unique_cars:
    print(car[::-1])


# Exercice 2 : Quel est votre nom ?


def get_full_name(first_name, last_name, middle_name=""):

    if middle_name == "":
        return first_name.capitalize() + " " + last_name.capitalize()

    else:
        return (
            first_name.capitalize()
            + " "
            + middle_name.capitalize()
            + " "
            + last_name.capitalize()
        )

# Test
print(get_full_name(
    first_name="john",
    middle_name="hooker",
    last_name="lee"
))

print(get_full_name(
    first_name="bruce",
    last_name="lee"
))





morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.",
    "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--.."
}


# Anglais → Morse
def english_to_morse(text):

    result = ""

    for letter in text.upper():

        if letter == " ":
            result += "/ "

        elif letter in morse_code:
            result += morse_code[letter] + " "

    return result


# Morse → Anglais
def morse_to_english(code):

    reverse_morse = {}

    for key, value in morse_code.items():
        reverse_morse[value] = key

    result = ""

    words = code.split(" / ")

    for word in words:

        letters = word.split()

        for letter in letters:
            result += reverse_morse[letter]

        result += " "

    return result


# Test
print(english_to_morse("HELLO"))
print(morse_to_english(".... . .-.. .-.. ---"))