def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the current column
        for i in range(row):
            if board[i][col] == 1:
                return False
        
        # Check upper left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        # Check upper right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1
        
        return True
    
    def solve(board, row):
        # Base case: If all queens are placed
        if row >= n:
            return True
        
        # Try placing queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                if solve(board, row + 1):
                    return True
                # Backtrack
                board[row][col] = 0
        
        return False
    
    # Initialize the board with all zeros
    board = [[0] * n for _ in range(n)]
    
    # Start solving from the first row (row 0)
    if solve(board, 0):
        return board
    else:
        return None

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

# Get user input for the size of the chessboard (n)
while True:
    try:
        n = int(input("Enter the size of the chessboard (n >= 4): "))
        if n < 4:
            print("Please enter a number greater than or equal to 4.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Find solution for the N-Queens problem
solution = solve_n_queens(n)
if solution:
    print(f"Solution found for {n}-Queens problem:")
    print_board(solution)
else:
    print(f"No solution found for {n}-Queens problem.")
