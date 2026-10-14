
import json

def displayBoard(board):
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
    


BLANK_BOARD = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
]

def getFileName():
    file_name = input("Where is your board located: ")
    return file_name

def getBoard(fileName): 
    done = False
    while not done:
        try: 
            with open(fileName, "r", encoding='utf-8') as file:
                data = json.load(file)
                return data['board']
            
        except FileNotFoundError:
            print("File not found")
        

def validInputPositions(board, input_positions):
    
    if (not input_positions[0].isdigit) or input_positions[0] in ["q", "Q"]:
        return True
    
    if len(input_positions) != 2:
        return False
    
    if not (input_positions[0].isdigit() or input_positions[1].isdigit()):
        return False
    
    for i in range (0, 1):
        if input_positions[i].isdigit():
            if 1 > input_positions > 9:
                return False
        else: 
            if not input_positions[i].lower() in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "q"]:
                return False
        
        if not isPositionAvailable:
            return False
    
    return True
        
def isPositionAvailable(board, input_positions):
    row = input_positions[0]
    column = input_positions[1]
    
    if board[row][column] == 0:
        return True
    return False
          
def getPosition(board): 
    done = False
    while not done:

        input_positions = input("Specify a coordinate to edit or 'Q' to save and quit: ")
        if(validInputPositions(board, input_positions)):
            done = True
         
        
    return input_positions

def transformInputNumbers(position):
    
    list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    positions = []
    print(position[0])
    print(position[1])
    
    for i in range(0, 2):
        position[i]
        if not position[i].isdigit():
            if (position[i]).lower() in list_of_letters:
                positions.append(list_of_letters.index(position[i]))
        else:
            positions.append(int(position[i]))   
    return positions

def getNumber():
    done = False
        
    while not done:
        try:
            number = int(input("Enter the a number between 1 and 10: "))         
            # Checking if the number is correct
            if number >= 1 and number <=10: return number
            else: print("Error: Invalid number, please pick a number between 1 and 10 ")     
        except ValueError:
                print('Error: Invalid input, you need to type a number')

def canPlaceNumber(positions, number, board ):
    row = positions[0]
    column = positions[1]
    
    if board[row][column] is None:
        return False
    
    for i in range(0, 9):
        if board[row][i] == number:
            return False
    
    for j in range(0, 9):
        if board[i][column] == number:
            return False
        
    sub_grid_row_start = row - row % 3
    sub_grid_column_start = column - column % 3
    
    for row in range (sub_grid_row_start, sub_grid_row_start + 2):
        for column in range (sub_grid_column_start, sub_grid_column_start+ 2):
            if board[row][column] == number:
                return False
    
    return True
      
def changeBoard(positions, number, board):
    if canPlaceNumber(positions, number, board):
        row = positions[0]
        column = positions[1]
        board[row][column] = number
        return board
    else:
        print("Invalid number for this position")
        return board

def save_board(filename, board):
    '''Save the current game to a file.'''
    
    # Try except to save the file.
    try:
        with open (filename, "w", encoding="utf-8") as file:
            board_dict ={"board": board}
            print(board_dict)
            json.dump(board_dict, file)
    except FileNotFoundError:
        print("File not found")

def playGame(board):
    done = False
    while not done:
        input_position = getPosition(board)
        
        if input_position[0] == "Q":
            done = True
            save_board(file_name)
            
        else:
            board_position =  transformInputNumbers(input_position)
            newNumber = getNumber()
            print(board_position, newNumber)
            board = changeBoard(board_position, newNumber, board)
            displayBoard(board)
            
    return board

if __name__ == "__main__":
    
        file_name = getFileName()
        board = getBoard(file_name)
        displayBoard(board)
        board = playGame(board)
        
        
# def valid_input_positions(positions):
#     letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "A", "B", "C", "D", "E", "F", "G", "H", "I", "q", "Q"]
    
#     row = next((char for char in letter_list if char.isalpha()), None)
#     print(row)
#     column = positions[1]
    
#     if not board[row][column] == 0:
#             return False
    
#     if len(positions) != 2:
#             return False
        
#     if (1 > row or row > 9) or (1> column > 9):
#         return False
    
#     return True
    