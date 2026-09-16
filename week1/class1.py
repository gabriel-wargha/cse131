def hello_user_message():
    name = input("Whats is your last name: ")
    gender = input("Are you male or female: (m/f) ")
    
    if gender == "m":
        print(f"Hello Mr. {name}")
    else:
        print(f"Hello Ms. {name}")
    
if __name__ == "__main__":
    hello_user_message()