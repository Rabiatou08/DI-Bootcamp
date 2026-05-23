# game.py
import random

class Game:
    def get_user_item(self):
        while True:
            user_item = input("Choisissez pierre, papier ou ciseaux : ").lower()
            if user_item in ["pierre", "papier", "ciseaux"]:
                return user_item
            print("Choix invalide ! Réessaie.")

    def get_computer_item(self):
        return random.choice(["pierre", "papier", "ciseaux"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "pierre" and computer_item == "ciseaux") or \
             (user_item == "ciseaux" and computer_item == "papier") or \
             (user_item == "papier" and computer_item == "pierre"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        if result == "win":
            print(f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez gagné ! ")
        elif result == "draw":
            print(f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Égalité ! ")
        else:
            print(f"Vous avez choisi {user_item}. L'ordinateur a choisi {computer_item}. Vous avez perdu ! ")

        return result