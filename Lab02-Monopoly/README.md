## Lab 02 - OOP

In today's lab we will be working on adding some classes to our Monopoly app. By the end of the lab our game will have 3 players who move around the game board buying properties and/or collecting rent.

We will be picking up where Lab 01 left off, but the code base has been updated a little bit. We have split the GUI (graphical user interface) code into view.py and added a controller.py where the logic for the game lives. 

You'll work with a partner for the duration of today's lab. Two people - one computer. (Although if your partner is next to you, you are welcome to each have a computer open in case you want one for reference)

## Task 1 (10 minutes):

We want to complete the class to represent a `Player`

Find a partner and discuss the following (if the discussion isn't flowing put up your hand and ask the lab instructor for some guidance - they might even combine your group with another group to get the discussion going):

1. What attributes should a `Player` have?

2. What methods should a `Player` have?

Some discussion points:

- Does a `Player` buy a `Property` or a `Property` get bought by a `Player`, i.e., which class should the buy method be in?

- How does a `Player` pay rent to another `Player`?


## Task 2 (10 minutes)

Still working with your partner (or group), open up `view.py` and scroll to the bottom and run the `main` method. You should be able to `play` the game although not much happens and it may even be less functional than what you got to in lab 1.

Open the `Player` class in player.py (and gameboard.py and gamesquare.py, and examine the files. These are a few new classes that have been added to the code base.

The `Player` class is incomplete.

Implement the __init__ method of the Player class. Remember that in Monopoly, players start with no properties, and they start at GO. When the controller creates a player it will pass in the player's name and $1500 starting money.

**Your attributes in the Player class should be: private** i.e., they should all start with double underscore.

After you have implemented __init__ implement the `networth` method. This method should return the sum of the player's money and the value of all the properties they own.

## Task 3 (10 minutes)

Implement the `__str__` method for the `Player` and also for the `GameBoard` class. 

Once you have completed these methods run the game and see if the output is as expected.

You might focus on the state of the game for these `__str__` methods: the players and their money for example or which squares they are on. The Gameboard may take advantage of the `__str__` method in the `Player` class that you have written.

## Task 4 (5 mins))

Implement the `move` method in the player class along with the accessor and modifier methods. Many of them are set up to use the @property decorator to allow you to access the double under score attributes.

## Task 5 (20 minutes)

Implement the remaining methods in the `Player` class.

- `buy_property`
- `pay_rent`
- `declare_bankrupt`
- etc

Note when a player lands on a square the controller will try to pay_rent, without checking if rent is due or not. Your method should return 0 if no rent is payable. Similarly the controller will try to buy_property without checking if it is appropriate to do so. Your method should return False if the property is not for sale or it is not a property that can be bought.


**Play the game and see if you need to make any adjustments or can spot any bugs or errors.** Add print statements if necessary to help you debug.
