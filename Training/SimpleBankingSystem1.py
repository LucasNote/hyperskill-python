"""
About
Everything goes digital these days, and so does money. Today, most people have credit cards,
which save us time, energy and nerves. From not having to carry a wallet full of cash to consumer protection,
cards make our lives easier in many ways. In this project, you will develop a simple banking system with database.

Learning outcomes
In this project, you will find out how the banking system works and learn about SQL.
We'll also see how Luhn algorithm can help us avoid mistakes when entering the card number.
As an overall result, you'll get new experience in Python.

Description: https://hyperskill.org/projects/109/stages/591/preview

"""

# 4/1: Card anatomy
# Theory: String formatting
print(11 / 3)  # 3.6666666666666665
print('%.3f' % (11 / 3))  # 3.667
print('%.2f' % (11 / 3))  # 3.67

# 1. The str. format() method
# The operation of the method is already described in its name: in the string part,
# we introduce curly braces as placeholders for variables enlisted in the format part:
print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
print('{1} in the {0} by Frank Sinatra'.format('Strangers', 'Night'))

# We can also use keywords to make such strings more readable. Don't forget that you can easily break the lines!
print('The {film} at {theatre} was {adjective}!'.format(film='Lord of the Rings',
                                                        adjective='incredible',
                                                        theatre='BFI IMAX'))

# Also, you can combine both positional and keyword arguments:
print('The {0} was {adjective}!'.format('Lord of the Rings', adjective='incredible'))
# The Lord of the Rings was incredible!

# Keep tabs on the order of your arguments, though:
# print('The {0} was {adjective}!'.format(adjective='incredible', 'Lord of the Rings'))
# SyntaxError: positional argument follows keyword argument

"""
Formatted string literals
Formatted string literals (or, simply, f-strings) are used to embed the values of expressions  
inside string literals. This way is supposed to be the easiest one: you only need to put f before the string 
and put the variables you want to embed into the string in curly braces. 
They are also the newest feature among all string formatting methods in Python.
"""
student_name = 'Elizabeth II'
title = 'Queen of the United Kingdom and the other Commonwealth realms'
reign = 'the longest-lived and longest-reigning British monarch'
f'{student_name}, the {title}, is {reign}.'
print(f'{student_name}, the {title}, is {reign}.')

hundred_percent_number = 1823
needed_percent = 16
needed_percent_number = hundred_percent_number * needed_percent / 100

print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
# 16% from 1823 is 291.68

print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
# Rounding 291.68 to 1 decimal place is 291.7


# 6.1.3.1. Format Specification Mini-Language¶
# https://docs.python.org/3.6/library/string.html#format-specification-mini-language

# String formatting > Divide
'%.5f' % (100 / 6)
'{1} divided by {0} equals {2}'.format(6, 100, 100 / 6)
'{} divided by {} equals {:.5f}'.format(100, 6, 100 / 6)
'{dividend} / {divisor} = {quotient}'.format(quotient=100 / 6, divisor=6, dividend=100)

# String formatting > Correct format
# print('%.3f' % (11/3))  # 3.667
"%.4f".format(3.14159265358979)
"{1} {1} {1}".format(1, 2, 3)
# "{1} is a {kind}".format(kind="fruit", "grapefruit")  # SyntaxError: positional argument follows keyword argument
"{city} is the capital of {country}".format(country="Portugal",
                                            city="Lisbon")

# String formatting > Write a number:
print('%.2f' % (21 / 4))

# String formatting > Film
movie = input()
director = input()
year = input()
print(f'{movie} (dir. {director}) came out in {year}')
print("{0} (dir. {1}) came out in {2}".format(movie, director, year))
print("{movie} (dir. {director}) came out in {year}".format(movie=movie
                                                            , director=director
                                                            , year=year))

# String formatting > Tax brackets
"""
0 — 15,527: 0% tax
15,528 — 42,707: 15% tax
42,708 — 132,406: 25% tax
132,407 and more: 28% tax
"""

income = int(input())
percent = 0
calculated_tax = 0

if income > 132406:
    percent = 28
elif income > 42707:
    percent = 25
elif income > 15527:
    percent = 15

# calculated_tax = int(round(income * percent / 100))
calculated_tax = round(income * percent / 100)

print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
# format = f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!"
# print(format)

# Sample 1
income = int(input())
if income <= 15527:
    tax = 0
elif 1527 < income <= 42707:
    tax = 15
