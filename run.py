import random
import time


def start_game():
    """
    Prints welcome message and instructions,
    and gives user the opportunity to start the game.

    User input should be either 'Y', 'N', 'y', or 'n'
    (function will convert input to uppercase).
    """
    # Welcome message
    print("Welcome to Battleships!\n"
          "The aim of the game is to find and sink your opponent's "
          "battleships before they sink yours.\n"
          "Choose the location for each of your ships, while the computer "
          "generates random positions, then take it in turns to guess "
          "where each other's ships are.\n"
          "Ready to play?")

    # User input to either start game or exit
    while True:
        user_start = input("Y/N\n").upper()

        try:
            if not user_start:
                raise ValueError  # Checks for empty value
            elif user_start == "Y":
                break
            elif user_start == "N":
                print("Maybe next time!")
                exit()
            else:
                # Checks for invalid but non-empty value
                print(f"Invalid input: {user_start}. Please type 'Y' or 'N'.")
        except ValueError:
            print("Input must not be empty.")

    return user_start


def create_user():
    """
    Gets the user to enter a username.

    Must be at least three characters and contain
    alphanumeric characters only or an error will be raised.
    """
    print("Excellent! Before we get started, what should we call you?")

    # Ask for username
    while True:
        username = input("Enter username: ")

        try:
            if not username:
                raise ValueError  # Checks for empty value
            elif username.isalnum() is False:
                raise TypeError  # Checks for invalid characters
            elif len(username) < 3:
                raise ValueError  # Checks username is at least 3 characters
        except ValueError:
            print("Username must be at least 3 characters.")
        except TypeError:
            print("Username should use numbers and letters only.")
        else:
            break

    return username


class Ship:
    """
    Ship class.
    """
    user_coordinates = []
    cpu_coordinates = []

    def __init__(self, name, length):
        """
        Ship class constructor.

        name: Which ship is being positioned.
        length: Length of the ship/how many coordinates it takes up.
        position: Empty array - will be set using set_position or
            random_position function.
        orientation: Will be set to either vertical or horizontal
            using set_position or random_position.
        """
        self.name = name
        self.length = length
        self.position = []
        self.orientation = None

    def set_position(self):
        """
        Allows the user to set the coordinates for each ship.

        Checks for invalid or empty inputs and uses set ship length
        to determine the ship's full position.
        Also checks to make sure the ship fits on the board and does
        not overlap with any ships already placed.
        """
        # Converts user input letter to corresponding column number
        letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                            "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

        # Loops until valid coordinates have been set
        while not self.position:
            print(f"Set the coordinates for the {self.name} "
                  f"(length = {self.length})")
            while True:
                # Convert input to uppercase
                column = input("Choose a column from A-J: ").upper()
                try:
                    if not column:
                        raise ValueError  # Checks for empty value
                    elif column in "ABCDEFGHIJ" and len(column) == 1:
                        # Converts valid input to number
                        column = letter_to_number[column]
                        break
                    elif column.isalpha() is False:
                        raise TypeError  # Checks input type is alpha
                    elif len(column) != 1:
                        # Checks input is only 1 letter
                        print("Input should only be one letter.")
                    else:
                        # Checks letter is in accepted values
                        print("Invalid letter.")
                except ValueError:
                    print("Input must not be empty.")
                except TypeError:
                    print("Input must be a letter.")

            while True:
                try:
                    # Make sure input is an integer
                    row = int(input("Choose a row from 1-10: "))
                    if not row:
                        raise ValueError  # Checks for empty value
                    elif row >= 1 and row <= 10:
                        row -= 1  # Converts valid input to row number
                        break
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Invalid input. Please type a letter from 1-10.")

            while True:
                print("Now choose the ship's orientation:\n"
                      "Horizontal ('H') or vertical ('V')?")
                # Convert input to uppercase
                self.orientation = input().upper()
                try:
                    if not self.orientation:
                        raise ValueError  # Checks for empty input
                    elif self.orientation == "H":
                        # Checks horizontal ship fits on board
                        if column + self.length > 10:
                            break
                        else:
                            while len(self.position) < self.length:
                                # Set full ship position using ship length
                                self.position.append((column, row))
                                column += 1
                        break
                    elif self.orientation == "V":
                        # Checks vertical ship fits on board
                        if row + self.length > 10:
                            break
                        else:
                            while len(self.position) < self.length:
                                # Set full ship position using ship length
                                self.position.append((column, row))
                                row += 1
                        break
                    else:
                        print("Please input only 'H' or 'V' for orientation.")
                except ValueError:
                    print("Input must not be empty.")

            if (len(Ship.user_coordinates + self.position) !=
                    len(set(Ship.user_coordinates + self.position))):
                # Checks ship does not overlap with another ship on the board
                self.position = []  # Set array to empty to restart loop
                print("Ship doesn't fit; please try again.")
            elif not self.position:
                # If ship does not fit on board and position is empty
                print("Ship doesn't fit; please try again.")
            else:
                Ship.user_coordinates = Ship.user_coordinates + self.position
                return Ship.user_coordinates  # Coordinates set for ship

    def random_position(self):
        """
        Generates random positions for each ship.

        Uses random to set coordinates and orientation.
        Checks each ship fits on the board and does not overlap
        with another ship - restarts the loop to generate new coordinates
        if ship doesn't fit.
        """
        orientation = ["H", "V"]
        print(f"Setting computer coordinates for {self.name}...")
        while not self.position:
            # Randomly set starting coordinates and orientation for ship
            column = random.randint(0, 9)
            row = random.randint(0, 9)
            self.orientation = random.choice(orientation)

            if self.orientation == "H":
                if column + self.length > 10:
                    pass  # If ship doesn't fit on board
                else:
                    while len(self.position) < self.length:
                        self.position.append((column, row))
                        column += 1  # Set full ship position using ship length
            elif self.orientation == "V":
                if row + self.length > 10:
                    pass  # If ship doesn't fit on board
                else:
                    while len(self.position) < self.length:
                        self.position.append((column, row))
                        row += 1  # Set full ship position using ship length

            if (len(Ship.cpu_coordinates + self.position) !=
                    len(set(Ship.cpu_coordinates + self.position))):
                # Checks ship does not overlap with another ship on the board
                self.position = []  # Set array to empty to restart loop
            # If ship does not fit on board and position is empty
            elif not self.position:
                self.position = []
            else:
                Ship.cpu_coordinates = Ship.cpu_coordinates + self.position
                return Ship.cpu_coordinates  # Coordinates set for ship


