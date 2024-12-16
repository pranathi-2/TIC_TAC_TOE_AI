import math
# Displaying the Tic-Tac-Toe board
def print_the_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print()
# Checking if the board is full (draw)
def is_full(board):
    for row in board:
        if any(cell == " " for cell in row):
            return False
    return True
# Checking if there's a winner
def check_winner(board, player):
    # Checking the rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
# Get all the available moves
def get_available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
# Minimax with Alpha-Beta Pruning alg
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "O"): # AI wins
        return 10 - depth
    if check_winner(board, "X"): # Human wins
        return depth - 10
    if is_full(board): # Draw
        return 0
    if is_maximizing:
        max_eval = -math.inf
        for row, col in get_available_moves(board):
            board[row][col] = "O"
            eval_score = minimax(board, depth + 1, False, alpha, beta)
            board[row][col] = " "
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for row, col in get_available_moves(board):
            board[row][col] = "X"
            eval_score = minimax(board, depth + 1, True, alpha, beta)
            board[row][col] = " "
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval
# Finds the best move for the AI
def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for row, col in get_available_moves(board):
        board[row][col] = "O"
        move_score = minimax(board, 0, False, -math.inf, math.inf)
        board[row][col] = " "
        if move_score > best_score:
            best_score = move_score
            best_move = (row, col)
    return best_move
# Main game
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X' and AI is 'O'.")
    print_the_board(board)
    while True:
        # Humans move
        while True:
            try:
                move = input("Enter your move (row and column, e.g., 1 2): ").split()
                row, col = int(move[0]) - 1, int(move[1]) - 1
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column numbers (1-3).")
        print("Your move:")
        print_the_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!🎉")
            break
        if is_full(board):
            print("It's a draw! 🤝")
            break
        # AI move
        print("AI's turn...")
        row, col = find_best_move(board)
        board[row][col] = "O"
        print_the_board(board)
        if check_winner(board, "O"):
            print("AI wins! Better luck next time!")
            break
        if is_full(board):
            print("It's a draw! 🤝")
            break
# Start the game here
play_tic_tac_toe()
