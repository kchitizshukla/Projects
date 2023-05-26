board = [' ' for _ in range(9)]

def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

def make_move(player, position):
    board[position] = player

def is_winner(player):
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

def is_board_full():
    return ' ' not in board

# Start the game loop
current_player = 'X'
while True:
    print_board()
    position = int(input(f"Player {current_player}, make your move (1-9): ")) - 1
    if board[position] == ' ':
        make_move(current_player, position)
        if is_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif is_board_full():
            print_board()
            print("Tie game.")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("That position is already taken. Try again.")
