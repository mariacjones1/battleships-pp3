import random
import time


def start_game():
    """
    Prints welcome message and instructions,
    and gives user the opportunity to start the game
    """
    print("Welcome to Battleships!\n"
          "The aim of the game is to find and sink your opponent's"
          "battleships before they sink yours.\n"
          "Choose the location for each of your ships, while the computer"
          "generates random positions, then take it in turns to guess"
          "where each other's ships are.\n"
          "Ready to play?")

    while True:
        user_start = input("Y/N\n").upper()

        try:
            if not user_start:
                raise ValueError
            elif user_start == "Y":
                break
            elif user_start == "N":
                print("Maybe next time!")
                exit()
            else:
                print(f"Invalid input: {user_start}. Please type 'Y' or 'N'.")
        except ValueError:
            print("Input must not be empty.")

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
            if not username:
                raise ValueError
            elif username.isalnum() is False:
                raise TypeError
            elif len(username) < 3:
                raise ValueError
        except ValueError:
            print("Username must be at least 3 characters.")
        except TypeError:
            print("Username should use numbers and letters only.")
        else:
            break

    return username


class Ship:
    """
    Ship class
    """
    user_coordinates = []
    cpu_coordinates = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.position = []
        self.orientation = None

    def set_position(self):
        """
        Allows the user to set the coordinates for each ship
        """
        letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                            "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

        while not self.position:
            print(f"Set the coordinates for the {self.name} "
                  f"(length = {self.length})")
            while True:
                column = input("Choose a column from A-J: ").upper()
                try:
                    if not column:
                        raise ValueError
                    elif column in "ABCDEFGHIJ" and len(column) == 1:
                        column = letter_to_number[column]
                        break
                    elif column.isalpha() is False:
                        raise TypeError
                    else:
                        print("Invalid letter.")
                except ValueError:
                    print("Input must not be empty.")
                except TypeError:
                    print("Input must be a letter.")

            while True:
                try:
                    row = int(input("Choose a row from 1-10: "))
                    if not row:
                        raise ValueError
                    elif row >= 1 and row <= 10:
                        row -= 1
                        break
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Invalid input. Please type a letter from 1-10.")

            while True:
                print("Now choose the ship's orientation:\n"
                      "Horizontal ('H') or vertical ('V')?")
                self.orientation = input().upper()
                try:
                    if not self.orientation:
                        raise ValueError
                    elif self.orientation == "H":
                        if column + self.length > 10:
                            break
                        else:
                            while len(self.position) < self.length:
                                self.position.append((column, row))
                                column += 1
                        break
                    elif self.orientation == "V":
                        if row + self.length > 10:
                            break
                        else:
                            while len(self.position) < self.length:
                                self.position.append((column, row))
                                row += 1
                        break
                    else:
                        print("Please input only 'H' or 'V' for orientation.")
                except ValueError:
                    print("Input must not be empty.")

            if (len(Ship.user_coordinates + self.position) !=
                    len(set(Ship.user_coordinates + self.position))):
                self.position = []
                print("Ship doesn't fit; please try again.")
            elif not self.position:
                print("Ship doesn't fit; please try again.")
            else:
                Ship.user_coordinates = Ship.user_coordinates + self.position
                return Ship.user_coordinates

    def random_position(self):
        """
        Generates random positions for each ship
        """
        orientation = ["H", "V"]
        print(f"Setting computer coordinates for {self.name}...")
        while not self.position:
            column = random.randint(0, 9)
            row = random.randint(0, 9)
            self.orientation = random.choice(orientation)

            if self.orientation == "H":
                if column + self.length > 10:
                    pass
                else:
                    while len(self.position) < self.length:
                        self.position.append((column, row))
                        column += 1
            elif self.orientation == "V":
                if row + self.length > 10:
                    pass
                else:
                    while len(self.position) < self.length:
                        self.position.append((column, row))
                        row += 1

            if (len(Ship.cpu_coordinates + self.position) !=
                    len(set(Ship.cpu_coordinates + self.position))):
                self.position = []
            elif not self.position:
                self.position = []
            else:
                Ship.cpu_coordinates = Ship.cpu_coordinates + self.position
                return Ship.cpu_coordinates