def guess_coordinates(guessed, coordinates):
    """
    User guesses ship coordinates, which are checked
    against previously guessed coordinates and computer
    ship coordinates.

    guessed: Contains coordinates which have already been guessed.
    coordinates: Contains set ship coordinates.
    """

    # Converts user input letter to corresponding column number
    letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                        "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
    guess = ()  # Starts with empty guess

    while not guess:
        while True:
            guess_column = input("Guess a column from A-J: ").upper()
            try:
                if not guess_column:
                    raise ValueError  # Checks for empty input
                elif guess_column in "ABCDEFGHIJ" and len(guess_column) == 1:
                    # Converts valid input to number
                    guess_column = letter_to_number[guess_column]
                    break
                else:
                    print("Invalid letter.")
            except ValueError:
                print("Input must not be empty.")

        while True:
            try:
                guess_row = int(input("Guess a row from 1-10: "))
                if not guess_row:
                    raise ValueError  # Checks for empty input
                elif guess_row >= 1 and guess_row <= 10:
                    guess_row -= 1  # Converts valid input to row number
                    break
                else:
                    print("Invalid number.")
            except ValueError:
                print("Input must be a number 1-10.")

        # Adds column and row inputs to full coordinate guess
        guess = (guess_column, guess_row)

        # Checks if coordinate has already been guessed
        if guess in guessed:
            print("Coordinate already guessed! Please guess again.")
            guess = ()  # Sets guess to empty so loop restarts
        else:
            # Adds guess to guessed array
            guessed.append(guess)
            # Checks if guess is a hit or a miss
            if guess in coordinates:
                print("Hit!")
            else:
                print("Miss!")


def guess_random_coordinates(guessed, coordinates):
    """
    Uses random to generate random coordinates for computer guesses
    and checks against previously guess coordinates and user ship coordinates.

    guessed: Contains coordinates which have already been guessed.
    coordinates: Contains set ship coordinates.
    """
    # Converts randomly generated number to corresponding column letter
    number_to_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    guess = ()  # Starts with empty guess

    while not guess:
        while True:
            # Randomly guesses coordinates
            guess_column = random.randint(0, 9)
            guess_row = random.randint(0, 9)
            guess = (guess_column, guess_row)
            # Checks if coordinate has already been guessed
            if guess in guessed:
                guess = ()
            else:
                # Prints computer guess
                print(f"Computer guessed ({number_to_letter[guess_column]}, "
                      f"{guess_row + 1})")
                # Adds guess to guessed array
                guessed.append(guess)
                # Checks if guess is a hit or a miss
                if guess in coordinates:
                    print("Hit!")
                else:
                    print("Miss!")
                break


def print_board(board, coordinates, guessed, correct, player):
    """
    Prints user board showing set coordinates and
    correct computer guesses.

    board: Contains all possible coordinates.
    coordinates: Array with set ship coordinates (user or cpu).
    guessed: Array with guessed coordinates (user or cpu).
    correct: Array with correctly guessed coorinates (user or cpu).
    player: String, either user or cpu.
    """

    # Prints column letters
    print("  | A | B | C | D | E | F | G | H | I | J |\n"
          "   ----------------------------------------")
    # Starts with first row
    row_number = 1
    for row in board:
        if row_number < 10:  # Prints a space after row numbers 1-9
            print(str(row_number) + " |", end="")
        else:  # Doesn't print a space after row number '10'
            print(str(row_number) + "|", end="")
        for i in row:
            # Checks if coordinate has been correctly guessed
            if i in guessed and i in coordinates:
                print(" ⊗ |", end="")
                correct.append(i)
            # Checks if coordinate is a set ship coordinate on user's board
            elif i in coordinates and player == "user":
                print(" ⬤ |", end="")
            # Checks if coordinate has been incorrectly guessed
            elif i in guessed:
                print(" ~ |", end="")
            # For all other coordinates
            else:
                print(" ○ |", end="")
        print("\n")
        row_number += 1


