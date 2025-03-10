from collections import deque
class MyStack:
    def __init__(self, name, grades, position):
        self.name = name
        self.grades = grades
        self.position = position
        self.stk = deque() 
    def add_tostk(self):
        for grade in self.grades:
            self.stk.append()
    def popstk(self):
        if self.stk:
            self.stk.pop()
        else:
            return 'The stack you are trying to pop is an empty stack'
    def is_empty(self):
        if len(self.stk) == 0:
            return 'The stack is empty'
        else:
            return f'The length of the stack is {len(self.stk)}'
    def peek(self):
        if self.stk:
            return self.stk[-1]
        else:
            return IndexError
    def __str__(self):
        return 'The stack you have is the collection of student grade'