elif 42707 < income <= 132406:
    tax = 25
elif income > 132406:
    tax = 28
calculated_tax = (income * tax / 100)
print(f'The tax for {income} is {tax}%. That is {calculated_tax:.0f} dollars!')

# Sample 2
tex_brackets = dict({15527: 0, 42707: 0.15, 132406: 0.25})
income = int(input())

for u in tex_brackets:
    if income <= u:
        percent = tex_brackets[u]
        break
else:
    percent = 0.28

print(f"The tax for {income} is {percent:.0%}. That is {round(income * percent)} dollars!")

# [Topic] Theory: Dictionary
# 1. Dictionary creation
birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
prices = {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
empty_dict = {}

print(type(birds))
print(type(prices))
print(type(empty_dict))

another_empty_dict = dict()  # using the dict constructor
print(type(another_empty_dict))  # <class 'dict'>

# note that the future dictionary keys are listed without quotes
prices_with_constr = dict({'espresso': 5.0}, americano=8.0, latte=10, pastry='various prices')
print(prices_with_constr)  # {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}

prices_with_constr2 = dict(prices)
print(prices_with_constr2)  # {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
print(type(prices_with_constr2))  # <class 'dict'>

# d1 = dict(888=8.0)  # SyntaxError: keyword can't be an expression
# d2 = dict("americano"=8.0)  # SyntaxError: keyword can't be an expression
# d3 = dict(["americano", "filter"]=8.0)  # SyntaxError: keyword can't be an expression
# d4 = dict(the best americano=8.0) # SyntaxError: invalid syntax
#
# d5 = dict(1: 'value')  # SyntaxError: invalid syntax
d6 = dict({'1': 'value'})

# a nested dictionary example
my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}

# another nested dictionary example
# note that keys of the outer dictionary are numbers
digits = {1: {'Word': 'one', 'Roman': 'I'},
          2: {'Word': 'two', 'Roman': 'II'},
          3: {'Word': 'three', 'Roman': 'III'},
          4: {'Word': 'four', 'Roman': 'IV'},
          5: {'Word': 'five', 'Roman': 'V'}}

# 2. Accessing the items
my_pet = {}

# add 3 keys and their values into the dictionary
my_pet['name'] = 'Dolly'
my_pet['animal'] = 'dog'
my_pet['breed'] = 'collie'

print(my_pet)  # {'name': 'Dolly', 'animal': 'dog', 'breed': 'collie'}

# get information from the dictionary about an added item
print(my_pet['name'])  # Dolly

# our nested dictionary once again:
my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}

print(my_pets['cat'])  # {'name': 'Fluffy', 'breed': 'maine coon'}

print(my_pets['cat']['breed'])  # maine coon

# 3. Choosing the keys
trilogy = {'IV': 'Star Wars', 'V': 'The Empire Strikes Back', 'VI': 'Return of the Jedi'}
print(trilogy['IV'])  # Star Wars

trilogy['IV'] = 'A New Hope'
print(trilogy['IV'])  # A New Hope

# In Python 3.7 and up, dictionaries do maintain the insertion order for values they store,
# but in previous versions it is not necessarily so:
alphabet = {}
alphabet['alpha'] = 1
alphabet['beta'] = 2

print(alphabet)  # Python 3.8 output: {'alpha': 1, 'beta': 2}

# Dictionary > Grocery list
shopping_list = {'bananas': 5, 'oranges': 3, 'yogurt': 2, 'chicken breasts': 3, 'olive oil': 1}

# bananas['shopping_list'] = 10  # NameError: name 'bananas' is not defined
# shopping_list[bananas] = 10  # NameError: name 'bananas' is not defined
shopping_list['bananas'] = 10
# shopping_list.bananas = 11  # AttributeError: 'dict' object has no attribute 'bananas'

# Any datatype can be a value in a dictionary

# Dictionary > Let's count
sample = {}
sample['a'] = 3
sample['b'] = 5
sample['c'] = -2
print(sample['a'] + sample['b'] + sample['c'])

# Dictionary > Create
# Let's say you asked your friends to name their favorite flowers: now you know that ' \
#    'Alex likes 'field flowers', Kate prefers 'daffodil', Eva adores 'artichoke flower', and Daniel loves 'tulip'.
# Create a dict with the names as keys and flowers as values and print it.
favorite_flowers = {'Alex': 'field flowers', 'Kate': 'daffodil', 'Eva': 'artichoke flower', 'Daniel': 'tulip'}
print(favorite_flowers)

