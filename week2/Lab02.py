def getMonth():
    
    while True:
        try:
            month = int(input("Enter the month number: "))

            #Checking for the month number
            if not (1 <= month and month <= 12):
                print("Error: Invalid Month, month needs to be a number and be between 1 and 12")
                continue
            
            break; 
           
        except ValueError:
            print('Error: Invalid input, month needs to be a number')
            
def getYear():
    
    while True:
        try:
            year = int(input("Enter the month number: "))

            #Checking for the year  number
            if not ( year >= 1753):
                print("Error: Invalid year, year needs to be a number and be between 1 and 12")
                continue
            
            break; 
           
        except ValueError:
            print('Error: Invalid input, year needs to be a number')
            

def compute_offset():
    


def main ()