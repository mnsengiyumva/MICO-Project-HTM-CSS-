# Lab 01 - Project Introduction

Over the course of hte semester, we will be working on a project that builds a working Monopoly game. If you are unfamiliar with Monopoly it is a popular board game that has been around since the early 1900s. You are encouraged to familiarize yourself with the game before getting too far into the labs this semester.

*The Monopoly Game and associated logos, characters and images are trademarked by Parker Brothers and Hasbro and this project is not affiliated with them or the Official Monopoly game in any way.*

In today's lab we will be doing some File I/O and reviewing some of our skills from CS 1910. 

Remember you are encouraged to work with your classmates on the labs, but you must submit your own work. That means you can and should discuss the lab with those around you, but you should be typing in your own code and understanding what you are typing in.

There are two parts to today's lab, the first part is outlined in this document and then the second part is an individual coding challenge to be completed without help from your classmates.

## Grading for Part 1

The grading for part 1 is simple. You will receive full credit (1 point) if you complete the instructions in this document and show your completed work to your lab instructor and 0 points if you do not.


## A quick reminder

The labs are not designed to be tests but rather a way for you to learn and practice the material. If you are struggling with the labs, please reach out to your lab instructor or the professor for help. We are here to help you learn and succeed. If you are **putting forth effort on the labs and keeping pace in the course** you should be able to receive full marks with little concern. 

In the past, students who have focused on the **answers and obtaining the points** in the lab as their prime goal have struggled in the course and found the course stressful.

## Task 1 (5 minutes)

Find someone in the room who has played Monopoly before and ask them the following questions about game rules and house rules. If you do not know the meaning of house rules in games, please consult google (or your AI assistant of choice) before proceeding!

1. At your house when playing Monopoly what happens when you land on free parking?
   * Official rule: Nothing
   * Their house rule: __________

2. At your house what happens if you land on an unowned property and you do not want to buy it?
   * Official rule: Auction
   * Their house rule: __________

3. At your house when a player is in jail are they allowed to collect rent money?
    * Official rule: Yes
    * Their house rule: __________

If any of these rules are unclear ask your colleague to explain them to you.

### Source Code
Visit the source code found in the `monopoly1920` package. You will see a file called `game.py`. Open this file and near to the `TODO: Task 1` comment text, set the three variables pertaining to game rules to either the house rule or the official rule you have discussed with your colleague, depending on your preference.

Run `game.py` and verify that your house rules are displayed.


## Task 2 (10 minutes)

Take 5 minutes and review the code in the `game.py` file. You are not responsible for understanding all of the code at this point, especially the GUI code that uses the TkInter library.

After examining the code, implement the roll_dice function. This function should return the sum of two random numbers between 1 and 6 (representing the roll of a pair of dice). The `random` module is already imported at the top of the `game.py` file for you.

## Task 3 (8 minutes)

Many details for the monopoly game board are stored in a file `resources/data/board.csv`. This file is located in the `monopoly1920` package. Open the file and examine its contents. The file is a comman separated value file wherein the top line describes the columns and each subsequent line represents a square on the game board. For today's lab we are just concerned with the name column. 

In the `game.py` file, implement the `load_board` function. This function should read the `board.csv` file and return an ordered list of the names of the squares on the board (starting with go and ending with boardwalk).

## Task 4 (5 minutes)

This task gives a bit of a chance to ensure everyone is on the same page and following what we are doing. In this task you can assume the list you return in Task 3 is passed into the `get_board_space_name` function along with an index. Implement the function so that it returns the name of the square at the given index.

## Task 5 (8 minutes)

Examine the `resources/images/properties` directory. You'll see all of the monopoly deed cards along with the squares of the monopoly board. The file names correspond to their position on the game board, where 0 is the first square (GO) and travelling clockwise around the board the squares proceed in order 0 to 39 (boardwalk).

Complete the `get_board_square_images` function` in the `game.py` file. This function should return a list of the file names of the images for each square on the board. For example:

```
"resources/images/properties/0.png", 
"resources/images/properties/1.png", 
... 
"resources/images/properties/39.png"
```

If your function is longer than 10 lines then please go back and fix the function to make it more concise.

## Task 6 (12 minutes)

Find someone sitting near to you. Ask them to take control of your computer and try out your program. If you have completed the above 5 Tasks correctly, then the program should crash. Ask them to run the program a few times and see if they can provide some insights as to what makes the program crash (steps to reproduce)

Once they have given you some insights ask them to give you back control of your computer and proceed to debug and fix the problem. 

You may signal to the lab instructor once you have completed this and then wait for further instructions. While you wait (but after the instructor has confirmed your work so far) please feel free to improve, adjust or break any parts of the code or lab.

## Grading 

If you have gotten at least as far as most of the other students in the class when the instructor signals the end of this part of the lab then you will receive full credit for this portion of the lab.