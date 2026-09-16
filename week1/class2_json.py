import json

def read_data_from_file():
    
    try:
        with open("friends.json", "r", encoding="utf-8") as friends_file:
            data = json.load(friends_file)
            return data
    except FileNotFoundError:
            print("We were not able to retrieve the file")
        
def owe_me():
    friends = read_data_from_file()
    total = 0

    for amount in friends["Owe me"]:
        total += amount

    return total


def main():
    my_friends = {
        "Names": ["Bob", "Bubba", "Jeannie"],
        "Phone Numbers": [801362123, 7654331, 27878897],
        "Ages": [23, 43, 56],
        "Owe me": [123.54, 543.45, 1010.87]
    }

    with open("friends.json", "w") as friends_file:
        json.dump(my_friends, friends_file, indent=4)

    total = owe_me()
    print(f"My friends owe me a total of ${total:.2f}")


if __name__ == "__main__":
    main()
    
    
    