# Dictionary > Nested
children = {'Emily': 'artist', 'Adam': 'astronaut', 'Nancy': 'programmer'}

my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
           'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}

children = {'Emily': {'profession': 'artist', 'age': 5},
            'Adam': {'profession': 'astronaut', 'age': 9},
            'Nancy': {'profession': 'programmer', 'age': 14}}

# Sample 1
age = {'Emily': 5, 'Adam': 9, 'Nancy': 14}
for student_name in children:
    children[student_name] = {'profession': children[student_name], 'age': age[student_name]}

# Sample 2
children = {'Emily': 'artist', 'Adam': 'astronaut', 'Nancy': 'programmer'}
ages = {'Emily': 5, 'Adam': 9, 'Nancy': 14}

for key, _value in children.items():
    children[key] = {"profession": children.get(key), "age": ages.get(key)}

# Theory: Invoking a function
print("Hello, world!")
print()
print("Bye,", "then!")

number = "111"
# finding the length of an object
print(len(number))  # 3

# converting types
integer = int(number)
float_number = float(number)
print(str(float_number))  # "111.0"

# adding and rounding numbers
my_sum = sum((integer, float_number))

print(my_sum)  # 222.0
print(round(my_sum))  # 222

# finding the minimum and the maximum
print(min(integer, float_number))  # 111
print(type(max(integer, float_number, my_sum)))  # <class 'float'>

help(min)

# Invoking a function > String length
string = input()
print(len(string))

# Invoking a function > Hello, world!
student_name = input()
print(f"Hello, world! Hello, {student_name}")

# Invoking a function > Longest word
word1 = input()
word2 = input()

# How many letters does the longest word contain?
longest = max(len(word1), len(word2))
print(longest)

# Theory: Declaring a function
"""
def function_name(parameter1, parameter2, ...):
    # function's body
    ...
    return "return value"
"""


# Function definition
def multiply(x, y):
    return x * y


# Function calls
a = multiply(3, 5)  # 15
b = multiply(a, 10)  # 150


# no arguments
def welcome():
    print("Hello, people!")


# This function does nothing (yet)
def lazy_func(param):
    pass


# 1. Parameters vs arguments
def send_postcard(address, message):
    print("Sending a postcard to", address)
    print("With the message:", message)


send_postcard("Hilton, 97", "Hello, bro!")
# Sending a postcard to Hilton, 97
# With the message: Hello, bro!

send_postcard("Piccadilly, London", "Hi, London!")


# Sending a postcard to Piccadilly, London
# With the message: Hi, London!

# send_postcard("Big Ben, London")  # TypeError: send_postcard() missing 1 required positional argument: 'message'

# 2. Execution and return
def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


# Convert the boiling point of water
water_bp = celsius_to_fahrenheit(100)
print(water_bp)  # 212.0

chant = print("We Will Rock You")
print(chant)

# 3. Conclusion
"""
Thus, we've learned the syntax for declaring functions. Now you also know that:

Parameters of a function are simply aliases, or placeholders for values that you will pass to them. 
    - Parameters are re-initialized every time you call the function. Inside the function, 
    you have access to these values, which means you can perform calculations on them.
    - A function can simply perform an action without returning anything or return a specific result. 
    If your function doesn't return anything, assigning its result to a variable or printing it will give you None.

Declaring your own functions makes your code more structured and reusable. 
Whenever you use the same piece of code more than once, try to create a function of it!
"""


# Declaring a function > Lucky number
def three():
    print(3)
    return 3
    print(3)


three()
print(3)


# Declaring a function > The Sum of 2
# 1
def get_sum(a, b):
    return int(a) + int(b)


a, b = input().split()
print(get_sum(a, b))

# 2
a = input()
b = input()
print(get_sum(a, b))

# 3
a, b = input().split()
print(get_sum(int(a), int(b)))


# 4
def get_sum(a, b):
    # return a + b
    return sum([a, b])


a, b = map(int, input().split())
print(get_sum(a, b))


def get_sum(a: int, b: int) -> int:
    return a + b


# Declaring a function > Fahrenheit
def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 3)


# Declaring a function > Fahrenheit
water_bp = fahrenheit_to_celsius(451)
print(water_bp)


