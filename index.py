# Quiz question

print('Welcome to my computer quiz')
playing = input('Do you want to play? ')
if playing != 'yes'.lower():
    quit()
print("Great let's go")
correct = 0
count = 0
answer = input('What is the capital city of canada')
count +=1
if answer.lower() == 'ottawa':
    correct +=1
    print('Correct, The capital city of canada is Ottawa')
else:
    correct += 0
    print('Incorrect!')
answer = input('What is the name of thre president of Rwanda?')
count +=1
if answer.lower() == 'kagame':
    correct += 1
    print('Correct. The president of Rwanda is kagame')
else:
    correct += 0
    print('Incorrect!')
answer = input('What is the capital city of prince edward island')
count +=1
if answer.lower() == 'charlottetown':
    correct += 1
    print(f'Correct. the capital city of prince edward island is {answer}!')
else:
    correct += 0
    print('Incorrect!')

answer = input('What is the capital city of Rwanda?')
count +=1
if answer.lower() == 'kigali':
    correct += 1
    print(f'Correct. The capital city of Rwanda is {answer}')
else:
    correct += 0
    print('Incorrect')
answer = input('what is the name of largest number boundary')
count+=1g
if answer.lower() == 'infinity':
    correct += 1
    print(f'Correct the largest bound of a number is {answer}')
else:
    correct +=0
    print('Incorrect')
print(f'Quiz complete. Your final core is {correct} out of {count} ')

#Object oriented programing

class Items:
    pay_rate = 0.5
    all = []
    def __init__(self, name, quantity, price):
        #aSSIGN CONDITIONS FOR THE INPUTS (check for the strings, integers and floats values)
        assert quantity >= 1, f" Quantity {quantity} is not greater than 1"
        assert price >= 10, f"Price {price} is not greter than 10"
        self.name = name
        self.quantity = quantity
        self.price = price

        ## Actions
        Items.all.append(self)
    def calculate_cost(self):
        return self.quantity * self.price
    def return_names(self):
        return self.name
    def cost_after_pay_rate(self):
        return self.calculate_cost() *  self.pay_rate
    def __repr__(self):
        return f"Item('{self.name}, {self.quantity}, {self.price}')"

    
class Grocery(Items):
    def __init__(self, name, quantity, price):
        super().__init__(name, quantity, price)


item2 = Grocery('Mangoes', 20, 30)
item1 = Items('Phone', 200, 45)
item3 = Grocery('Rice', 20, 22)

print(Grocery.all)

### Further on the object oriented programing


import csv
class Products:
    ## Class attribute (Can be accessed any where in the class)
    discount = 0.6
    all = []
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        ## actions to be excuted
        Products.all.append(self)
        ## Checking if the conditions are being met before calculating any thing
        assert price >=0, f"Price {self.price} is not greater than or Equal to zero. Please put a correct figure"
        assert quantity>=0,f"Price {self.quantity} is not greater than or Equal to zero. Please put a correct figure"

    def calculate_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.discount
    @classmethod ## Converting into a class method
    def instantiate_from_CSV(cls): #Accessing the data from the file
        with open('myitems.csv', 'r') as f: ## Opening file from csv
            reader = csv.DictReader(f) ## Viewing  the data from the csv file asd a dictionary
            products = list(reader) ## Converting the data int a  list
        for item in products:
            Products(
                name = item.get('name'),
                price = item.get('price'),
                quantity = item.get('quantity'),
            )



    def __repr__(self):
        return f"Product('{self.name}, {self.price}, {self.quantity}')"



# product1 = Products('phone', 200, 30)
# product2 = Products('mouse', 30, 20)
# product3 = Products('computer', 40, 40)
Products.instantiate_from_CSV()
print(Products.all)
