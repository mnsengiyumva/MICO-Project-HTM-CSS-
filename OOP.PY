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

#Palindrome string

def palindrome(text):
    stack = deque()
    palind = ''
    for letter in text:
        stack.appendleft(letter)
    for l in range(len(stack)):
        palind += stack.popleft()
    if palind.lower() == text.lower():
        return 'Palindrome'
    else:
        return 'Not a Palindrome'
# print(palindrome('racecaRy'))

# Binary search

def binary_search(lst, key, lo, hi):
    if hi>=lo:
        mid = (hi+lo)//2
        if lst[mid] == key:
            return True
        elif key<lst[mid]:
            return binary_search(lst, key, lo, mid-1)
        else:
            return binary_search(lst, key, mid+1, hi)
print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 0, 9))

# Linear search
def linear_search(c, key):
    for i in c:
        if i == key:
            return True
        else:
            return False
print(linear_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6))
print(linear_search({'Mico': 10, 'Kevin':30}, 'Kevin'))

class PhoneRecord:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __str__(self):
        return "str" + self.name + ":" + str(self.number)
    def __repr__(self):
        return "repr" + self.name + ":" + str(self.number)
    def __eq__(self, other):
        return self.name == other.name and self.number == other.number
    def __lt__(self, other):
        return self.name < self.other or self.name == other.name and self.number < other.number
    
phone_book = [PhoneRecord('Norm', 123), PhoneRecord('Min', 535), PhoneRecord('Bii', 767)]

print(linear_search(phone_book, PhoneRecord('Norm', 123)))
print(phone_book)
print(phone_book[0])

## LIST COMPLEHENSION CAN DO MATCHES

matches = [record for record in phone_book if record.name == 'Norm']
print(matches)

import bisect
def my_key(record):
    return record.name
phone_book.sort(key = my_key)
print(phone_book)
nums = range(100)
idx = bisect.bisect_left(nums, 50)
print(idx)  

#sorting by energy
players = ['sam', 'bill', 'tom']
energy = [80,70,100]
position = [3,1,2]
def sort_players(players, energy, position):
    zip_lst = list(zip(players, energy, position))
    zip_lst.sort(key = lambda x:x[1], reverse=True)
    return [list(x) for x in zip(*zip_lst)]
p,n,e = sort_players(players,energy,position)
print(p,n,e)


# Given an x and y find the smallest and greatest numbers above and below a given n that are divisible by both x and y
def greatest(x, y, n):
    result = []
    for i in range(n):
        if i%x == 0 and i%y == 0:
            result.append(i)
    if len(result)>0:
        result.sort()
        return result[-1]
    else:
        return 0
def smallest(x,y,n):
    result2 = []
    for i in range(n+1,x*y*n+1):
        if i%x ==0  and i%y == 0:
            result2.append(i)
    if len(result2) >0:
        result2.sort()
        return result2[0]
    else:
        return 0
#Special sorting

from collections import deque
def solve(arr):
    dq = deque()
    result = deque()
    lst = sorted(arr)
    final = []
    for i in lst:
        dq.append(i)
    while len(dq)>0:
        result.append(dq.pop())
        if dq:
            result.append(dq.popleft())
    for i in result:
        final.append(i)
    
    return final

#counting douplicates
def duplicate_count(text):
    txt = text.lower()
    result = []
    for i in txt:
        if txt.count(i)>1:
            result.append(i)
    return len(result)
print(duplicate_count('abc'))

## String reduction

def solve(a,b):
    if len(b)>len(a):
        return 0
    else:
        for i in a:
            for j in b:
                if b.count(j)>a.count(i):
                    return 0
                elif b.count(j)<=a.count(i) and i==j and j in a:
                    return len(a)-len(b)
                elif b.count(j)==a.count(i)==1 and i==j and j in a:
                    return len(a)-len(b)
#testCase: solve(abcd,cd) ===> 2


#Reverse with stack
from collections import deque
class Stack:
    def __init__(self):
        self.dq = deque()
        '''Represente a queue'''
    def push(self, x):
        self.dq.append(x)
    def pop(self):
        if self.dq:
            return self.dq.pop()
    def peek(self):
        if self.dq:
            return self.dq[-1]
    def isEmpty(self):
        return len(self.dq) == 0
    def __len__(self):
        return len(self.dq)
def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reverse = ''
    while len(stack)>0:
        reverse+= stack.pop()
    return reverse
print(reverse_string('ABC'))