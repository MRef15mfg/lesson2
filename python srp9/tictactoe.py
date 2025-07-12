import numpy as np
import os

height, width = 5, 5
field = np.full((height, width), " ", dtype=str)

def place_numbers():
    pos_num = 1
    field[:, 1] = "│"
    field[:, 3] = "│"
    field[1, :] = "─"
    field[3, :] = "─"
    for i in range(height):
        for q in range(width):
            if field[i, q] == " ":
                field[i, q] = str(pos_num)
                pos_num += 1

def display_field():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n     Tic-Tac-Toe\n")
    for row in field:
        print("  " + " ".join(f"{c:^3}" for c in row))

def get_move(turn):
    symbol = "X" if turn % 2 == 0 else "O"
    while True:
        user = input(f"\nPlayer {symbol}, choose a cell (1-9): ").strip()
        if not user.isdigit():
            print("  Please enter a number.")
            continue
        for i in range(height):
            for q in range(width):
                if field[i, q] == user:
                    field[i, q] = symbol
                    return True
        print("  Invalid move. Try again.")

def check_win():
    wins = [
        [(0,0), (0,2), (0,4)],
        [(2,0), (2,2), (2,4)],
        [(4,0), (4,2), (4,4)],
        [(0,0), (2,0), (4,0)],
        [(0,2), (2,2), (4,2)],
        [(0,4), (2,4), (4,4)],
        [(0,0), (2,2), (4,4)],
        [(0,4), (2,2), (4,0)]
    ]
    for combo in wins:
        cells = [field[i, q] for i, q in combo]
        if cells[0] in ['X', 'O'] and all(cell == cells[0] for cell in cells):
            return cells[0]
    return None

place_numbers()
turn = 0

while True:
    display_field()
    if not get_move(turn):
        continue
    winner = check_win()
    if winner:
        display_field()
        print(f"\nPlayer {winner} wins!")
        break
    turn += 1
    if turn >= 9:
        display_field()
        print("\nIt's a draw!")
        break
