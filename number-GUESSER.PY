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


#Recursion permutation of a word

def permute(text):
    if len(text) == 1:
        return [text]
    else:
        perms = []
        for i in range(len(text)):
            for perm in permute(text[0:i]+text[i+1:]):
                perms.append(text[i]+perm)
        return perms
print(permute('ABC'))


#Recursion Palindome
def is_palindrome(txt, start, end):
    if start >= end:
        return True
    else:
        return txt[start] == txt[end] and is_palindrome(txt, start+1, end-1)
print(is_palindrome('racecar', 0, 5))

#Recursion mazeTraverse
