###############################
#### VARIABLES AND STRINGS ####
###############################
# Think of variables as boxes that we use to store things and retrieve them
# later when needed. In Python variables are used to store values.
# A string is a series of characters, sorounded by single or double quotes.

# Hello World Program
print("Hello, Python World!")

# Hello World Program with a Variable
message = 'Hello, Python World!'
print(message)

# String concatenation
first_name = "Robert"
last_name = 'Mutukudzi'

musician = first_name + ' ' + last_name
print(musician)

###############
#### LISTS ####
###############
# A list is a Python built-in data structure that we use when we want to store
# values as a series of items. And you can access the items based on their
# index or within a loop.

# Defining a list
capitals = ["maputo", "cape town", "luanda", "dodoma"]
print(capitals)

# Accessing the first item in the list
capitals = ["maputo", "cape town", "luanda", "dodoma"]

mozambique_capital = capitals[0]
print(mozambique_capital)

# Accessing the last item in the list
capitals = ["maputo", "cape town", "luanda", "dodoma"]

tanzania_capital = capitals[-1]
print(tanzania_capital)

# Iterating or looping over a list
capitals = ["maputo", "cape town", "luanda", "dodoma"]

for capital in capitals:
	print(capital.title())

# Adding new items to a list
capitals = []

capitals.append('maputo')
capitals.append("cape town")
capitals.append('luanda')
capitals.append("dodoma")

print(capitals)

# A list of heights: 'use case'
heights = []

for value in range(1, 11):
	heights.append(value * 10 / 5)

print(heights)

# List comprehension
heights = [value * 10 / 5 for value in range(1, 11)]
print(heights)

# List slices
capitals = ["maputo", "cape town", "luanda", "dodoma"]

first_three = capitals[:3]
print("First three items:", first_three)

last_two = capitals[-2:]
print("Last two items:", last_two)

# List copy
capitals = ["maputo", "cape town", "luanda", "dodoma"]

copy_of_capitals = capitals[:]
print(copy_of_capitals)

################
#### TUPLES ####
################
# A tuple is almost the same as a list data structure, but the items on it
# cannot be modified. A tuple works just like lists.

# Making a tuple
dog = ("shepherd", 4, "specialist on eating", 13.4)
print(dog)

# Get the first and last item in a tuple
dog = ("shepherd", 4, "specialist on eating", 13.4)

dog_name = dog[0] 	    # first item
dog_weight = dog[-1]    # last item

print(dog_name)
print(dog_weight)

# Iterating or looping over a tuple
dog = ("shepherd", 4, "specialist on eating", 13.4)

for attribute in dog:
	print(attribute)

#######################
#### IF STATEMENTS ####
#######################
# If statements are control statements used to execute specific parts of our
# code based on a particular condition.

# Conditional tests
	# Equals						x == y
	# Not equal						x != y
	# Greater than					x > y
	# Greater than or equal to		x >= y
	# Less than						x < y
	# Less than or equal to			x <= y

# Conditional tests
provinces = ["maputo", "gaza", "inhambane", "manica"]

if "maputo" in provinces:
	print("Maputo is a province of Mozambique")

if "nelspruit" not in provinces:
	print("Nelspruit is a city in South Africa")

# Assigning boolean values (True or False)
is_enabled = True

if is_enabled:
    print('Mario is enabled to be a programmer')

cant_change = False
if not cant_change:
    print('Mario can change to other tech field')

# A simple if test
is_mozambican = True

if is_mozambican:
    print('Mario is Mozambican')

# If-elif-else statements
is_mozambican = False

if not is_mozambican:
	print("Sharon is not a Mozambican name")
elif is_mozambican:
	print("Julia is a Mozambican name")
else:
	print("That is not a name")

######################
#### DICTIONARIES ####
######################
# Dictionary is a Python built-in data structure used when we want connections
# between two pieces of information. Each item in the dictionary represent a
# key-value pair.

# A simple dictionary
cities = {'mozambique': 'maputo', 'angola': 'luanda', 'tanzania': 'dodoma'}
print(cities)

# Accessing a value
cities = {'mozambique': 'maputo', 'angola': 'luanda', 'tanzania': 'dodoma'}

mozambique_capital = cities['mozambique']
print(mozambique_capital) # print 'maputo'

tanzania_capital = cities['tanzania']
print(tanzania_capital) # print 'dodoma'

# Adding new key-value pairs
cities = {'mozambique': 'maputo'}

cities['south africa'] = 'cape town'
cities['zimbabwe'] = 'harare'

print(cities)

# Iterating or looping over all key-value pairs
demography = {'mozambique': 30, 'angola': 32, 'south africa': 59}

