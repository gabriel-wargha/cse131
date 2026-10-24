# 1. Name:
#      Gabriel Wargha
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      Allow the user to play the Sudoku game
# 4. What was the hardest part? Be as specific as possible.
#      This week the hardest part was to figured out how to display hints
# 5. How long did it take for you to complete the assignment?
#      2 hours this week. Close 10 in total.

import json

def getFileName():
    file_name = input("Where is your board located: ")
    return file_name

def read_board(file_name): 
    ''' This function receives a file name as a parameter.
        If file is available, gets the board, if file does not exist, prompt the suer for a new file '''
    done = False
    while not done:
        try: 
            with open(file_name, "r", encoding='utf-8') as file:
                data = json.load(file)
                return data['board']
                done = True
            
        except FileNotFoundError:
            print("File not found")
            file_name = getFileName()
    
def display_board(board):
    '''This function receives a board as a parameter. Print the letters A to I as column names.
       After that we have a loop that will display each line, this loop adds a line separator when row is 3 or 6.
       Then, we loop trough each column to print the value of that board position. 
       Finally it adds a specific separator after each value depending of the position of the value in the board'''
    print("")
    print("   A B C D E F G H I")
    
    for row in range(9):
        if row == 3 or row == 6:
            print("   -----+-----+-----") 
        print(row + 1, " ", end='')
        
        for column in range(9):
            separator = [' ', ' ', '|', ' ', ' ', '|', ' ', ' ', '\n']
            print(board[row][column] if board[row][column] != 0 else ' ', end=separator[column])
                      
def write_board(board):
    '''Save the current game to a file.'''
    file_name = input("To file should we save the board: ")
    # Try except to save the file.
    with open (file_name, "w", encoding="utf-8") as file:
        board_dict ={"board": board}
        json.dump(board_dict, file)
    
def get_positions():
    ''' This functions prompt the user about a position in the board'''
    
    input_positions = input("Specify a coordinate to edit or 'Q' to save and quit: \n")
    return input_positions

def valid_input(input):
    '''This function was created to validate the input that we get in the user in the get_positions function
       and if this position is available.
       First we check if the input has a number and a letter.
       After, we assign the letter and number using next method.
       Then, we check that the input has exactly 2 digits. 
       Then we check if letter and and number follow the requirements.
       Finally if no fail on tests we return True'''
    
    
    letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "q"]
    
    have_a_number = any(char.isalpha() for char in input)
    have_a_letter = any(char.isdigit() for char in input)
    
    if not (have_a_letter and have_a_number):
            return False
    
    letter = next((char for char in input if char.isalpha()), None)
    number = int(next((char for char in input if char.isdigit()), None))
    
    if len(input) > 2:
        return False
        
    
    if letter.lower() not in letter_list:
        return False
    
    if number > 9 or number < 1:
        return False
    
    return True

def transformInputNumbers(position):
    '''This unction receives a position and transform the letter in the position parameter in a column and the number in a row.'''
    
    list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    positions = []
    column = 0
    row = 0
    
    for i in range(0, 2):
        position[i]
        if not position[i].isdigit():
            if (position[i]).lower() in list_of_letters:
                column = (list_of_letters.index(position[i].lower()))
        else:
            row = int(position[i]) 
            
    positions.extend([row, column])
    return positions    
        
def getNumber():
    '''This function prompt the user for a number value and validates the result'''
    done = False
    while not done:
        try:
            number = int(input("Enter the a number between 1 and 9: "))         
            # Checking if the number is correct
            if number >= 1 and number <=9: return number
            else: print("Error: Invalid number, please pick a number between 1 and 9")     
        except ValueError:
                print('Error: Invalid input, you need to type a number')

def changeBoard(board, position, new_number):
    '''This function receives the boards, the new position and new number and change the board based on that'''
    row = position[0] - 1
    column = position[1]
    
    board[row][column] = new_number
    
    return board
    
def play_game(board):
    '''The biggest function in the game.
            Every round we get the positions, check if position is valid and if the suer wants to quit the game.
            Then, if positions are not invalid we change the selected position value to the new number.'''
    input = get_positions()
    
    if input is "":
        print("Error, you need to type something")
        return False
        
    if input[0] == "Q":
        print("Bye, let's keep playing letter")
        write_board(board)
        print("File saved!")
        return True
     
        
    if not valid_input(input):
        print(f"ERROR: Square {input} is invalid")
        return False
        
    positions = transformInputNumbers(input)
    
    if not is_position_empty(board, positions):
        print("This position already has a number")
        return False
    
    showHint(board, positions)
    new_number = getNumber()
    
    if canPlaceNumber(board, new_number, positions): 
        board = changeBoard(board, positions, new_number)
    else:
        print("Invalid input. Please try again!")
    return False
  
def canPlaceNumber(board, number, positions):
    '''Function to check everything that would break the games rules about placing number'''
    row = positions[0] - 1 
    column = positions[1]
   
     # No number equal new number in the same row.
    for col in range(9):
        if board[row][col] == number:
            return False
    
    # No number equal new number in the same column.
    for r in range(9):
        if board[r][column] == number:
            return False 
    
    # No number equal new number in the 3x3 grid
    sub_grid_row_start = row - row % 3
    sub_grid_column_start = column - column % 3
    
    for r in range(sub_grid_row_start, sub_grid_row_start +3):
        for col in range(sub_grid_column_start, sub_grid_column_start + 3):
            if board[r][col] == number:
                return False
    
    return True

def showHint(board, positions):
    '''This function receives a board and the positions. Ask if the user wants a tip.
        If the user wants a tip, loop between 0-9 and add the possible numbers to a array
        The output is just the array with the tips'''
   
    done = False
    
    while not done:
        want_hint = input("Print 'T' for a quick tip or 'K' to keep going: ")
        if want_hint not in ["T", "K"]:
            print("Invalid input")
        
        if want_hint == "K":
            done = True
            
        elif want_hint == "T":
            hints = []
            for i in range(10):
                if canPlaceNumber(board, i, positions):
                    hints.append(i)
            print(f"These are all possible numbers for this position {hints}")
            done = True
            
def is_position_empty(board, positions):
    '''This functions receives the board and the positions as a parameter and check if the position is empty'''
    row = positions[0] - 1
    column = positions[1]
    
    if not (board[row][column] != 0):
        return True
    
    return False
        
if __name__ == "__main__":
    
    done = False
    
    file_name = getFileName()
    board = read_board(file_name)
    
    while not done:
        display_board(board)
        done = play_game(board)
        
            
    
            
        
    

    
    
        
        