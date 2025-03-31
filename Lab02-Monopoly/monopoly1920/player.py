import gameboard
import gamesquare

class Player:
    """Player class to represent a player in the game"""

    def __init__(self, name, money):
        """Constructor for the Player class
        all players start at position 0 (GO) with no properties"""

        #self.__name = name
        #self.__money = money
        #self.__properties = []
        #self.__board_position = 0
        #self.__doubles_count = 0
        self.__bankrupt_declared = False
        #self.__utility_count = 0
        #self.__railroad_count = 0

    def buy_property(self, board_property : gamesquare) -> bool:
        """Function to attempt to buy a property
        you might access: board_property.can_be_purchased()
        to check if the property can be purchased
        :param board_property: the property to buy
        :return: True if the property was bought, False otherwise
        """
        #placeholder always return False until implemented
        return False

    def pay_rent(self, square : gamesquare, dice_sum: int) -> int:
        """Function to attempt to pay rent (or tax) on a square
        note that for income tax as an example the rent is 200 even though
        it is tax. You likely want to use the calculate_rent_or_tax function from gamesquare
        :param square: the square to pay rent on (or tax)
        :param dice_sum: the sum of the dice
        :return: the amount of rent paid or 0 if no rent is paid
        """
        #placeholder always 0 until implemented
        return 0

    def net_worth(self):
        """Function to calculate the net worth of the player which is the sum
        of their money and the price of all their properties
        :return network of the player"""

        #placeholder return 0 until implemented
        return 0

    def move(self, spaces : int):
        """Function to move the player on the board
        ensure to check if they passed go and if so increase money by $200"""


    def declare_bankrupt(self):
        """Function to declare bankruptcy"""


    #Accessor and modifiers

    @property
    def money(self):
        # placeholder always return 0 until implemented
        return 0


    @money.setter
    def money(self, money):
        """Function to set the money of the player"""


    @property
    def name(self):
        # placeholder always return player until implemented
        return "player"


    @property
    def position(self):
        """which square (number) the player is currently on"""
        #placeholder always return 0 (go) until implemented
        return 0

    @property
    def bankrupt_declared(self):
        #placeholder return False until implemented
        return False

    @property
    def railroad_count(self):
        """how many railroads does the player own?
        :return the number of railroads the player owns"""
        #placeholder always return 0 until implemented
        return 0

