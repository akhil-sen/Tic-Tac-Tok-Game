'''
Logic:

[Visual Representation]-->[User Input]-->[Funtion Updates]-->[New Visual]-->[Update in Visual Representation]
'''
#class for formating print statement
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
'''
Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
'''
#from IPython.display import clear_output

def display_board(board):
    #clear_output()
    #Clear_output() This is use to clear previous output. Remember, this only works in jupyter.
    print('┏━━━━━┳━━━━━━┳━━━━━┓')
    print('┃     ┃      ┃     ┃')
    print('┃  '+board[1]+'  ┃   '+board[2]+'  ┃  '+board[3]+'  ┃')
    print('┃     ┃      ┃     ┃')
    print('┣━━━━━╋━━━━━━╋━━━━━┫')
    print('┃     ┃      ┃     ┃')
    print('┃  '+board[4]+'  ┃   '+board[5]+'  ┃  '+board[6]+'  ┃')
    print('┃     ┃      ┃     ┃')
    print('┣━━━━━╋━━━━━━╋━━━━━┫')
    print('┃     ┃      ┃     ┃')
    print('┃  '+board[7]+'  ┃  '+board[8]+'   ┃  '+board[9]+'  ┃')
    print('┃     ┃      ┃     ┃')
    print('┗━━━━━┻━━━━━━┻━━━━━┛')
'''
Take in a player input and assign their marker as 'X' or 'O'.
'''
def player_input():
    mark=''
    
    while mark !='X' and mark !='O':
        mark = input(color.RED+'Hey!'+color.END+' Player1:Select your mark '+color.RED+'X'+color.END+' or '+color.RED+'O'+color.END+': ').upper()
    if mark=='X':
        return ('X','O')
    else:
        return ('O','X')
#Output will be (Player 1 Choice, Player 2 Choice)
'''
Take in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
'''
def place_marker(board, mark, position):
    board[position]=mark
'''
Function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
'''
def win_check(board, mark):
    
    #Winning Tic Tak Toc conditions
    
    return ((board[1]==board[2]==board[3]==mark)or #row
           (board[4]==board[5]==board[6]==mark)or  #row
           (board[7]==board[8]==board[9]==mark)or  #row
           (board[1]==board[4]==board[7]==mark)or  #coluum
           (board[2]==board[5]==board[8]==mark)or  #coluum
           (board[3]==board[6]==board[9]==mark)or  #coluum
           (board[1]==board[5]==board[9]==mark)or  #Daigonal
           (board[3]==board[5]==board[7]==mark))   #Diagonal
'''
Function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
'''
import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
'''
Function that returns a boolean indicating whether a space on the board is freely available.
'''
def space_check(board, position):
    
    return board[position]==' '
'''
Function that checks if the board is full and returns a boolean value. True if full, False otherwise.
'''
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    #board is full another condition
    return True
'''
Function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use
'''
def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Enter Position value in range 1-9: '))
    return position
'''
Function that asks the player if they want to play again and returns a boolean True if they do want to play again.
'''
def replay():
    choice=input('Nice! wanna play it again? (Y)Yes or (N)No ')
    return choice=='Yes'
'''
Use while loops and the functions you've made to run the game!
'''
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No. ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print(color.RED+'Congratulations!'+color.END+' Player 1 have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print(color.RED+'Congratulations!'+color.END+' Player 2 have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
