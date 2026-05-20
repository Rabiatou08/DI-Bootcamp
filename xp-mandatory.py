# Exercise1:
print("Hello World \n" * 4)  

# Exercise2:

resultat= (int(99 ** 3))*8
print(resultat)

# Exercise3:
# Exercise3:
print(5 < 3)                 # False
print(3 == 3)                # True
# print("3" > 3)             # Error (str vs int)
print(3 == "3")              # False
print("Hello" == "hello")    # False

# Exercise4:
computer_brand = "HP"
print("I have a " + computer_brand + " computer")

# Exercise5:
name ="Rabiatou"
age= 22
shoe_size= 40
info = "My name is " + name + ", I am " + str(age) + " years old and my shoe size is " + str(shoe_size)
print(info)

# Exercise6: A et B

a = 15
b = 10
if a > b:
    print("Hello World")

    # Exercise7:
    input_number = int(input("Please enter a number: "))
    if input_number % 2 == 0:
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")

        # Exercise8:
        user_name = input("Quel est votre nom? ")
        if user_name == "Rabiatou":
               print("Incroyable! On partage le même nom, on est peut-être des jumelles secrètes ")
        else:
            print("Oups! Tu n'as pas le même nom que moi, mais on peut quand même être amis.")

# Exercise9:
taille= int(input("Entrez votre taille en centimètres: "))

if taille > 145:
    print("Vous êtes assez grand pour monter à cheval.")
else:
    print("Désolé, vous devez encore grandir pour monter à cheval.")