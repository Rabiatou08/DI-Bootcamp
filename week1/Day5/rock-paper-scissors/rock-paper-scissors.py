# rock-paper-scissors.py
from game import Game

def get_user_menu_choice():
    print("\n=== MENU ===")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores")
    print("q. Quitter")
    choice = input("Votre choix : ").lower()
    return choice

def print_results(results):
    print("\n=== RÉSUMÉ DES PARTIES ===")
    print(f" Victoires : {results['win']}")
    print(f" Défaites  : {results['loss']}")
    print(f" Égalités  : {results['draw']}")
    print("Merci d'avoir joué ! À bientôt ")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == "2":
            print_results(results)

        elif choice == "q":
            print_results(results)
            break

        else:
            print("Choix invalide ! Réessaie.")

main()