# this game is about number 21. The players will guess the number

number_player = int(input("How mamny number of players are playing? "))

players_names = []


for i in range(number_player):

    names = input("Enter the name of the player: ")

    players_names.append(names)

for i in range(1, 22):

    for name in players_names:
        name = i
        if name == 21:
            players_names.remove(name)
            
