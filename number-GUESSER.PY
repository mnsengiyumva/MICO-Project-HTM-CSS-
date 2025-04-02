# import random
# top_of_the_range = input('Type a number: ')

# if top_of_the_range.isdigit():
#     top_of_the_range = int(top_of_the_range)
#     if top_of_the_range <= 0:
#         print('Please type a number greater than zero next time.')
#         quit()
# else:
#     print('Please type a number next time')

# random_number = random.randint(0, top_of_the_range)
# print(random_number)
# guesses = 0
# while True:
#     guesses +=1
#     user_gues = input('What is your guess? ')
  
#     if user_gues.isdigit():
#         user_gues = int(user_gues)
#         if user_gues == random_number:
#             print('You got it right')
#             break
#         else:           
#             print('you Got it wrong')
#     else:
#         print('Please type a number next time')
    
# print('You got it',guesses,'times')


# #Recursion permutation of a word

# def permute(text):
#     if len(text) == 1:
#         return [text]
#     else:
#         perms = []
#         for i in range(len(text)):
#             for perm in permute(text[0:i]+text[i+1:]):
#                 perms.append(text[i]+perm)
#         return perms
# print(permute('ABC'))


# #Recursion Palindome
# def is_palindrome(txt, start, end):
#     if start >= end:
#         return True
#     else:
#         return txt[start] == txt[end] and is_palindrome(txt, start+1, end-1)
# print(is_palindrome('racecar', 0, 5))

#Recursion mazeTraverse
#Static class variables

class MyAttributes:
    name = 'randy'
    count = 0
    def __init__(self, age):
        self.age = age
        MyAttributes.count += 1
a = MyAttributes(25)
MyAttributes.name = 'bob'
a.name = 'alice'
# print(a.name)
# print(a.age)
# print(a.count)
#Property Function

class Alphabet:
    def __init__(self, value):
        self._value  = value
    #Get the values
    def get_value(self):
        print('Getting value')
        return self._value
    #setting value
    def set_value(self, value):
        print('Setting new value to value' + value)
        self._value = value
    #Delete a vealue
    def delete_value(self, value):
        print('Deleting value' + value)
        del self._value
    value = property(get_value, set_value, delete_value, )
x = Alphabet('GeeksforGeeks')
print(x.value)

from collections import deque
class Mystack:
    def __init__(self):
        self.dq = deque()
        self.qu = deque()
    def push(self,value):
        self.dq.append(value)
    def pop(self):
        if self.dq:
            return self.dq.pop()
    def peek(self):
        return self.dq[-1]
    def __len__(self):
        return len(self.dq)
    
    def enqueue(self, val):
        self.qu.append(val)
    def dequeue(self):
        if self.qu:
            return self.qu.popleft(  )

def decimal_binary(num):
    stack = Mystack()
    while num>0:
        remainder = num%2
        stack.push(remainder)
        num = num//2 
    s = ''
    while len(stack)>0:
        s+=str(stack.pop())
    return s
print(decimal_binary(233))



#Fibonacci
def fibonacci(n):
    arr = [0,1]
    for i in range(n):
        arr.append(arr[i]+arr[i+1])
    return arr
print(fibonacci(8))