###
### Author: Navneeth Mohan Kunkatla.
### Description: A program that uses graphics to print out
###              a 1 dimensional chess board that can be played
###              with the king and 2 knight pieces

from graphics import graphics

W_KNIGHT = 'WKn'
W_KING   = 'WKi'
B_KNIGHT = 'BKn'
B_KING   = 'BKi'
EMPTY    = '   '
WHITE    = 'White'
BLACK    = 'Black'
LEFT     = 'l'
RIGHT    = 'r'

def is_valid_move(board, position, player):
###Checks whether user move and input are valid
    if len(board)>position >=0:
        if player=='Black':
            if board[position]=='BKn' or board[position]=='BKi':
                return True
            else:
                return False
        else:
            if board[position]=='WKn' or board[position]=='WKi':
                return True
            else:
                return False

def move_knight(board, position, direction):
###Moving the Knight
    if direction =='r'and position + 2 <= len(board) :

        board[position+2]=board[position]
        board[position]=EMPTY

    elif direction == 'l'and position - 2 >= 0 :

        board[position - 2] = board[position]
        board[position] = EMPTY

def move_king(board, position, direction):
###Moving the King
###halt is used to know if the piece has reached the end
    if direction=='r':
        i=position+1
        halt = False
        while i<len(board) and not halt:
            if board[i]!=EMPTY or i==8:
                board[i]=board[position]
                board[position]=EMPTY
                halt = True
            else:
                i+=1
    elif direction=='l':
        i=position-1
        halt = False
        while i>=0 and not halt:
            if board[i]!=EMPTY or i==0:
                board[i]=board[position]
                board[position]=EMPTY
                halt = True
            else:
                i-=1

def print_board(board):
###Printing the board
    print('+-----------------------------------------------------+')
    print('|', end='')
    i=0
    while i<board:
        print(' '+ i +' |', end = '')
        i+=1
    print('\n+-----------------------------------------------------+')

def draw_board(board, gui):
###Draws the game board
gui.clear()


    gui.text(250, 35, '1 Dimensional Chess', 'dark green', 25)
    # Drawing the base rectangle of the board:
    gui.rectangle(50, 85, 600, 70, 'red')


    i=0
    while i<=8:

        # Drawing the lines between the parts of rectangle of the board:
        if i>0:
            gui.line(50+((i)*67), 85,50+((i)*67),155, 'black')
        # Drawing the pieces of the game:
        if board[i] == W_KNIGHT:
            gui.text(50+((i)*72), 105, 'knight', 'white', 10)
        elif board[i] == W_KING:
            gui.text(50+((i)*72), 105, 'king', 'white', 10)
        elif board[i] == B_KNIGHT:
            gui.text(50+((i)*72), 105, 'knight', 'black', 10)
        elif board[i] == B_KING:
            gui.text(50+((i)*72), 105, 'king', 'black', 10)

        i+=1

    gui.update_frame(60)

def is_game_over(board):
###checking whether the game is over and returning the winner of the game
###        if not(W_KING in board):
    if (B_KING in board):
        print_board(board)
        print('Black wins!')
        return True
###    elif not(B_KING in board):
    elif (W_KING in board):
        print_board(board)
        print('White wins!')
        return True
    else:
        return False

def move(board, position, direction):
###Moving the chess pieces
    if ((not board[position]== 'WKi') or (not board[position]== 'BKi')):
        move_knight(board, position, direction)
    else:
        move_king(board, position, direction)


def main():

    # Create the canvas
    gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]

    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            # Draw the board again
            draw_board(board, gui)
            is_game_won = is_game_over(board)

main()
