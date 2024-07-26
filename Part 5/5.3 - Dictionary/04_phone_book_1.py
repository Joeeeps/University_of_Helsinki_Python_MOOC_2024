dic = {}

# Get the first command
command = int(input("1 search, 2 add, 3 quit): "))

while command != 3:
    if command == 1:
        # Search for a name in the dictionary
        name = input("name: ")
        if name in dic:
            # If the name exists, print the associated number
            print(f"{dic[name]}")
        else:
            # If the name does not exist, print a message
            print("no number")
    elif command == 2:
        # Add a new name and number to the dictionary
        name = input("name: ")
        number = input("number: ")
        dic[name] = number  # Correct way to add to the dictionary... the key of [name] corresponds to the value of [number]
        print("ok!")
    else:
        # Handle invalid commands
        print("Invalid command, please try again.")
    
    # Get the next command
    command = int(input("1 search, 2 add, 3 quit): "))

print("quitting...")

