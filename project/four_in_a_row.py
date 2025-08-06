# Simple Four in a Row Game for Kids
# Players take turns dropping pieces to get 4 in a row!

def create_board():
    """Make an empty game board (6 rows, 7 columns)"""
    board = []
    for row in range(6):
        board.append([' '] * 7)  # 7 empty spaces in each row
    return board

def print_board(board):
    """Show the game board on screen"""
    print("\n  1 2 3 4 5 6 7")  # Column numbers
    print("  " + "-" * 13)
    
    for row in board:
        print("| " + " ".join(row) + " |")
    
    print("  " + "-" * 13)
    print("  1 2 3 4 5 6 7\n")

def drop_piece(board, column, piece):
    """Drop a game piece into the chosen column"""
    # Start from bottom row and go up
    for row in range(5, -1, -1):  # 5, 4, 3, 2, 1, 0
        if board[row][column] == ' ':
            board[row][column] = piece
            return True
    return False  # Column is full

def check_winner(board, piece):
    """Check if someone won the game"""
    
    # Check horizontal (left to right)
    for row in range(6):
        for col in range(4):  # Only check first 4 columns
            if (board[row][col] == piece and
                board[row][col + 1] == piece and
                board[row][col + 2] == piece and
                board[row][col + 3] == piece):
                return True
    
    # Check vertical (up and down)
    for row in range(3):  # Only check first 3 rows
        for col in range(7):
            if (board[row][col] == piece and
                board[row + 1][col] == piece and
                board[row + 2][col] == piece and
                board[row + 3][col] == piece):
                return True
    
    # Check diagonal (bottom-left to top-right)
    for row in range(3, 6):  # Start from row 3
        for col in range(4):
            if (board[row][col] == piece and
                board[row - 1][col + 1] == piece and
                board[row - 2][col + 2] == piece and
                board[row - 3][col + 3] == piece):
                return True
    
    # Check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if (board[row][col] == piece and
                board[row + 1][col + 1] == piece and
                board[row + 2][col + 2] == piece and
                board[row + 3][col + 3] == piece):
                return True
    
    return False

def is_board_full(board):
    """Check if the board is completely full"""
    for col in range(7):
        if board[0][col] == ' ':  # If top row has empty space
            return False
    return True

def play_game():
    """Main game function"""
    print("🎮 Welcome to Four in a Row! 🎮")
    print("Player 1 uses 'X' and Player 2 uses 'O'")
    print("Get 4 pieces in a row to win!")
    
    board = create_board()
    current_player = 1
    game_over = False
    
    while not game_over:
        print_board(board)
        
        # Show whose turn it is
        if current_player == 1:
            piece = 'X'
            print("Player 1's turn (X)")
        else:
            piece = 'O'
            print("Player 2's turn (O)")
        
        # Get player's choice
        try:
            column = int(input("Choose a column (1-7): ")) - 1
            
            # Check if column number is valid
            if column < 0 or column > 6:
                print("Please choose a number between 1 and 7!")
                continue
            
            # Try to drop the piece
            if drop_piece(board, column, piece):
                # Check if this player won
                if check_winner(board, piece):
                    print_board(board)
                    print(f"🎉 Player {current_player} wins! 🎉")
                    game_over = True
                
                # Check if board is full (tie game)
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie! Good game!")
                    game_over = True
                
                else:
                    # Switch to other player
                    if current_player == 1:
                        current_player = 2
                    else:
                        current_player = 1
            
            else:
                print("That column is full! Try another one.")
        
        except ValueError:
            print("Please enter a number!")

# Start the game!
if __name__ == "__main__":
    play_game()
    
    # Ask if they want to play again
    while True:
        play_again = input("Want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y']:
            play_game()
        elif play_again in ['no', 'n']:
            print("Thanks for playing! 👋")
            break
        else:
            print("Please type 'yes' or 'no'")
