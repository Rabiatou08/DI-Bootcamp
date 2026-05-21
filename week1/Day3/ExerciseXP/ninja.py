# Exercice 1 : Historique des appels
class Phone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    # Appeler un autre téléphone
    def call(self, other_phone):

        message = f"{self.phone_number} called {other_phone.phone_number}"

        print(message)

        # Ajouter dans l'historique des appels
        self.call_history.append(message)
        other_phone.call_history.append(message)

    # Afficher historique des appels
    def show_call_history(self):

        print("Call History:")

        for call in self.call_history:
            print(call)

    # Envoyer message
    def send_message(self, other_phone, content):

        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }

        self.messages.append(message)
        other_phone.messages.append(message)

        print("Message envoyé !")

    # Messages envoyés
    def show_outgoing_messages(self):

        print("Outgoing Messages:")

        for message in self.messages:
            if message["from"] == self.phone_number:
                print(message)

    # Messages reçus
    def show_incoming_messages(self):

        print("Incoming Messages:")

        for message in self.messages:
            if message["to"] == self.phone_number:
                print(message)

    # Messages d’un numéro spécifique
    def show_messages_from(self, number):

        print(f"Messages from {number}:")

        for message in self.messages:
            if message["from"] == number:
                print(message)


# TEST

phone1 = Phone("111")
phone2 = Phone("222")

# Appel
phone1.call(phone2)

# Historique
phone1.show_call_history()

# Envoyer message
phone1.send_message(phone2, "Salut !")
phone2.send_message(phone1, "Bonjour !")

# Voir messages
phone1.show_outgoing_messages()
phone1.show_incoming_messages()

phone2.show_messages_from("111")