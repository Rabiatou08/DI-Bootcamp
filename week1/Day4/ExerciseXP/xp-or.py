# Exercice 1 : Compte bancaire

# Parties I, II, III
class BankAccount:
    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
        else:
            raise Exception("Nom d'utilisateur ou mot de passe incorrect.")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Vous devez être authentifié pour déposer.")
        if amount <= 0:
            raise Exception("Le montant doit être positif.")
        self.balance += amount
        print(f"Dépôt de {amount}€. Nouveau solde : {self.balance}€")

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Vous devez être authentifié pour retirer.")
        if amount <= 0:
            raise Exception("Le montant doit être positif.")
        self.balance -= amount
        print(f"Retrait de {amount}€. Nouveau solde : {self.balance}€")


# Partie II
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Vous devez être authentifié pour retirer.")
        if amount <= 0:
            raise Exception("Le montant doit être positif.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Solde insuffisant ! Minimum requis : {self.minimum_balance}€")
        self.balance -= amount
        print(f"Retrait de {amount}€. Nouveau solde : {self.balance}€")


# Partie IV BONUS : Guichet automatique
import sys

class ATM:
    def __init__(self, account_list, try_limit):
        # Vérifier que account_list contient des BankAccount
        for account in account_list:
            if not isinstance(account, BankAccount):
                raise Exception("La liste doit contenir des BankAccount.")

        # Vérifier que try_limit est positif
        try:
            if try_limit <= 0:
                raise Exception("try_limit doit être positif.")
        except Exception:
            print("try_limit invalide, valeur par défaut : 2")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Connexion")
            print("2. Quitter")
            choice = input("Votre choix : ")

            if choice == "1":
                username = input("Nom d'utilisateur : ")
                password = input("Mot de passe : ")
                self.log_in(username, password)
            elif choice == "2":
                print("Au revoir !")
                sys.exit()

    def log_in(self, username, password):
        for account in self.account_list:
            if account.username == username and account.password == password:
                account.authenticate(username, password)
                print("Connexion réussie !")
                self.current_tries = 0
                self.show_account_menu(account)
                return

        self.current_tries += 1
        print(f"Identifiants incorrects. Tentative {self.current_tries}/{self.try_limit}")

        if self.current_tries >= self.try_limit:
            print("Nombre maximum de tentatives atteint. Fermeture.")
            sys.exit()

    def show_account_menu(self, account):
        while True:
            print(f"\n=== MON COMPTE (Solde : {account.balance}€) ===")
            print("1. Déposer")
            print("2. Retirer")
            print("3. Quitter")
            choice = input("Votre choix : ")

            if choice == "1":
                amount = int(input("Montant à déposer : "))
                try:
                    account.deposit(amount)
                except Exception as e:
                    print(f"Erreur : {e}")
            elif choice == "2":
                amount = int(input("Montant à retirer : "))
                try:
                    account.withdraw(amount)
                except Exception as e:
                    print(f"Erreur : {e}")
            elif choice == "3":
                print("Déconnexion.")
                break


# Test
account1 = BankAccount(1000, "Rabiatou", "1234")
account2 = MinimumBalanceAccount(500, "Ridi", "5678", minimum_balance=100)

atm = ATM([account1, account2], try_limit=3)