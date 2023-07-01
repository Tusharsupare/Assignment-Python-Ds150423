def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if the current position is safe for the queen
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(board, col, solutions):
        if col >= n:
            solutions.append([''.join(row) for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                solve(board, col + 1, solutions)
                board[i][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(board, 0, solutions)
    return solutions

# Example usage
n = 4
solutions = solve_n_queens(n)

print(f"Number of solutions for {n}-Queens problem: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()