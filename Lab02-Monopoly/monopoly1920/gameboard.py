import player
import gamesquare

class GameBoard:
    """Class to represent the game board"""

    __boardCSV = {
        "name": 0,
        "space": 1,
        "color": 2,
        "position": 3,
        "price": 4,
        "build": 5,
        "rent": 6,
        "rent1": 7,
        "rent2": 8,
        "rent3": 9,
        "rent4": 10,
        "rent5": 11,
        "hotelcost": 12,
        "owner": 13,
        "houses": 14,
        "groupmembers": 15
    }

    def __init__(self, properties_path, players ):
        self.__properties = self._load_game_board(properties_path)
        self.__players = players
        self.__turn = 0
        self.__total_turns = 0

    def next_turn(self):
        self.__turn = (self.__turn + 1) % len(self.__players)

    def get_current_player(self):
        return self.__players[self.__turn]

    def get_all_squares(self):
        return self.__properties

    def get_square(self, index):
        return self.__properties[index]

    def remove_player(self):
        self.__players.pop(self.__turn)
        self.__turn = self.__turn % len(self.__players)

    @property
    def players(self):
        return self.__players


    # TODO: Complete this function
    def get_board_square(self, index):
        """Function to return the board square at the given index
            @:param game_board: an ordered list of Properties
            @:param index: the index of the space on the board
            @:return square: the square at the given index
        """
        square = self.__properties[index]
        return square

    def _load_game_board(self, csv_path):
        """Function to load and return the game board from a file
            :param csv_path: the path to the csv file containing the board data
            :return game_board: an ordered list of the game board spaces
                                 where the 0th index is "GO" and the indices
                                 proceed clockwise around the board
        """
        properties = []

        f = open(csv_path, "r")
        next(f)  # skip the header row of the file, we don't need it for this game
        for line in f:
            line = line.strip()
            line = line.split(",")

            # create a property object
            utility = line[self.__boardCSV["space"]] == "Utility"
            railroad = line[self.__boardCSV["space"]] == "Railroad"
            sq = gamesquare.GameSquare(name=line[self.__boardCSV["name"]], price=int(line[self.__boardCSV["price"]]),
                                      rent=int(line[self.__boardCSV["rent"]]), color=line[self.__boardCSV["color"]],
                                      is_utility=utility, is_railroad=railroad, space=line[self.__boardCSV["space"]])
            properties.append(sq)
        f.close()

        return properties

    def __str__(self):
        """convert the state of the game board into a string"""

        board_str = "here is information about the game board\n"

        return board_str