import gameboard
import gamesquare
import observer


class Player:
    """Player class to represent a player in the game"""

    def __init__(self, name, money):
        """Constructor for the Player class"""
        self.__name = name
        self.__money = money
        self.__properties = []
        self.__board_position = 0
        self.__doubles_count = 0
        self.__bankrupt_declared = False
        self.__utility_count = 0
        self.__railroad_count = 0

        #big numbers are lucky, negative numbers are unlucky
        self.__luck = 0

        #add a Data structure to track mortgaging order
        self.__mortgaging_order = []

    def __str__(self):
        """String representation of the player"""
        return f"{self.__name} - {self.money} - {self.net_worth()} luck:{self.__luck:.1f}"

    def buy_property(self, board_property):
        """Function to attempt to buy a property"""
        if not board_property.can_be_purchased():
            return False

        self.__properties.append(board_property)
        self.__money -= board_property.price
        board_property.owner = self
        if board_property.is_utility:
            self.__utility_count += 1
        if board_property.is_railroad:
            self.__railroad_count += 1

        return True

    def pay_rent(self, square, dice_sum):
        """Function to attempt to pay rent or tax on a square"""
        if square.owner is self:
            return 0
        rent = square.calculate_rent_or_tax(dice_sum)
        self.__money -= rent

        if square.owner is not None:
            square.owner.money += rent
        return rent

    def mortgage_property(self, deed_name):
        """Function to mortgage a property"""
        for p in self.__properties:
            if p.name == deed_name:
                res = p.mortgage()
                if res:
                    self.__mortgaging_order.append(p)
                return True
        return False

    def unmortgage_property(self):
        """Function to unmortgage a property
        return the name of the property that was unmortgaged
        or the empty string if no such property exists"""
        if len(self.__mortgaging_order) == 0:
            return ""
        p = self.__mortgaging_order.pop(0)
        res = p.unmortgage()
        if not res:
            return ""
        return p.name


    def net_worth(self):
        """Function to calculate the net worth of the player"""
        return self.money + sum(p.price for p in self.__properties)

    def collect(self, amount):
        """Function to collect money"""
        self.__money += amount

    def move(self, spaces):
        """Function to move the player on the board"""
        prior_position = self.__board_position
        self.__board_position += spaces
        if self.__board_position >= 40:
            self.__board_position -= 40
        # careful about passing go
        if self.__board_position < prior_position:
            observer.Event("update_state", "pass_go +200")
            self.collect(200)

    @property
    def doubles_count(self):
        return self.__doubles_count

    @doubles_count.setter
    def doubles_count(self, doubles_count):
        self.__doubles_count = doubles_count

    @property
    def luck(self):
        return self.__luck

    @luck.setter
    def luck(self, luck):
        self.__luck = luck

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__board_position

    @property
    def bankrupt_declared(self):
        return self.__bankrupt_declared

    def declare_bankrupt(self):
        self.__bankrupt_declared = True

    @property
    def railroad_count(self):
        return self.__railroad_count

    @property
    def properties(self):
        return self.__properties

    @property
    def deed_names(self):
        return [p.name for p in self.__properties]