import random

board = [' ' for _ in range(9)]
player_symbol = ''
computer_symbol = ''

def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

def select_symbol():
    global player_symbol, computer_symbol
    while player_symbol not in ['X', 'O']:
        player_symbol = input("Select X or O: ").upper()
    if player_symbol == 'X':
        computer_symbol = 'O'
    else:
        computer_symbol = 'X'

def make_move(symbol, position):
    board[position] = symbol

def is_winner(symbol):
    return (board[0] == symbol and board[1] == symbol and board[2] == symbol) or \
           (board[3] == symbol and board[4] == symbol and board[5] == symbol) or \
           (board[6] == symbol and board[7] == symbol and board[8] == symbol) or \
           (board[0] == symbol and board[3] == symbol and board[6] == symbol) or \
           (board[1] == symbol and board[4] == symbol and board[7] == symbol) or \
           (board[2] == symbol and board[5] == symbol and board[8] == symbol) or \
           (board[0] == symbol and board[4] == symbol and board[8] == symbol) or \
           (board[2] == symbol and board[4] == symbol and board[6] == symbol)

def is_board_full():
    return all([x != ' ' for x in board])

def player_turn():
    position = -1
    while position not in range(1, 10) or board[position - 1] != ' ':
        position = int(input("Select a position (1-9): "))
    make_move(player_symbol, position - 1)

def computer_turn():
    position = random.randint(0, 8)
    while board[position] != ' ':
        position = random.randint(0, 8)
    make_move(computer_symbol, position)

def play_game():
    select_symbol()
    print_board()
    while True:
        player_turn()
        print_board()
        if is_winner(player_symbol):
            print("Congratulations! You won!")
            break
        if is_board_full():
            print("It's a tie!")
            break
        computer_turn()
        print_board()
        if is_winner(computer_symbol):
            print("Sorry, you lost!")
            break
        if is_board_full():
            print("It's a tie!")
            break

play_game()
