import player
import gameboard


class GameSquare:
    def __init__(self, name, price, rent, space, color, is_utility, is_railroad):
        """Constructor for the GameSquare class"""
        self.__name = name
        self.__price = price
        self.__rent = rent
        self.__color = color
        self.__space = space
        self.__is_utility = is_utility
        self.__is_railroad = is_railroad
        self.__owner = None

        #add an is_mortgaged attribute
        self.__is_mortgaged = False

    # accessor methods
    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def rent(self):
        return self.__rent

    @property
    def color(self):
        return self.__color

    @property
    def space(self):
        return self.__space

    @property
    def is_utility(self):
        return self.__is_utility

    @property
    def is_railroad(self):
        return self.__is_railroad

    @property
    def is_mortgaged(self):
        return self.__is_mortgaged

    #Add methods to mortgage and unmortgage a property
    #remember to add a 10% fee to unmortgage
    def mortgage(self):
        """Function to mortgage a property
        return True if mortgaging was successful and False otherwise"""
        amt = self.price // 2
        if not self.__is_mortgaged:
            self.__is_mortgaged = True
            self.owner.money += amt
            return True
        return False

    def unmortgage(self):
        """Function to unmortgage a property if the player has the money
        and the property is currently mortgaged
        return True if the unmortgage was successful and False otherwise"""
        # add a 10% fee to unmortgage
        amt = self.price // 2
        amt = amt + amt // 10

        if self.owner.money >= amt and self.__is_mortgaged:
            self.__is_mortgaged = False
            self.owner.money -= amt
            return True

        return False

    def can_be_purchased(self):
        """Function to determine if a square can be purchased"""
        if self.owner is None:
            if (self.space == "Tax" or self.space == "Chance" or self.space == "Chest"
                    or self.space == "GotoJail" or self.space == "Jail"
                    or self.space == "Parking" or self.space == "Go"):
                return False
            else:
                return True

    def calculate_rent_or_tax(self, dice_sum):
        """Function to calculate the rent or tax for a square"""

        if self.owner is None and self.space != "Tax" or self.__is_mortgaged:
            return 0
        if self.is_utility:
            return 4 * dice_sum
        if self.is_railroad:
            return 25 * (2 ** (self.owner.railroad_count - 1))

        return self.rent

    def __str__(self):
        """Function to return a string representation of the GameSquare object"""
        return f"{self.name} - {self.price} - {self.rent}"