# Declaring a function > Make the function work
def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x

    if remainder > 0:
        return x + (5 - remainder)
    # print(f"remainder: {remainder}")

    return "I don't know :("


# Sample 1
def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    return x + (5 - remainder)


closest_higher_mod_5(40)  # Output: 40
closest_higher_mod_5(43)  # Output: 43


def closest_higher_mod_5(x):
    remainder = x % 5

    print(f"x: {x}, remainder: {remainder}")
    if remainder == 0:
        return x

    return closest_higher_mod_5(x + 1)


print(closest_higher_mod_5(40))
print(closest_higher_mod_5(43))

# Scopes > Cities
user_city = "Istanbul"


def change_city(new_user_city):
    global user_city
    user_city = new_user_city


change_city("Paris")
print(user_city)

# Else statement > The Maximum
a, b = 9, 9
if a > b:
    print('a', a)
else:
    print('b', b)

# For loop > True or False
for i in range(1, 5): print(i)

for _ in range(10):
    print("Hello world")

# The for loop only works with iterable objects.
# If the counter variable is not used in a loop, its name can be replaced with an underscore symbol.


# Loop control statements > Commenting out
student_name = 'John'
age = 10
# name = 'asdfghjkl'
# age = -999
print(student_name + ' ' + str(age))

import random  # 1

# 2
n_guesses = 0  # 3
while n_guesses < 5:  # 4
    number = random.randint(1, 5)  # 5
    print('number', number)
    guess = int(input())  # 6
    if guess == number:  # 7
        print('Yes!')  # 8
    else:  # 9
        print('No!')  # 10
    # n_guesses += 1                 # 11

# Theory: Load module
# 1. Module basics

# 2. Module loading
"""
import super_module
super_module.super_function()  # calling a function defined in super_module
print(super_module.super_variable)  # accessing a variable defined in super_module

from super_module import super_function
super_function()  # super_function is now available directly at the current module
super_module.super_function()  # note, that in this case name super_module is not imported, 
                               # so this line leads to an error
"""

"""
In order to be available for import, super_module.py should be located in the same directory 
as the file you are trying to import it from. At first, Python importing system looks for 
a module in the current directory, then it checks the built-in modules, 
and if nothing is found an error will be raised. After importing, 
the module becomes available under its name and you can access functions 
and variables defined in it using the dot notation.

In case you have to use several import statements, pay attention to their order:
1. standard library imports
2. third party dependency imports
3. local application imports

Having your imports grouped, you may put a blank line between import sections. 
Also, some guidelines, including ours, recommend sorting imports alphabetically.
"""

# 3. Built-in modules
import math

print(math.factorial(5))  # prints the value of 5!
print(math.log(10))  # prints the natural logarithm of 10
print(math.pi)  # math also contains several constants
print(math.e)

from string import digits

print(digits)  # prints all the digit symbols

from random import choice

print(choice(['red', 'green', 'yellow']))  # print a random item from the list

# Load module > Copysign function
# place `import` statement at top of the program
import math

# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))  # -68.83573394536573 -66.80342071491599
print(math.copysign(x, y))  # -68.83573394536573

# Sample 1
from math import copysign

x, y = map(float, input().split(' '))
print(copysign(x, y))

# Load module > Capitalize all words
# place `import` statement at top of the program
from string import capwords

# don't modify this code or the variable may not be available
input_string = input()

# use capwords() here
print(capwords(input_string))

# Load module > Not exactly random
# place `import` statement at top of the program
import random

# don't modify this code or variable `n` may not be available
n = int(input())

# put your code here
random.seed(n)  # 36
print(random.randint(-100, 100))  # -16

# Theory: Random module
# 1. Random method: first steps, import the module
import random

# random.random() will provide us with a pseudo-random number from 0 to 1
print(random.random())  # 0.6567877181696629

# We can also control the pseudo-random behavior by specifying the seed manually,
# i.e. configure the new sequence of pseudo-random numbers
# using random.seed(x) function. You can set your own number
# or omit the optional argument x and consequently current system time would be used by default.
random.seed()
print(random.random())  # 0.4542980882161418

# The seed controls the behavior of pseudo-random in Python
# and can be used with any other function of the random module.

random.seed(5)
print(random.random())  # 0.6229016948897019

random.seed(20)
print(random.random())  # 0.9056396761745207

# 2. Random basic functions
# random.uniform(a, b) – returns a pseudo-random float number in the range between a and b:
print(random.uniform(3, 100))  # 69.56665323159015

