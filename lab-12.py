
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for turn in range(9):
        print_board(board)

        try:
            position = int(input(
                f"Player {player}, enter position (1-9): "
            ))
        except ValueError:
            print("Enter a valid number!")
            continue

        if position < 1 or position > 9:
            print("Choose a position from 1 to 9!")
            continue

        row = (position - 1) // 3
        col = (position - 1) % 3

        if board[row][col] != " ":
            print("Position already occupied! Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")


tic_tac_toe()
