# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if a player has won
def check_winner(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to make a move
def make_move(player, position):
    board[position] = player

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()
        position = int(input("Player " + current_player + ", enter a position (1-9): ")) - 1

        if board[position] == ' ':
            make_move(current_player, position)
            if check_winner(current_player):
                display_board()
                print("Player " + current_player + " wins!")
                game_over = True
            elif is_board_full():
                display_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already filled. Try again.")