# random.randint(a, b) – returns a pseudo-random integer number in the range between a and b:
print(random.randint(35, 53))  # 39

# random.choice(seq)– returns pseudo-random element from non-empty sequences:
print(random.choice('Voldemort'))  # e

# random.randrange(a, b, c) – returns a pseudo-random number from a range between a and b with a step c.
print(random.randrange(3, 100, 5))  # 18
print(random.randrange(1, 5))  # 3
print(random.randrange(100))  # 44

# random.shuffle(seq) – shuffles a sequence. Attention: it doesn't work with immutable datatypes!
tiny_list = ['a', 'apple', 'b', 'banana', 'c', 'cat']
random.shuffle(tiny_list)
print(tiny_list)  # ['b', 'c', 'cat', 'banana', 'a', 'apple']

# random.sample(population, k)– returns a pseudo-random k length list from a population sequence.
# This function is used for random sampling without replacement:
print(random.sample(range(100), 3))  # [13, 16, 40]

# random.gammavariate(alpha, beta)
# random.gauss(mu, sigma)


"""
The pseudo-random generators of the random module should NOT be used for security purposes. 
If you are intending to work with passwords, security tokens and other sensitive data, 
check out the secrets module. It's considered more reliable since it generates secure random numbers.
"""

# Random module > The dice game
import random

# this line is needed for us to check the results, don't modify it please
random.seed(int(input()))

# use a function from the random module in the next line
print(random.randint(1, 6))

# sample
print(random.randrange(1, 7))

# Random module > Voldemort
import random

# work with this variable
n = int(input())

random.seed(n)
print(random.choice('Voldemort'))

# sample 1
n = random.randrange(len('Voldemort'))
print(list('Voldemort')[n])

# Random module > Beta distribution
random.seed(3)
print(random.betavariate(0.9, 0.1))  # 0.9997528058485836

# sample
print(random.betavariate(alpha=0.9, beta=0.1))  # 0.9997528058485836


# Theory: Class
# 1. Declaring classes

# class syntax
class MyClass:
    var = ...  # some variable

    def do_smt(self):
        # some method
        pass


# good class name
class MyClass:
    ...


# not so good class name:
class My_class:
    ...


# 2. Class attribute

# Book class
class Book:
    material = "paper"
    cover = "paperback"
    all_books = []


Book.material  # "paper"
Book.cover  # "paperback"
Book.all_books  # []

# 3. Class instance
# Book instance
my_book = Book()

print(my_book.material)
print(my_book.cover)
print(my_book.all_books)


# Class > Team time
class Tea:
    life_form = "plant"
    purpose = "beverage"


my_tea = Tea()


# my_tea = Tea("plant")  # TypeError: Tea() takes no arguments


class Tree:
    trunk = True  # Class attribute
    branches = True  # Class attribute

    def __init__(self, name, height):
        self.name = name  # Instance attribute
        self.height = height  # Instance attribute


my_tree = Tree('name', 5)
print(my_tree.trunk)
print(my_tree.branches)
print(my_tree.name)
print(my_tree.height)


# Class > Who is who
class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


angel = Angel()
print(angel.color)
print(angel.feature)
print(angel.home)

demon = Demon()
print(demon.color)
print(demon.feature)
print(demon.home)


# Class > The Creator
class Elf:
    height = 1.8
    weapon = "longbow"
    emotional_maturity = 125


# class > Let's rock
class RockBand:
    genre = 'rock'
    key_instruments = ["electric guitar", "drums"]
    n_members = 4


my_rockband = RockBand()
my_rockband.genre = 'rock'
my_rockband.key_instruments = ["electric guitar", "drums"]
my_rockband.n_members = 4

print(my_rockband.genre)
print(my_rockband.n_members)
print(my_rockband.key_instruments)

# sample
print(my_rockband.genre, my_rockband.n_members, my_rockband.key_instruments, sep="\n")


# Theory: Class instances
# 1. def __init__()
class River:
    # list of all rivers
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # add current river to the list of all rivers
        River.all_rivers.append(self)


volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)

# print all river names
for river in River.all_rivers:
    print(river.student_name)


# Output:
# Volga
# Seine
# Nile


# 2. self
class River:
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)

    def get_info(self):
        print("The length of the {0} is {1} km".format(self.name, self.length))


volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)

volga.get_info()
seine.get_info()
nile.get_info()

