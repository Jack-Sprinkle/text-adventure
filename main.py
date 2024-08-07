from functions import print_slow, startMenu, clear, uncleMikesTrailer, optionalTwo
from setup import locations, vowels, inventory, currLocation, currMsg
    
clear()
startMenu()

while True:
    clear()

    print(f"You are in {currLocation}\nInventory : {inventory}\n{'-' * 27}")
    print_slow(currMsg)

    # Accepts player's move as input
    user_input = input("Enter your move: ")

    # Splits move into words
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    # Reset item and direction
    item = "Item"
    direction = "null"

    # Second word is object or direction
    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = " ".join(item).title()

    # Moving between rooms
    if action == "Go":
        try:
            currLocation = locations[currLocation][direction]
            currMsg = f"You travel {direction} to {currLocation}"

        except:
            currMsg = "You can't go that way."

        if currLocation == "Uncle Mike's Trailer":
            path = uncleMikesTrailer(inventory) 
            if path == 1:
                currMsg = "Uncle Mike needs your help, go find some items to help."
            elif path == 2:
                currMsg = "You might need some more things to help out."
            elif path == 3:
                currMsg = "You're ready to tackle the beast."

        if currLocation == "Optional Two":
            clear()
            path = optionalTwo()

            if path == 1:
                currMsg = "You approach the deer and begin to notice the rotten smell."
            if path == 2:
                currMsg = "Guess someone is scared."
            if path == 3: 
                currMsg == "That option is not valid."

    # Exit program
    elif action == "Exit":
        break
    # Any other commands invalid
    else:
        currMsg = "Invalid command"
