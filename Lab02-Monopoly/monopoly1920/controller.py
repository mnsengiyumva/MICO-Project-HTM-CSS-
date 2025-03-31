import os
import view
import random
import gameboard
import player as plr # avoid naming conflict with the player module
import gamesquare

class Controller:
    """Control the game flow"""

    def __init__(self, root):

        #for now we have references to the backend and frontend objects
        #tight coupling is not ideal, but we will refactor later
        self._view = view.View(root, self)

        csv_path = os.path.join("resources", "data", "board.csv")
        players = self._create_players(3)
        self._gameboard = gameboard.GameBoard(csv_path, players)

    def _create_players(self, num_players):
        """Create num_players players and return a list of them"""
        players = []
        for i in range(num_players):
            player = plr.Player(f"Player {i}", 1500)
            players.append(player)
        return players

    def _roll_dice(self):
        """Simulate the rolling of two dice
            :return the sum of two random dice values
        """
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        return dice_sum

    def _handle_roll_dice(self):
        """Function to handle the roll dice button click event"""
        dice_sum = self._roll_dice()
        player = self._gameboard.get_current_player()

        #move the player
        player.move(dice_sum)
        position = player.position
        square = self._gameboard.get_square(position)

        #pay the rent
        rent = player.pay_rent(square,dice_sum)
        if rent == 0:
            self._buy_square()
        else:
            print(f"rent paid: {rent}")

        #no money left?
        if player.money < 0:
            player.declare_bankrupt()
            self._gameboard.remove_player()

    def _buy_square(self):
        """try to buy the square the active player is currently on"""
        player = self._gameboard.get_current_player()
        position = player.position
        square = self._gameboard.get_square(position)
        buy = player.buy_property(square)
        if buy:
            print(f"Square bought {square}")

    def button_clicked(self, button):
        """Handle View button click events"""
        print(f"Button clicked: {button}")

        player = self._gameboard.get_current_player()

        if button == "roll":
            self._handle_roll_dice()

            square = self._gameboard.get_square(player.position)
            money = player.money

            msg = f"{player.name} landed on {square} and now has ${money}."

            self._gameboard.next_turn()

            self._view.update_state("roll",msg)
            self._view.update_state_box(str(self._gameboard))