def guess_coordinates(guessed, coordinates):
    """
    User guesses ship coordinates, which are checked
    against previously guessed coordinates and computer
    ship coordinates
    """

    letter_to_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
                        "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
    guess = ()

    while not guess:
        while True:
            guess_column = input("Guess a column from A-J: ").upper()
            try:
                if not guess_column:
                    raise ValueError
                elif guess_column in "ABCDEFGHIJ" and len(guess_column) == 1:
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
                    raise ValueError
                elif guess_row >= 1 and guess_row <= 10:
                    guess_row -= 1
                    break
                else:
                    print("Invalid number.")
            except ValueError:
                print("Input must be a number 1-10.")

        guess = (guess_column, guess_row)

        if guess in guessed:
            print("Coordinate already guessed! Please guess again.")
            guess = ()
        else:
            guessed.append(guess)
            if guess in coordinates:
                print("Hit!")
            else:
                print("Miss!")


def guess_random_coordinates(guessed, coordinates):
    """
    Generates random coordinates for computer guesses and makes sure
    coordinate has not already been guessed
    """
    number_to_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    while True:
        guess_column = random.randint(0, 9)
        guess_row = random.randint(0, 9)
        guess = (guess_column, guess_row)
        print(f"Computer guessed ({number_to_letter[guess_column]}, "
              f"{guess_row + 1})")
        if guess in guessed:
            break
        else:
            guessed.append(guess)
            if guess in coordinates:
                print("Hit!")
            else:
                print("Miss!")
            break


def print_board(board, coordinates, guessed, correct, player):
    """
    Prints user board showing set coordinates and
    correct computer guesses
    """

    print("  | A | B | C | D | E | F | G | H | I | J |\n"
          "   ----------------------------------------")
    row_number = 1
    for row in board:
        if row_number < 10:
            print(str(row_number) + " |", end="")
        else:
            print(str(row_number) + "|", end="")
        for i in row:
            if i in guessed and i in coordinates:
                print(" ⊗ |", end="")
                correct.append(i)
            elif i in coordinates and player == "user":
                print(" ⬤ |", end="")
            elif i in guessed:
                print(" ~ |", end="")
            else:
                print(" ○ |", end="")
        print("\n")
        row_number += 1


user_carrier = Ship("Carrier", 5)
user_battleship = Ship("Battleship", 4)
user_destroyer = Ship("Destroyer", 3)
user_submarine = Ship("Submarine", 3)
user_patrol_boat = Ship("Patrol Boat", 2)

cpu_carrier = Ship("Carrier", 5)
cpu_battleship = Ship("Battleship", 4)
cpu_destroyer = Ship("Destroyer", 3)
cpu_submarine = Ship("Submarine", 3)
cpu_patrol_boat = Ship("Patrol Boat", 2)


def main():
    """
    Runs main game functions
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

            # Computer guesses
            print("Computer guessing...")
            time.sleep(2)
            guess_random_coordinates(cpu_guessed, Ship.user_coordinates)
            time.sleep(1)
            print(f"{username}'s board:")
            print_board(board, Ship.user_coordinates, cpu_guessed, cpu_correct,
                        "user")
            time.sleep(1)

            # Declare winner
            if len(set(user_correct)) == 17:
                print("Congratulations, you win!")
                winner = True
            elif len(set(cpu_correct)) == 17:
                print("Computer wins!")
                winner = True
            else:
                winner = False

        while True:
            play_again = input("Would you like to play again (Y/N)? ").upper()
            if play_again == "Y":
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
                exit()
            else:
                print(f"Invalid input: {play_again}. Please type 'Y' or 'N'")


main()