# Creates user ships
user_carrier = Ship("Carrier", 5)
user_battleship = Ship("Battleship", 4)
user_destroyer = Ship("Destroyer", 3)
user_submarine = Ship("Submarine", 3)
user_patrol_boat = Ship("Patrol Boat", 2)

# Creates cpu ships
cpu_carrier = Ship("Carrier", 5)
cpu_battleship = Ship("Battleship", 4)
cpu_destroyer = Ship("Destroyer", 3)
cpu_submarine = Ship("Submarine", 3)
cpu_patrol_boat = Ship("Patrol Boat", 2)


def main():
    """
    Runs main game functions.
    """
    # Start game and create username
    start_game()
    username = create_user()

    # Game loop runs until user chooses to exit
    while True:
        # User sets ship positions
        user_guessed = []
        user_correct = []
        cpu_guessed = []
        cpu_correct = []
        board = [[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
                  (7, 0), (8, 0), (9, 0)],
                 [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
                  (7, 1), (8, 1), (9, 1)],
                 [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
                  (7, 2), (8, 2), (9, 2)],
                 [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
                  (7, 3), (8, 3), (9, 3)],
                 [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
                  (7, 4), (8, 4), (9, 4)],
                 [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5),
                  (7, 5), (8, 5), (9, 5)],
                 [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6),
                  (7, 6), (8, 6), (9, 6)],
                 [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
                  (7, 7), (8, 7), (9, 7)],
                 [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8),
                  (7, 8), (8, 8), (9, 8)],
                 [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9),
                  (7, 9), (8, 9), (9, 9)]]
        print(f"{username}'s board:")
        print_board(board, Ship.user_coordinates, cpu_guessed, cpu_correct,
                    "user")
        user_carrier.set_position()
        print_board(board, Ship.user_coordinates, cpu_guessed, cpu_correct,
                    "user")
        user_battleship.set_position()
        print_board(board, Ship.user_coordinates, cpu_guessed, cpu_correct,
                    "user")
        user_destroyer.set_position()
        print_board(board, Ship.user_coordinates, cpu_guessed, cpu_correct,
                    "user")
        user_submarine.set_position()
        print_board(board, Ship.user_coordinates, cpu_guessed, cpu_correct,
                    "user")
        user_patrol_boat.set_position()
        print_board(board, Ship.user_coordinates, cpu_guessed, cpu_correct,
                    "user")

        # Randomly generate computer ship positions
        cpu_carrier.random_position()
        time.sleep(2)
        cpu_battleship.random_position()
        time.sleep(2)
        cpu_destroyer.random_position()
        time.sleep(2)
        cpu_submarine.random_position()
        time.sleep(2)
        cpu_patrol_boat.random_position()
        time.sleep(2)
        print("Computer board:")
        print_board(board, Ship.cpu_coordinates, user_guessed, user_correct,
                    "cpu")

        # Start gameplay
        winner = False

        while winner is False:
            # User guesses
            print(Ship.cpu_coordinates)
            guess_coordinates(user_guessed, Ship.cpu_coordinates)
            time.sleep(1)
            print("Computer board:")
            print_board(board, Ship.cpu_coordinates, user_guessed,
                        user_correct, "cpu")
            time.sleep(1)

            # Check if user has won
            if len(set(user_correct)) == 17:
                print("Congratulations, you win!")
                winner = True
            else:
                # Computer guesses
                print("Computer guessing...")
                time.sleep(2)
                guess_random_coordinates(cpu_guessed, Ship.user_coordinates)
                time.sleep(1)
                print(f"{username}'s board:")
                print_board(board, Ship.user_coordinates, cpu_guessed,
                            cpu_correct, "user")
                time.sleep(1)

                # Check if computer has won
                if len(set(cpu_correct)) == 17:
                    print("Computer wins!")
                    winner = True
                else:
                    winner = False

        # Ask if user wants to play again and reset all position arrays
        while True:
            play_again = input("Would you like to play again (Y/N)? ").upper()
            try:
                if not play_again:
                    raise ValueError
                elif play_again == "Y":
                    user_carrier.position = []
                    user_battleship.position = []
                    user_destroyer.position = []
                    user_submarine.position = []
                    user_patrol_boat.position = []
                    Ship.user_coordinates = []
                    cpu_carrier.position = []
                    cpu_battleship.position = []
                    cpu_destroyer.position = []
                    cpu_submarine.position = []
                    cpu_patrol_boat.position = []
                    Ship.cpu_coordinates = []
                    user_guessed = []
                    user_correct = []
                    cpu_guessed = []
                    cpu_correct = []
                    winner = False
                    break
                elif play_again == "N":
                    print("See you soon!")
                    exit()  # Exit game if user decides not to play again
                else:
                    print(f"Invalid input: {play_again}."
                          "Please type 'Y' or 'N'.")
            except ValueError:
                print("Input must not be empty.")


main()
