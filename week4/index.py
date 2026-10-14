def transformInputNumbers(position):
    
    list_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    positions = []
    
    for i in range(0, 2):
        if (position[i]).lower() in list_of_letters:
            positions.append(list_of_letters.index(position[i]))
        else:
            positions.append(int(position[i]))
            
    return positions

if __name__ == "__main__":
    
   newPositions = transformInputNumbers("3c")
   print(newPositions)
    


# FUNCTION transformInputNumbers(input_position):
#     list_of_letters <-- ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
#     positions_on_board <-- []
    
#     FOR i <-- 0 ... 2:
#         IF input_position[] IN list_of_letters:
#             positions_on_board[i] <--  GET index number from letter

#         ELSE: 
#             positions_on_board[i] <-- input_position[i]
        
#     RETURN positions_on_board 
    
    
    
    