board = [" "] * 9

def display_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def player_input(player):
    while True:
        try:
            pos = int(input(f"Joueur {player}, choisissez une position (1-9) : ")) - 1
            if 0 <= pos <= 8 and board[pos] == " ":
                return pos
            else:
                print("Position invalide ou déjà prise. Réessaie.")
        except ValueError:
            print("Entre un nombre entre 1 et 9.")

def check_win():
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # lignes
        [0,3,6], [1,4,7], [2,5,8],  # colonnes
        [0,4,8], [2,4,6]             # diagonales
    ]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]  # retourne "X" ou "O"
    return None

def check_draw():
    return " " not in board

def play():
    player = "X"
    print("=== TIC TAC TOE ===")
    print("Cases numérotées de 1 à 9 :")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        display_board()
        pos = player_input(player)
        board[pos] = player

        winner = check_win()
        if winner:
            display_board()
            print(f" Joueur {winner} a gagné !")
            break

        if check_draw():
            display_board()
            print(" Égalité !")
            break

        player = "O" if player == "X" else "X"

play()