"""
Note that when we actually call an object's method we don't write the self argument 
in the brackets. The self parameter (that represents a particular instance of the class) 
is passed to the instance method implicitly when it is called. 
So there are actually two ways to call an instance method: self.method() 
or class.method(self). In our example it would look like this:

# self.method()
volga.get_info()
# The length of the Volga is 3530 km

# class.method(self)
River.get_info(volga)
# The length of the Volga is 3530 km
"""


# 3. Instance attributes
# Instance attributes are defined within methods and they store instance-specific information.

# Instance attributes, naturally, are used to distinguish objects: their values are different for different instances.

# So when deciding which attributes to choose in your program, you should first decide
# whether you want it to store values unique to each object of the class or,
# on the contrary, the ones shared by all instances.

# Class instances > Movie night
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year


# objects of the class Movie
titanic = Movie("Titanic", "James Cameron", 1997)
star_wars = Movie("Star Wars", "George Lucas", 1977)
fight_club = Movie("Fight Club", "David Fincher", 1999)


# Class instances > Shopping
class Store:
    def __init__(self, name, category):
        self.name = name
        self.category = category


shop = Store("GAP", "clothes")
print(shop.name, shop.category)


# Class instances > Students
class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

        # calculate the student_id here
        self.student_id = self.name[0] + last_name + str(birth_year)


student_name = input()
student_last_name = input()
student_birth_year = int(input())

DSmith = Student(student_name, student_last_name, student_birth_year)
print(DSmith.student_id)


# Theory: Methods
# If attributes define the data that the objects of a particular class have, the methods define their behavior.

# 1. Method syntax
# basic method syntax
class MyClass:
    # the constructor
    def __init__(self, arg1):
        self.att = arg1

    # custom method
    def do_smt(self):
        # does something
        pass


"""
The first parameter of the method should always be self. You may remember that self represents the particular instance of the class. 
When it comes to instance methods, the first parameter that is passed to the method is the instance that called it.
"""
my_object = MyClass('some_value')
# calling the instance method
my_object.do_smt()
# my_object does something

MyClass.do_smt(my_object)
# my_object does the same thing

# These examples clearly illustrate why self has to be the first argument of the instance methods.
# If you want your method to have other parameters, just write them after the self keyword!


# 2. Methods vs functions
# "a method is a function that 'belongs to' an object."

# class and its methods
class Ship:
    def __init__(self, name, capacity, cargo):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self):
        print("{} has sailed!".format(self.name))

    def convert_cargo(self):
        return self.cargo * 1000


# function
def sail_function(name):
    print("{} has sailed!".format(name))

# call the method sail of the class Ship and the function sail_function.
# creating an instance of the class Ship
# and calling the method sail
black_pearl = Ship("Black Pearl", 800)
black_pearl.sail()
# prints "Black Pearl has sailed!"


# calling the function sail_function
sail_function(black_pearl.name)
# also prints "Black Pearl has sailed!"


# 3. Return
black_pearl = Ship("Black Pearl", 800, 10)
print(black_pearl.convert_cargo())  # 0

# Methods > Open door policy
class Door:
    def open_door(self):
        print("Door open")

door = Door()
door.open_door()
Door.open_door(door)


# Methods > Drive
class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print("vroom vroom")

my_car = Car("Volkswagen")
my_car.drive()
Car.drive(my_car)


# Methods > Point
# Create a class Point that will represent a point in space. Its constructor needs two parameters xx and yy,
# the coordinates of a point on the plane. The class should have a method dist that takes another instance of Point
# and returns the Euclidean distance between these two points. For Point(x1, y1) and Point(x2, y2),
# calculate the distance according to the formula:
# square root can be expressed as ** 0.5

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p1):
        first = (self.x - p1.x) ** 2
        second = (self.y - p1.y) ** 2
        result = (first + second) ** 0.5
        return result


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        print(self.y, other.y)
        print(self.y - other.y)
        print((self.y - other.y) ** 2)
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        return sqrt(pow(self.x - p2.x, 2) + pow(self.y - p2.y, 2))


p1 = Point(1.5, 1)
p2 = Point(1.5, 2)

print(p1.dist(p2))  # 1.0

# (-1) ** 2  # 1
# -1 ** 2   # -1


# changed from Windows 2021-05-16
# git commit -m "Simple Banking System #1 20210516 8 (Win)"
# git commit -m "Simple Banking System #1 20210516 9 (Win)"
