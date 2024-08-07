import sys,time, os

def print_slow(str):
    for letter in str + "\n":
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def startMenu():
    print("You wake to a frantic call from Uncle Mike.")
    print("\t> Hey man, need your help. You awake?")
    print("\tI am now Unc, what's up?")
    print("\t> Your Aunt went crazy, need some help...keeping her at bay.")
    print("\tWhat kind of help?")
    print("\t> Just get over here and I'll show you.")
    print("You somewhat remember Mike's place, it's somewhere North-west of here.")
    print("Instructions:")
    print("\tTo move - Go {Direction} Either North, South, East or West.")
    print("\tTo pick up an item and add it to your inventory - Get {item}")
    print("\tType Exit to quit game.")
    print("Good luck...")
    input("Press Enter to continue.")

# Clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def uncleMikesTrailer(inventory):
    if len(inventory) == 0:
        print_slow("\t> Dang dude, you made it here fast.")
        print_slow("\t> Look man, your Aunt and I were messing around with The Book of Death.")
        print_slow("\t> ...and I may have turned her into them things from Evil Dead.")
        print_slow("\t> We gotta lock her up downstairs. You down to help?")
        return 1
    elif 4 > len(inventory) > 1:
        print_slow("\t> Dude, that's all you got? You saw your aunt!")
        return 2
    else:
        print_slow("\t> Hell yea dude, let's get started.")
        return 3

def optionalTwo():
    print_slow("Driving to Uncle Mike's you notice a dead doe on the side of the road.")
    print_slow("While it's not unusual to see around here, it looks rather disfigured.")
    print_slow("You also notice more blood than usual...Do you want to stop and take a look?")
    deerChoice = input("<Yes> <No> : ").title()
    if deerChoice == "Yes":
        return 1
    elif deerChoice == "No":
        return 2
    else:
        return 3