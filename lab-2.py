def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    # Base case: If all queens are placed, return True
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen from board[i][col] (Backtrack)
            board[i][col] = 0

    return False

def solve_8_queens():
    n = 8
    # Initialize an 8x8 board with 0s
    board = [[0] * n for _ in range(n)]

    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    # Print the visual board layout
    for row in board:
        print(" ".join("👑" if cell == 1 else " . " for cell in row))
    return True

# Run the program
solve_8_queens()
