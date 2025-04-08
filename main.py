#Cyber security like example (word encycription)

import random
import string
import copy
class Encrypting:
    def __init__(self, text):
        self.text = text
    def message_encrypting(self):
        characters = ' ' + string.punctuation + string.ascii_letters + string.digits
        letters = []
        for letter in characters:
            letters.append(letter)
        cipher = copy.copy(letters)
        random.shuffle(cipher)
        cipher_text = ''
        for l in self.text:
            letter_index = letters.index(l)
            cipher_text += cipher[letter_index]
        return cipher_text
    def __str__(self):
        return f'The {self.text} message is encrypted into {self.message_encrypting()}'



text1 = Encrypting('I sing')
text1.message_encrypting()
print(text1)
#descrypting a message

#cipher_message = input('Enter the message you want to descrypt: ')
from collections  import deque
class Stack:
    def __init__(self):
        self.dq = deque()
    def push(self,item):
        self.dq.append(item)
    def pop(self):
        return self.dq.pop()
    def peek(self):
        return self.dq[-1]
    def __len__(self):
        return len(self.dq)
def reverse(strng):
    stack = Stack()
    for char in strng:
        stack.push(char)
    rev = ''
    for l in range(len(stack)):
        rev += stack.pop()
    return rev
print(reverse('abc'))

#finding numbers in st2 which are not in s1
def findAdded(st1, st2):
    s1 = []
    s2 = []
    result = ''
    for i in st1:
        s1.append(int(i))
    for j in st2:
        s2.append(int(j))
    for k in s1:
        if k in s2:
            s2.remove(k)
    sorted_num = sorted(s2)
    for n in sorted_num:
        result += str(n)
    return result
#test indAdded('44554466', '447554466')
#Expected output 7


def is_isogram(st):

    if len(st) !=0:
        text = ''
        result = []
        for i in str(st):
            if i.isalpha():
                text += i
        for i in text.lower():
            if i not in result:
                result.append(i)
        if len(result) == len(text) or len(text)%len(result)==0:
            return True
        else:
            return False

    else:
        return False
    
#Counting sentence

print(is_isogram("Isogram"))

import  string
letters = string.ascii_letters
dig = string.digits
lower = [x for x in letters[:26]]
upper = [y for y in letters[26:]]
digi = [n for n in dig]
su = 0
for l in s:
    if l in lower:
        su += lower.index(l)+1
    if l in upper:
        su += (upper.index(l)+1)*2
    if l in dig:
        su+= digi.index(l)

import random
words = ('Banana', 'orange', 'apple')

hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "  "),
               4:(" o ",
                  "/|\\",
                  "   ",
                  ),
               5:(" o ",
                  "/|\\",
                  "/  ",
                  ),
               6:(" o ",
                  "/|\\",
                  "/ \\  ",
                  )}
def display_man(wrong_guesses):
    print("****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************")
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrrong_guesses =0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrrong_guesses)
        display_hint(hint)
        guess = input('Enter a letter: ').lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalind In put")
            continue
        if guess in guessed_letters:
            print(f'Our {guess} is already Guessed')
            continue
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrrong_guesses +=1

if __name__ == "__main__":
    main()
print()


# calendar and turtle generation
import calendar
year = 2025
month = 1
print(calendar.month(year, month))
#Drawing a turtle using the turtle method
import turtle
window = turtle.Screen()
drawer = turtle.Turtle()
for i in range(20):
    drawer.forward(250)
    drawer.right(250)

#Password creation

def create_password(password_length = 10):
    letters = string.ascii_letters
    digit = string.digits
    specil_characters = string.punctuation
    alphabet = letters + digit +specil_characters
    pwd = ''
    pw_strong = False
    while not pw_strong:
        for i in range(password_length):
            pwd  += ''.join(secrets.choice(alphabet))
        if (any(char in specil_characters for char in pwd)) and sum(char in digits for char in pwd) >=2:
            pw_strong = True
    print(pwd)

#Implementing class shape
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height
    def area(self):
        return self.length*self.height
    def __str__(self):
        return f"The area of rectancle with length {self.length} and heigt {self.height} is {self.length*self.height} square meters"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.ceil(self.radius**2*math.pi)
    def __str__(self):
        return f"The area of the circle with radius {self.radius} is {math.ceil(self.radius**2*math.pi)} square meters"
r1 = Rectangle(3,4)
print(r1.area())
print(r1.__str__())
c1 = Circle(4)
print(c1.area())
print(c1.__str__())


# Counting zeros between 1 and N

def count_zeros(n):
    nums = []
    count = 0
    for i in range(n+1):
        nums.append(str(i))
    for j in nums:
        if len(j)>1:
            for num in j:
                if int(num) == 0:
                    count+=1
    return count


#Calculate areas of different shapes
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius**2 * math.pi*2
class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
shape1 = Circle(10)

#Stack operations

class MyStack:
    def __init__(self):
        self.q = deque()
    def add(self):
        self.q.append()
    def poping(self):
        if len(self.q) > 0:
            self.q.pop()
        else:
            raise 'The deque you are poping is empty'
    def is_empty(self):
        if len(self.q) == 0:
            return 'Empty'
        else:
            raise ValueError
    def peek(self):
        if self.q:
            return self.q[-1]
stk = MyStack()

# checking if it is ascii letter
def is_letter(s):
    lett = []
    import string
    letters = string.ascii_letters
    for l in letters:
        lett.append(l)
    if len(s) == 1:
        if s in letters:
            return True
        else:
            return False
    else:
        return False

# Using random method
import random
number = random.randint(1, 100)
while True:
    try:

        guess = int(input('Guess the number between 1 and 100: '))
        if guess < number:
            print('too low')
        elif guess > number:
            print('too high')
        elif guess == number:
            print('Correct guess')

    except ValueError:
        print('Pleaser enter a valid number')

#Hailstone sequence using recursion
def hailstone_sequence(n):
    if n == 1:
        return
    elif n%2 == 0:
        print(int(n/2), end=' ')
        hailstone_sequence(n/2)
    else:
        print(int(n*3+1), end=' ')
        hailstone_sequence(3*n+1)
n = int(input('Enter a number: '))
print(int(n), end=' ')
hailstone_sequence(6)


