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
    
    input_positions = input("Specify a coordinate to edit or 'Q' to save and quit: ")
    return input_positions

def valid_input(input):
    '''This function was created to validate the input that we get in the user in the ge_positions function.
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
    print(board[row][column])
    
    return board
    
def play_game(board):
    '''The biggest function in the game.
            Every round we get the positions, check if position is valid and if the suer wants to quit the game.
            Then, if positions are not invalid we change the selected position value to the new number.'''
        
    input = get_positions()
        
    if input[0] == "Q":
        print("Bye, let's keep playing letter")
        write_board(board)
        print("File saved!")
        return True
            
        
    if not valid_input(input):
        print(f"ERROR: Square {input} is invalid")
        return False
        
        
    positions = transformInputNumbers(input)
    new_number = getNumber()
    board = changeBoard(board, positions, new_number)
    return False
  
def canPlaceNumber():
    return True


if __name__ == "__main__":
    
    done = False
    
    file_name = getFileName()
    board = read_board(file_name)
    
    while not done:
        display_board(board)
        done = play_game(board)
            
        
    

    
    
        
        