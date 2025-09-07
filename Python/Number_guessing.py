import random

trials = 5

play  = input("Welcome to the game. Do you want to proceed with playing? (y/n): ")

rand_number = random.randrange(1,100)



if play.lower() != 'y' and play.lower() != 'n':
    print("Your choice is incorect. Try again later!")
    
elif play.lower() == 'n':
    print("Thank you. See you next time.")


else:




    while trials >0:
    
        

        user = int(input('Enter your guess: '))
        print(f"Your guess: {user}")

        if user < rand_number:
            print("Too low. Try higher number next time")
            trials -= 1
        elif user> rand_number:
            print("Too high. Try a lower number nextime")
            trials -= 1

        elif user == rand_number and trials >0:
            print(f"Congratulations, you won you guessed {user} and the random number is {rand_number} ")
            break
        if trials<=0:
            print("You lost. Thank you for playing")
    
