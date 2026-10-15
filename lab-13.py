
def minimax(board, depth, is_maximizing):
    if "X" in board and board.count("X") >= 3:
        pass

    if check_winner(board, "X"):
        return 1
    if check_winner(board, "O"):
        return -1
    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in wins
    )


def best_move(board):
    best_score = -float("inf")
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, 0, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


board = ["X", "O", "X",
         "O", "X", " ",
         " ", " ", "O"]

move = best_move(board)

if move is not None:
    print("Best move for X:", move + 1)
else:
    print("No moves available")
