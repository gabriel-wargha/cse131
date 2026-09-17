# 1. Name:
#      Gabriel Jose Esposito Wargha 
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      Getting json data in the right way and transforming in a array. I had a hard time in the save_board file. 
#      By mistake I was just saving an array for the board before I think about the solution that I used in line 52.
# 5. How long did it take for you to complete the assignment?
#      3-4 hours. 

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '
FILE_NAME = 'game.json'
# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

filename = FILE_NAME

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    
    # We use a try/expect to se if the file already exists.
    try: 
        with open(filename, "r", encoding='utf-8') as file:
            data = json.load(file)
            return data['board']
        
    # If not we start a blank board
    except FileNotFoundError:
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    
    # Try except to save the file.
    try:
        with open (filename, "w", encoding="utf-8") as file:
            board_dict ={"board": board}
            json.dump(board_dict, file)
    except FileNotFoundError:
        print("File not found")
    
    

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    
    #Layout to display the board similar 
    board_layout = f"""
         {board[0]:^3} | {board[1]:^3} | {board[2]:^3} 
        -----+-----+-----
         {board[3]:^3} | {board[4]:^3} | {board[5]:^3} 
        -----+-----+-----
         {board[6]:^3} | {board[7]:^3} | {board[8]:^3} """
    print (board_layout)
          

def is_x_turn(board):
    '''Determine whose turn it is.'''
    
    # Lets initialize 2 variables to count how many times each player already did.
    x_count = 0
    o_count = 0
    
    # Loop trough the board to get the count
    for item in board:
        
        if item == X:
            x_count += 1
        elif item == O:
           o_count += 1
    
    # "X" always starts, so player "O" will just play if has lees turns then "X"
    if x_count <= o_count:
        return X
    else:
        return O

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    
    # lets use keep_playing to know when stop our program.
    keep_playing = True
    while keep_playing: 
        display_board(board)
        choice = input(f"{is_x_turn(board)} > ")
        
        # If user hits "q" we save the board, so when the program runs again, the board still the same.
        if choice == "q":
            save_board(filename, board)
            keep_playing = False
        
        # We mark the option that user choose with "x" or "o" depending of who's turn it is.
        else:
            choice = int(choice)
            board[choice - 1] = is_x_turn(board)
            
            # If the game is over we make the board empty again and display message.
            if(game_done(board, message=True)):
                board = blank_board["board"]
                save_board(filename, board)
                keep_playing = False
                

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.


if __name__ == "__main__":
   board = read_board(filename)
   play_game(board)
   display_board(board)
    