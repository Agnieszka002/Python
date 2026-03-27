import random

# --- Board ---
board = {
    "A1": " ", "A2": " ", "A3": " ",
    "B1": " ", "B2": " ", "B3": " ",
    "C1": " ", "C2": " ", "C3": " "
}

# --- Function to display the board ---
def show_board():
    print(f" {board['A1']} | {board['A2']} | {board['A3']}")
    print("---+---+---")
    print(f" {board['B1']} | {board['B2']} | {board['B3']}")
    print("---+---+---")
    print(f" {board['C1']} | {board['C2']} | {board['C3']}")
    print()

# --- List of winning combinations ---
combinations = [
    ["A1","A2","A3"], ["B1","B2","B3"], ["C1","C2","C3"],
    ["A1","B1","C1"], ["A2","B2","C2"], ["A3","B3","C3"],
    ["A1","B2","C3"], ["A3","B2","C1"]
]

# --- Function to check winner ---
def check_winner():
    for c in combinations:
        if board[c[0]] == board[c[1]] == board[c[2]] != " ":
            return board[c[0]]  # returns winning symbol
    return None

# --- Computer AI function ---
def computer_move():
    # 50% chance to block player, 50% random move
    if random.random() < 0.5:
        # Try to block player if they have 2 in a row
        for c in combinations:
            values = [board[p] for p in c]
            if values.count(player_symbol) == 2 and values.count(" ") == 1:
                return c[values.index(" ")]
    # Random move
    empty_fields = [k for k, v in board.items() if v == " "]
    return random.choice(empty_fields)

# --- Player chooses symbol ---
player_symbol = input("Which symbol do you want to play? x or o?: ").lower()
while player_symbol not in ["x", "o"]:
    player_symbol = input("Invalid symbol. Enter x or o: ").lower()

computer_symbol = "o" if player_symbol == "x" else "x"

turn_input = input(f"Great! I will be {computer_symbol}. Who starts, me or you? (Type 'me' or 'you'): ").lower()
while turn_input not in ["me", "you"]:
    turn_input = input("Invalid answer. Type 'me' or 'you': ").lower()

turn = "player" if turn_input == "me" else "computer"

# --- Main game loop ---
game_on = True
while game_on:
    if turn == "player":  # player move
        move = input("Enter position, e.g. A1, B2: ").upper()
        if move in board and board[move] == " ":
            board[move] = player_symbol
            winner = check_winner()
            if winner:
                show_board()
                print(f"Congratulations! {winner} wins!")
                break
            elif " " not in board.values():
                show_board()
                print("Draw!")
                break
            turn = "computer"
        else:
            print("Invalid move, try again.")
    else:  # computer move
        move = computer_move()
        board[move] = computer_symbol
        print(f"Computer made a move: {move}")
        show_board()
        winner = check_winner()
        if winner:
            print(f"Computer wins! ({winner})")
            break
        elif " " not in board.values():
            print("Draw!")
            break
        turn = "player"
