import random

words = ["rock", "paper", "scisor"]

def computer():

    comp = random.choice(words)
    return comp

def play():

    player = input("Who is playing: ")
    print(f"Welcome {player}. Good luck.")

    while True:
        user = input("rock/paper/scisor: ")

        if user.lower() == "rock" and computer() == "paper":
            print(f"{player} choice: {user}")
            print(f"Computer choice: {computer()}")
            print("Computer won!")
        elif user.lower() == "paper" and computer() == "scisor":
            print(f"Player choice: {user}")
            print(f"Computer choice: {computer()}")
            print("Computer won!")
        elif user.lower() == "paper" and computer() == "rock":
            print(f"{player} choice: {user}")
            print(f"Computer choice: {computer()}")
            print("Computer won!")
        elif user.lower() == computer():
            print(f"{player} choice: {user}")
            print(f"Computer choice: {computer()}")
            print("Tie!")
        
        else:
            print(f"{player} choice: {user}")
            print(f"Computer choice: {computer()}")
            print(f"Congratulations. {player} won!")

        keep_playing = input('Do you want to keep playing? (y/n): ')
        if keep_playing.lower() == 'y':
            continue
        else:
            print("Thank you for playing see you next time")
            break


computer()
play()

