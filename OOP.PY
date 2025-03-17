# from collections import deque
# class MyStack:
#     def __init__(self, name, grades, position):
#         self.name = name
#         self.grades = grades
#         self.position = position
#         self.stk = deque() 
#     def add_tostk(self):
#         for grade in self.grades:
#             self.stk.append()
#     def popstk(self):
#         if self.stk:
#             self.stk.pop()
#         else:
#             return 'The stack you are trying to pop is an empty stack'
#     def is_empty(self):
#         if len(self.stk) == 0:
#             return 'The stack is empty'
#         else:
#             return f'The length of the stack is {len(self.stk)}'
#     def peek(self):
#         if self.stk:
#             return self.stk[-1]
#         else:
#             return IndexError
#     def __str__(self):
#         return 'The stack you have is the collection of student grade'

import string
import copy
import random
def message(text):
    chars = " " + string.punctuation + string.ascii_letters + string.digits
    characters = []
    for j in chars:
        characters.append(j)
    chars_shuffle = copy.copy(characters)
    cipher = ''
    random.shuffle(chars_shuffle)

    for i in text:
        indx = characters.index(i)
        cipher += chars_shuffle[indx]
    return cipher
message('I sing')

# Reverse a string
from collections import deque
class String:
    def __init__(self, text):
        self.text = text
        self.myStack = []
        for i in self.text:
            self.myStack.append(i)
    def reversing(self):
        reverse = ''
        for i in range(len(self.myStack)):
            reverse += self.myStack.pop()
        return reverse
text1 = String('ABC')
print(text1.reversing())