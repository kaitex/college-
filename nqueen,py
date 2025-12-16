def is_safe(board, row, col, n):
    # Check this column
    for i in range(row):
        if board[i] == col:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueen(board, row, n):
    if row == n:
        print(board)
        return True   # remove this if you want all solutions

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_nqueen(board, row + 1, n):
                return True
            board[row] = -1

    return False

def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print("Q" if board[i] == j else ".", end=" ")
        print()
    print()

# Driver code
n = 4
board = [-1] * n
solve_nqueen(board, 0, n)
print_board(board)