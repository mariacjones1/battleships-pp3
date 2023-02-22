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


def create_user():
    """
    Gets the user to enter a username
    Must be at least three characters and contain
    alphanumeric characters only or an error will be raised
    """
    print("Excellent! Before we get started, what should we call you?")

    while True:
        username = input("Enter username: ")

        try:
            if username.isalnum() is False:
                raise TypeError
            elif len(username) < 3:
                raise ValueError
        except TypeError:
            print("Username should use numbers and letters only.")
        except ValueError:
            print("Username must be at least 3 characters.")
        else:
            break

    return username


class Ship:
    """
    Ship class
    """
    def __init__(self, length):
        self.length = length


class Carrier(Ship):
    """
    Carrier class
    """
    def __init__(self, position):
        Ship.__init__(self, 5)
        self.position = position
        

class Battleship(Ship):
    """
    Battleship class
    """
    def __init__(self, position):
        Ship.__init__(self, 4)
        self.position = position
        

class Destroyer(Ship):
    """
    Destroyer class
    """
    def __init__(self, position):
        Ship.__init__(self, 3)
        self.position = position
        

class Submarine(Ship):
    """
    Submarine class
    """
    def __init__(self, position):
        Ship.__init__(self, 3)
        self.position = position
        

class PatrolBoat(Ship):
    """
    Patrol Boat class
    """
    def __init__(self, position):
        Ship.__init__(self, 2)
        self.position = position


start_game()
create_user()
