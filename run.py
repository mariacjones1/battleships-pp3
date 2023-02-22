def start_game():
    """
    Prints welcome message and instructions,
    and gives user the opportunity to start the game
    """
    print("Welcome to Battleships!\n"
           "The aim of the game is to find and sink your opponent's"
           "battleships before they sink yours.\n"
           "Choose the location for each of your ships, or generate"
           "random positions, then take it in turns to guess"
           "where each other's ships are.\n"
           "Ready to play?")
    
    while True:
        user_start = input("Y/N\n").upper()

        if user_start == "Y":
            break
        elif user_start == "N":
            print("Maybe next time!")
            exit()
        else:
            print(f"Invalid input: {user_start}. Please type 'Y' or 'N'")

    return user_start


start_game()
