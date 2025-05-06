#!/usr/bin/python3

def print_board(board):
    # Function to print the current game board.
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Function to check if there is a winner.
    # Checks all rows, columns, and diagonals for a win condition.
    
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    # Function to check if the game is a draw (no empty spaces left).
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    # Function to play the Tic-Tac-Toe game.
    board = [[" "]*3 for _ in range(3)]  # Initialize an empty 3x3 board.
    player = "X"
    
    while not check_winner(board):
        print_board(board)

        # Input validation for row and column
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                
                # Check if the input is valid (i.e., within bounds)
                if 0 <= row < 3 and 0 <= col < 3:
                    if board[row][col] == " ":
                        break
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid row or column. Please enter values between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 2.")
        
        # Place the player's mark on the board
        board[row][col] = player
        
        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            return  # End the game if it's a draw.
        
        # Switch player
        player = "O" if player == "X" else "X"

    # Print the final board and announce the winner
    print_board(board)
    print(f"Player {player} wins!")

# Run the game
tic_tac_toe()