for country, population in demography.items():
	print(country, ":", population)

# Iterating or looping over all keys
demography = {'mozambique': 30, 'angola': 32, 'south africa': 59}

for country in demography.keys():
	print(country)

# Iterating or looping over all values
demography = {'mozambique': 30, 'angola': 32, 'south africa': 59}

for population in demography.values():
	print("Population: " + str(population))

####################
#### USER INPUT ####
####################
# Python programs can laverage a built-in function to get input on the fly
# from the user. All input is stored as a string.

# Prompting for a value
province = input("What's your province? ")
print("Your province is", province)

# Prompting for numerical input
street_number = input("What is your street number address? ")
street_number = int(street_number) # WARNING: type conversion may not succeed
print(street_number, type(street_number))

country_population = input("What's your country population? ")
country_population = float(country_population) # WARNING: type conversion may not succeed
print(country_population, type(country_population))

#####################
#### WHILE LOOPS ####
#####################
# A while loop is one of the Python control statements used to execute a block
# of code as long as a certain condition is met.

# A simple while loop
index = 1
while index <= 5:
	print(index)
	index += 1

# Iterating or looping over a list
capitals = ["maputo", "cape town", "luanda", "dodoma"]
while capitals:
    print(capitals.pop())

# Iterating or looping over a dictionary
demography = {'mozambique': 30, 'angola': 32, 'south africa': 59}
while demography:
    print(demography.popitem())

###################
#### FUNCTIONS ####
###################
# Functions are named blocks of code, designed to do one specific job. 
# Information passed to a function is called an argument, and information
# received by a function is called a parameter.

# Function definition and call
def hello():
    """Prints a hello world message."""
    print("Hello, Python World!")

hello()

# Function parameters and arguments
def hello(message):
    """Prints a user provided message."""
    print(message)

hello("Hello, Python World!")

# Function default parameters
def hello(message="Hello, Python World!"):
    """Prints a user provided message."""
    print(message)

hello()
hello("Hello, Edondza Academy")

# Function returning a value
def add(x, y):
    """Add two numbers and return the sum."""
    return x + y

sum = add(3, 5)
print(sum)

#################
#### CLASSES ####
#################
# A class is a user defined type provided to represent a real world concept.
# When an object of a class is created, information is stored in attributes
# and the behavior is defined by the methods (functions that belong to the
# class).
# A child class is said to inherit all the members of its parent class.

# Creating a Person class
class Person:
    """Represent a Person"""

    def __init__(self, name):
        """Initialize person attributes."""
        self.name = name
        
    def greet(self):
        """Greet a person."""
        print(self.name + " is saying Hello.")

luan = Person("Luan")

print(luan.name + " is Person just like me.")
luan.greet()

# Inheritance
class Programmer(Person):
    """Represent a machine that turn coffee into code"""

    def __init__(self, name, fav_language):
        """Initialize programmer attributes."""
        super().__init__(name)
        self.fav_language = fav_language
    
    def fav_programming_language(self):
        """Tells the favorite programming language"""
        print("I love " + self.fav_language)

shaun = Programmer('Shaun', 'TypeScript')

print(shaun.name + " is a programmer.")
shaun.greet()
shaun.fav_programming_language()

############################
#### WORKING WITH FILES ####
############################
# You can make your programs read, write or append to files.
# Files are opened in read mode 'r' by default, but they can also be opened in
# write mode 'w' and append mode 'a'.

# Reading from a file
filename = "programming_languages.txt"
with open(filename) as file_handle:
    lines = file_handle.readlines()

    for line in lines:
        print(line.rstrip())

# Writing to a file
filename = "authors.txt"
with open(filename, 'w') as file_handle:
    authors = ['ritchie', 'stroustrup', 'thompson']
    
    for author in authors:
        file_handle.write(author + '\n')

# Appending to a file
filename = "authors.txt"
with open(filename, 'a') as file_handle:
    author = 'nygaard'

    file_handle.write(author)

####################
#### EXCEPTIONS ####
####################
# Exceptions help you respond appropriately to errors that are likely to
# occur. You place code that might cause an exception in the try-block and
# code that should handle the exception goes in the except-clause. Code that
# should run on successfull run of the try-block goes in the else-block.

# Catching an exception
message = "What is your age? "
user_age = input(message)

try:
    # Code that may cause an exception
    user_age = int(user_age)
except ValueError as exc:
    # Code that handle the error
    print("The age you provided is an invalid integer value.")
    print(exc)
else:
    # Successfull run of try-block
    print(f"You gave {user_age} as your age.")