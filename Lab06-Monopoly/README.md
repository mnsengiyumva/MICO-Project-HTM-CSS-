## Lab 06 - Stacks and queues

In today's lab we will add some queues and stacks to help with our practice on those structures. 

Firstly we will alter the gameboard so that the current player is tracked not using an int (self.__turn) but rather a queue. 

Queues are a great option for tracking the order of things and there are a few advantages over the current int implementation. Practically speaking the current implementation is fine and mostly this will give us some practice with queues but some advantages:

1. we will avoid problems with modular arithmetic: if there are 3 players, we no longer need to do things like `self.__turn = self.__turn % 3`
2. we will dequeue (pop(0)) the current player out of the queue of players when it is there turn, this gives easier access to the current player (no need to reference `self.__players[self.__turn]` all the time)
3. if someone goes bankrupt no need to worry about finding them in this list of players and removing them. Also no need to worry that someone has code out there with a 3 or a self.num_players = 3 hardcoded in it.

We will use Stacks in a little bit of a modification to the typical Monopoly rules. 

In typical Monopoly rules you can mortgage your property to the bank for half of the purchase price. At any point you can pay a 10% fee (plus the mortgage price) to unmortgage the property. No rent is collected on Mortgaged properties. 
In our version you will only be allowed to unmortgage properties in a LIFO (last in first out) order. This means that if you mortgage a property you must unmortgage it before you can unmortgage any other properties. For example if you owned and mortgaged (in this order) Boardwalk (facevalue 400, mortgage amount 200), Park Place (facevalue 350, mortgage amount 175), and St. James Place (facevalue 180, mortgage amount 90) you would have to unmortgage them in the order St. James Place, Park Place, Boardwalk.

If you want to work in a team for today you, can but it is designed to operate well as a solo effort lab.

### Learning Objectives

- Practice with data structures in a practical manner.

## Task 1 (5 minutes):

Open view.py and run the program. You should become a little bit familiar with the new gameplay features: buying properties, mortgaging properties and ending your turn are all part of the player's decisions during their turn now.

The general flow for a turn in the game is now:

1. Anytime in their turn they may mortgage a property that they own
2. Roll the dice
3. After rolling the dice they may buy a property if they land on an unowned property
4. If they roll doubles they should repeat from step 2 (roll again)
5. They can end their turn anytime after rolling the dice and not getting doubles

## Task 2 (20 minutes) Use a Queue to track the current player:

Open `gameboard.py `

1. Notice that we already track players in a structure called `self.__players` which is a list of player objects. We will use operate on this list as if it were a queue.

2. Add an instance attribute: `self.__current_player` which will represent the player's whose turn it currently is. At the bottom of the `__init__` method dequeue the first players from the list of players (self.__players) and set it to `self.__current_player`. 

Ask your neighbour if you do not recall how to dequeue a player from a queue (that is actually a list).

3. In the `next_turn` method, enqueue the current player back into the list of players  (queue of players) and dequeue the next player to be the current player and return their name.

4. Update the `__str__` method so that it converts the current player to a string first and then iterates over the rest of the players.

5.  Update the `get_current_player` method so that it returns the current player.

6. Remove the `__turn` attribute from the class. Remove the players property from the class.

Play the game an ensure that nothing has changed (except that the current player appears at the top of the left status text field)


## Task 3 (25 minutes) Use a Stack to track the order of unmortgaging properties:

Mortgaging properties is already implemented.
Play the game an verify that you can mortgage properties.

We will add the ability to unmortgage properties. 

1. In the view we will need to trigger a new Event when the unmortgage button is pressed. Edit the `_action_taken` method so that an Event is triggered. Recall that the View communicates with the Controller through Events. To help the Controller know what the Event is about, pass the string "unmortgage" as the argument to the Event and leave the second argument (data) as None. 

2. The Event class has a debugging print out when Events are created. Verify that your new code triggers an "unmortgage" Event when you click the button. 

3. In gamesquare.py file add a new method called `unmortgage` that will unmortgage the property. This method should check if the owner has enough money to unmortgage the propery and if they do then proceed to unmortgage it. You should consult the mortgage property method to gain some insight. Do not forget to charge the player a 10% fee to unmortgage the property. Return True if the unmortgage was successful and False otherwise (not enough money).

4. In player.py file in the Player class `__init__` method add an empty stack attribute to track properties that have been mortgaged. You can use a list as the stack.

5. Edit the `mortgage_property()` method. If `p.mortgage` was successful push the property to the top of the stack of mortgaged properties:
```python
            def mortgage_property(self, deed_name):
        """Function to mortgage a property"""
        for p in self.__properties:
            if p.name == deed_name:
                res = p.mortgage()
                if res:
                    self.__mortgaging_order.append(p) #use your stack name here
                return True
        return False
```

6. Add an `unmortgage_property(self):` method to the player class. This method should pop the top property off the stack of mortgaged properties and call the `unmortgage` method on it. If the unmortgage is successful then return the property name, otherwise return the empty string "".

7. Finally update the Controller class 

a. In the `_add_listeners` method ensure you listen for the "unmortgage" Event and call a new method called `self._unmortgage`.

b. Create the `_unmortgage` method:
```python
    def _unmortgage(self):
        """Function to unmortgage a property"""
        player = self._gameboard.get_current_player()
        deed_name = player.unmortgage_property()
        if deed_name != "":
            observer.Event("update_state", f"Unmortgaged: {deed_name}")
            observer.Event("update_state_box", str(self._gameboard))
        
```



# Task 4 (5 minutes) 

If you have linked everything up correctly your game should allow properties to be mortgaged and unmortgaged (using the LIFO order). 

Play the game and verify that things are working.