import player
import gamesquare

class GameBoard:

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
        #players enters the class as an ordered list of players
        self.__players = players
        self.__total_turns = 0
        self.__turn = 0

        # Task 1: use a queue to manage the players

        #pop the first player into a variable

    def next_turn(self):
        #Task 1: update this method
        self.__turn = (self.__turn + 1) % len(self.__players)

    def get_current_player(self):
        """return the current player"""
        #Task 1: update this method
        return self.__players[self.__turn]

    def get_all_squares(self):
        return self.__properties

    def get_square(self, index):
        return self.__properties[index]


    #Task 1: remove this method
    @property
    def players(self):
        return self.__players

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
        board_str = "player - cash - net worth - position\n"
        #Task 1: Process the current player first: board_str += ...
        #then verify the below code works for the remaining players
        for player in self.__players:
            board_str += f"{player} "
            board_str += f"{self.get_board_square(player.position).name}\n"

        return board_str

