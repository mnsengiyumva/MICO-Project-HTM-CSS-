## Lab 07 - Recursion

Have you ever played a game and lost to an inferior opponent? While you may help yourself feel better by belittling your opponent using insulting colloquialisms: Beginner's luck, luck of the irish, better to be lucky than good, etc. etc. etc. You may also be curious about how lucky your opponent was.

In today's lab we will build a measure of luck and report each player's luck as the game progresses.

### Learning Outcomes

- Practice using recursion to solve problems
- Building a base case
- Carrying information through recursive calls

### Problem Description

In statistics Expected Value refers to the average value of a random variable. Put simply it is the sum of the possible outcomes multiplied by their probability of occurring. In this lab we will calculate the expected value (change in your money) of turn in a game of Monopoly. 

Before you roll the dice in Monopoly you can look at the game board and see the probability of landing on each space. The probability of landing on a space is the number of ways to land on that space divided by the total number of ways to roll two dice.

For example, the probability of rolling an 9 is 4/36 because there are 4 ways to roll a 9 (3,6; 4,5; 5,4; 6,3) and there are 36 possible rolls of two dice.

Suppose that you are 9 squares away from a square that I own and the rent is \$100. Then you would have a 4/36 = 1/9 chance of landing on my square and paying me \$100 during your turn. If every other possible roll landed on an unowned square (no rent due) then you might say you expect to pay me \$100/6 = \$16.67. **But** this isn't quite accurate because:

In Monopoly if you roll doubles you get to roll again, but if you roll doubles 3 times then you go directly to jail. So if I own a property 9 squares away from you, you could roll a 9 and pay me \$100, or you could roll a 2 (1+1) followed by a 7 (there are 6 ways to roll a seven), or you could roll a 4 (2+2) followed by a 3 or a 2 followed by a 2 followed by a 5 ... you get the idea there are a number of ways that you might land on my square and pay me $100 in that same turn.

In this lab we will calculate the expected value of your turn in Monopoly. We will do this by calculating the probability of landing on each square and multiplying that probability by the rent due on that square. We will then sum these values to get the expected value of your turn. We will do this using recursion because on some rolls (doubles) we get to roll again from our new square. 

After we have calculated your expected value we will compare that to what actually happens in the game. If more often than not you end up paying out more than the expected value then you are considered unlucky, if you pay out less than the expected value then you are considered lucky. We have a measure of luck! 

### Instructions    


## Task 1 (10 minutes)

Add a `self.__luck` attribute to the Player class along with a an `@property` `luck` and `@luck.setter` . This will be an integer that starts at 0. Then as each turn progresses it will track the outcome of the player's turn compared to our prediction. Edit the `__str__` method to ensure that luck is printed out with the player's name (amoung the other information).

For example if we predict the player will lose \$16.82 on a turn but they actually lose $200 then their luck would go down by -183.18. If they lose nothing then their luck would increase by 16.82.

For this Task we just add the attribute and ensure it is used in the str method. If the property is set correctly the controller will use this `.luck` property to track the player's luck.

Play the game to ensure everything is working.

## Task 2 (30 minutes)

Finish the GameBoard class method: `calculate_expected_value`. This method will calculate the expected value of a turn in Monopoly. 

First let's start with a known value and build from there. 

At that start of the game before anyone owns anything the expected outcome of the first turn is to pay out $16.82. To arrive at this value we first note that with what we currently have implemented in the game the only 2 squares on the board that the user must pay on are income tax (square 4: \$200) and luxury tax (square 38: \$100). 

From Go at the start of the game the user cannot land on Luxury tax = square 38 (the most they can roll is 12 (doubles) + 12 (doubles) + 11 = 35) but they can land on income tax in the following ways: 1 + 3, 2 + 2 (doubles), 3 + 1 and 1+1 (doubles) followed by another (1+1). Therefore at the start of the game the first player has an expected outcome of 1/36 * 200 (roll 1+3) + 1/36 * 200 (roll 2+2) + 1/36 * 200 (roll 3+1) + 1/36 * 1/36 * 200 (roll 1+1 followed by another 1+1) = 16.82. We expect the person to lose\$16.82.

`calculate_expected_value` should return the expected value of the turn and take as input a position on the game board (int) and the number of times that the player has rolled doubles (int):

```python
def calculate_expected_value(self, position: int, doubles: int) -> float:
```

Take a crack at this method. You might like to use a nested for loop to simulate the possible rolls of the dice:

```python
def calculate_expected_value(self, position: int, doubles: int) -> float:
    expected = 0 #store the answer here
    for i in range(1,7):
        for j in range(1,7):
            
            next_position = (position + i + j) % 40
            
            #each die roll combination has probability 1/36
          
            #Did you roll your third doubles? Then add nothing
            #to the total (because you go directly to jail)
            if i == j and doubles == 2:
                continue
            
            #continue calculating the expected value from here

```

Note that the GameSquare class has a method to determine the rent or tax on a square: `def calculate_rent_or_tax(self, dice_sum):` The dice sum has to be passed to it since water works and electric company use this to calculate the rent. 

When doubles are rolled don't forget to increment the doubles variable and pass it to the next recursive call. Remember that the game board has a variable for the current player and the player class has a variable for the current position.

Play the game and see if your method returns the expected value of the first turn to be $16.82.

If not try using the debugger to help flush out issues with your code. Put a break point in the calculate_rent_or_tax method and step through the code to see if it is working as expected.

If that fails consult your neighbor or the instructor for help.

Once you have got things working, test your method by having the first player buy the first property they land on and then notice if the second player's expected value has increased by the correct amount. Continue playing until someone has to pay a large rent or tax and notice if their luck has decreased by the correct amount.

If you have completed the task early check in with your neighbour to see if they may be stuck in the debugging process and offer a hand.




