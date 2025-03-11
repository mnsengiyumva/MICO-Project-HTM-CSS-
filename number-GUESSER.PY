import random
top_of_the_range = input('Type a number: ')

if top_of_the_range.isdigit():
    top_of_the_range = int(top_of_the_range)
    if top_of_the_range <= 0:
        print('Please type a number greater than zero next time.')
        quit()
else:
    print('Please type a number next time')

random_number = random.randint(0, top_of_the_range)
print(random_number)
guesses = 0
while True:
    guesses +=1
    user_gues = input('What is your guess? ')
  
    if user_gues.isdigit():
        user_gues = int(user_gues)
        if user_gues == random_number:
            print('You got it right')
            break
        else:           
            print('you Got it wrong')
    else:
        print('Please type a number next time')
    
print('You got it',guesses,'times')
