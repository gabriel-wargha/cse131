# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

def getMonth():
    
    done = False
       
    while not done:
        try:
            month = int(input("Enter the month number: "))
               
            # Checking for the month number.
            if (month > 0 and month <= 12):
                   return month
            else:
                print("Error: Invalid month, month needs to be a number and be between 1 and 12")
        
        # Month must be a number.
        except ValueError:
               print('Error: Invalid input, month needs to be a number')
               
def getYear():
    
    done = False
    
    while not done:
        try:
            year = int(input("Enter the year number: "))
            
            #Checking for the year number.
            if ( year >= 1753):
                return year
            else:
                print("Error: Invalid year, please pick a year that is equal or higher than 1753")
        
        # Year needs to be a number.
        except ValueError:
            print('Error: Invalid input, year needs to be a number')
     
def isLeapYear(year):
    
    # If an year is divisible by 400 is a leap year 
    if year % 400 == 0: return True
    
    # If an year is divisible for 100 and not 400 is not a leap year.
    if year % 100 == 0: return False
    
    # If an year is not divisible by 100 and is divisible by 4 is a leap year.
    if year % 4 == 0: return True

    return False
    
def compute_offset(month, year):
    
    # Calculating the number of days.
    days = 0
    days += compute_days_from_year(year)
    days += compute_days_from_month(month, year)
    
    # All weeks have 7 days and because we start on a monday we just need to use this formula.
    day_of_week = (days + 1) % 7
    
    return day_of_week
    
def compute_days_from_year(year):
    days = 0
   # Loop to discover the number of days between the years that was chosen.
    for i in range(1753, year):
       
       #Leap years have one more day
       if isLeapYear(i):
           days += 366
       else:
           days += 365
    return days

def compute_days_from_month(month, year):
    
    days = 0
    # Loop to calculate the days until the chosen month.
    for i in range(1, month):
        days += get_days_in_month(i, year)  
    return days
        
def get_days_in_month(month, year):

    # Here we calculate all possibilities of days in a month
    if month in [1,3,5,7,8,10,12]: return 31
    
    elif month in [4,6,9,11]: return 30
            
    elif month == 2 and isLeapYear(year): return 29
    
    elif month == 2 and not isLeapYear(year): return 28
    
def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline



if __name__ == "__main__":
    month = getMonth()
    year = getYear()
    
    day_of_week = compute_offset(month, year)
    days_in_month = get_days_in_month(month, year)
    
    display_table(day_of_week, days_in_month)
