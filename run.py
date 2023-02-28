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
    ship_coordinates = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.position = []
        self.orientation = None

    def set_position(self):
        """
        Sets the coordinates for each ship
        """
        letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                            "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

        while not self.position:
            print(f"Set the coordinates for the {self.name}")
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
                print("Now choose the ship's orientation:\n"
                      "Horizontal ('H') or vertical ('V')?")
                self.orientation = input().upper()
                if self.orientation == "H":
                    if (column + (self.length - 1)) > 9:
                        break
                    else:
                        while len(self.position) < self.length:
                            self.position.append((column, row))
                            column += 1
                    break
                elif self.orientation == "V":
                    if (row + (self.length - 1)) > 9:
                        break
                    else:
                        while len(self.position) < self.length:
                            self.position.append((column, row))
                            row += 1
                    break
                else:
                    print("Please input only 'H' or 'V' for orientation")

            print(self.position)
            print(Ship.ship_coordinates)
            print(Ship.ship_coordinates + self.position)
            print(set(Ship.ship_coordinates + self.position))
            if (len(Ship.ship_coordinates + self.position) !=
                    len(set(Ship.ship_coordinates + self.position))):
                self.position = []
                print("Ship doesn't fit; please try again.")
            elif not self.position:
                print("Ship doesn't fit; please try again.")
            else:
                Ship.ship_coordinates = Ship.ship_coordinates + self.position
                return Ship.ship_coordinates


def print_board(coordinates):
    """
    Prints board with set ship coordinates
    """
    board = [[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
              (8, 0), (9, 0)],
             [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
              (8, 1), (9, 1)],
             [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
              (8, 2), (9, 2)],
             [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
              (8, 3), (9, 3)],
             [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
              (8, 4), (9, 4)],
             [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
              (8, 5), (9, 5)],
             [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
              (8, 6), (9, 6)],
             [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
              (8, 7), (9, 7)],
             [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8),
              (8, 8), (9, 8)],
             [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9),
              (8, 9), (9, 9)],]

    for row in board:
        for coordinate in row:
            if coordinate in coordinates:
                print("@")
            else:
                print("O")


carrier = Ship("Carrier", 5)
battleship = Ship("Battleship", 4)
destroyer = Ship("Destroyer", 3)
submarine = Ship("Submarine", 3)
patrol_boat = Ship("Patrol Boat", 2)


start_game()
create_user()
print(carrier.set_position())
print_board(Ship.ship_coordinates)
print(battleship.set_position())
print(destroyer.set_position())
print(submarine.set_position())
print(patrol_boat.set_position())
