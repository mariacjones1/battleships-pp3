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
        # self.orientation = orientation


class Battleship(Ship):
    """
    Battleship class
    """
    def __init__(self, position, orientation):
        Ship.__init__(self, 4)
        self.position = position
        self.orientation = orientation


class Destroyer(Ship):
    """
    Destroyer class
    """
    def __init__(self, position, orientation):
        Ship.__init__(self, 3)
        self.position = position
        self.orientation = orientation


class Submarine(Ship):
    """
    Submarine class
    """
    def __init__(self, position, orientation):
        Ship.__init__(self, 3)
        self.position = position
        self.orientation = orientation


class PatrolBoat(Ship):
    """
    Patrol Boat class
    """
    def __init__(self, position, orientation):
        Ship.__init__(self, 2)
        self.position = position
        self.orientation = orientation


def set_position(ship, length):
    """
    Sets the cooridinates for each ship
    """
    letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                        "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

    ship.position = []

    while True:
        column = input("Choose a column from A-J: ").upper()
        if column in "ABCDEFGHIJ" and len(column) == 1:
            column = letter_to_number[column]
            break
        else:
            print("Invalid letter.")

    while True:
        try:
            row = int(input("Choose a row from 1-10: "))
            if row >= 1 and row <= 10:
                row -= 1
                break
            else:
                print("Invalid number.")
        except ValueError:
            print("Input must be a number 1-10.")

    while True:
        print("Now choose the ship's orientation:")
        ship.orientation = input("Horizontal (H) or vertical (V)? ").upper()
        if ship.orientation == "H":
            while len(ship.position) <= length:
                ship.position.append((column, row))
                column += 1
            break
        elif ship.orientation == "V":
            while len(ship.position) <= length:
                ship.position.append((column, row))
                row += 1
            break
        else:
            print("Please input only 'H' or 'V' for orientation")

    return ship.position


start_game()
create_user()
set_position(Carrier, 5)
set_position(Battleship, 4)
set_position(Destroyer, 3)
set_position(Submarine, 3)
set_position(PatrolBoat, 2)
