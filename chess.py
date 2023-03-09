# print(" - - - - - - - -")
# for i in range(8):
#     print("| | | | | | | | |")
#     print(" - - - - - - - -")

# empty board
board = [[0] * 8 for i in range(8)]

# board with init positions (using nums for pieces)
# 1 = pawn   
# 2 = knight
# 3 = bishop
# 4 = rook
# 5 = queen
# 6 = king

# Pieces need to have color. so they should be at least a list of size 2. 
# [# of piece, isWhite (bool)

# Pawns on Board
for i in range(len(board)): 
    board[1][i] = [1, True]
for i in range(len(board)): 
    board[6][i] = [1, False]

# Knights on Board
board[0][1] = [2, True]
board[0][6] = [2, True]
board[7][1] = [2, False]
board[7][6] = [2, False]

# Bishops on Board
board[0][2] = [3, True]
board[0][5] = [3, True]
board[7][2] = [3, False]
board[7][5] = [3, False]

# Rooks on Board
board[0][0] = [4, True]
board[0][7] = [4, True]
board[7][0] = [4, False]
board[7][7] = [4, False]

# Queens on Board
board[0][3] = [5, True]
board[7][3] = [5, False]

# Kings on Board
board[0][4] = [5, True]
board[7][4] = [5, False]

# Start game
for i in range(len(board)-1, -1, -1):
    print(board[i])

game_over = False
whites_turn = True

while game_over is False:
    if whites_turn:
        user_input = input("White's turn: input piece letter you want to move (p, n, b, r, q, k) ")
    else:
        user_input = input("Black's turn: input piece letter you want to move (p, n, b, r, q, k) ")

    piece = user_input[0]

    match piece:
        case "p":
        case "n":
        case "b":
        case "r":
        case "q":
        case "k":
        case _:
            print("try again.")
            continue

    def check_if_piece_exists(piece):
        

        return

    # Check if piece exists (duplicates dont matter, just if piece of correct color is on the board)

    whites_turn = not whites_turn

    game_over = True