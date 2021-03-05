gb = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # Game board cells
initial = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def game_board(board):  # Visualisation of board
    print('\n' * 100)
    print('   |   |   ')
    print(f' {gb[7]} | {gb[8]} | {gb[9]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {gb[4]} | {gb[5]} | {gb[6]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {gb[1]} | {gb[2]} | {gb[3]} ')
    print('   |   |   ')


def choose_marker():  # Player chooses what marker they want
    option = ['X', 'O']
    marker1 = 'place'
    while marker1 not in option:
        print("Choose between 'X' and 'O'")
        marker1 = input("Player 1, what would you like to be: ")
    option.remove(marker1)
    marker2 = option[0]
    return marker1, marker2


def player_input():
    pos = ''
    pos = input('Where would you like to go (1-9): ')
    while pos.isdigit() is False or int(pos) not in range(1, 10):  # Checks input is valid
        pos = input('Needs to be a number between 1-9: ')
    if space_check(gb, pos):  # Checks if space on board is available
        return int(pos)
    else:
        print('Space is full')
        return player_input()


def place_marker(board, marker, position):  # places either X or O in given position
    gb[position] = marker


def win(board, mark):  # Every winning position
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    else:
        return False


def space_check(board, position):  # Checks if given position is empty
    return board[int(position)] == ' '


def full_board_check(board):  # returns true if board is full
    return ' ' not in board


def replay():
    replst = ['Y', 'N']
    rep = ''
    rep = input('Would you like to play again? Y or N: ')
    while rep not in replst:
        print('Must be Y or N')
        rep = input('Would you like to play again? Y or N: ')
    if rep == 'Y':
        return True

    else:
        return False


print('Welcome to Tic Tac Toe!')


def full_game():
    marker1 = choose_marker()[0]
    if marker1 == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'

    game_board(gb)

    while win(gb, marker1) is False and win(gb, marker2) is False:
        place_marker(gb, marker1, player_input())
        game_board(gb)
        if win(gb, marker1):
            print('Congratulations, you won!')
            break
        else:
            pass
        if full_board_check(gb):
            print("Board full, it's a tie!")
            break
        else:
            pass

        place_marker(gb, marker2, player_input())
        game_board(gb)
        if win(gb, marker2):
            print('Congratulations, you won!')
            break
        else:
            pass
        if full_board_check(gb):
            print("Board full, it's a tie!")
            break
        else:
            pass


full_game()

while replay():
    gb = initial
    initial = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    full_game()

print('Thanks for playing!')
