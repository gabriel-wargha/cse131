import json

def getFileName():
    file_name = input("Where is your board located: ")
    return file_name

def read_board(file_name): 
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
    board_layout = f'''
       A|B|C | D|E|F |  G|H|I
    1| {board[0][0]} {board[0][1]} {board[0][2]} | {board[0][3]} {board[0][4]} {board[0][5]} | {board[0][6]} {board[0][7]} {board[0][8]}
    2| {board[1][0]} {board[1][1]} {board[1][2]} | {board[1][3]} {board[1][4]} {board[1][5]} | {board[1][6]} {board[1][7]} {board[1][8]}
    3| {board[2][0]} {board[2][1]} {board[2][2]} | {board[2][3]} {board[2][4]} {board[2][5]} | {board[2][6]} {board[2][7]} {board[2][8]}
    4| {board[3][0]} {board[3][1]} {board[3][2]} | {board[3][3]} {board[3][4]} {board[3][5]} | {board[3][6]} {board[3][7]} {board[3][8]}
    5| {board[4][0]} {board[4][1]} {board[4][2]} | {board[4][3]} {board[4][4]} {board[4][5]} | {board[4][6]} {board[4][7]} {board[4][8]}
    6| {board[5][0]} {board[5][1]} {board[5][2]} | {board[5][3]} {board[5][4]} {board[5][5]} | {board[5][6]} {board[5][7]} {board[5][8]}
    7| {board[6][0]} {board[6][1]} {board[6][2]} | {board[6][3]} {board[6][4]} {board[6][5]} | {board[6][6]} {board[6][7]} {board[6][8]}
    8| {board[7][0]} {board[7][1]} {board[7][2]} | {board[7][3]} {board[7][4]} {board[7][5]} | {board[7][6]} {board[7][7]} {board[7][8]}
    9| {board[8][0]} {board[8][1]} {board[8][2]} | {board[8][3]} {board[8][4]} {board[8][5]} | {board[8][6]} {board[8][7]} {board[8][8]}
    '''
    print(board_layout)

def write_board(board):
    '''Save the current game to a file.'''
    file_name = input("To file should we save the board: ")
    # Try except to save the file.
    try:
        with open (file_name, "w", encoding="utf-8") as file:
            board_dict ={"board": board}
            json.dump(board_dict, file)
    except FileNotFoundError:
        print("File not found")

def get_positions():
    input_positions = input("Specify a coordinate to edit or 'Q' to save and quit: ")
    return input_positions

def valid_input(input):
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
    done = False
        
    while not done:
        try:
            number = int(input("Enter the a number between 1 and 10: "))         
            # Checking if the number is correct
            if number >= 1 and number <=9: return number
            else: print("Error: Invalid number, please pick a number between 1 and 9")     
        except ValueError:
                print('Error: Invalid input, you need to type a number')

def changeBoard(board, position, new_number):
    row = position[0] - 1
    column = position[1]
    
    board[row][column] = new_number
    print(board[row][column])
    
    return board
    
def play_game(board):
        
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
  
if __name__ == "__main__":
    
    done = False
    
    file_name = getFileName()
    board = read_board(file_name)
    
    while not done:
        display_board(board)
        done = play_game(board)
            
        
    

    
    
        
        