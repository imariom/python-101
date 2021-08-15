######################################################################################
## What are if statements? What are while loops?
######################################################################################
# If statements allow you to examine the current state of a program and
# respond appropriately to that state. You can write a simple if statement
# that checks one condition, or you can create a complex series of if
# statements that identify the exact conditions you're looking for.

# While loops run as long as certain conditions remain true. You can use
# while loops to let your programs run as long as your users want them to.

######################################################################################
## Conditional tests
######################################################################################
# A conditional test is an expression that can be evaluated as True or False.
# Python uses the values True and False to decide whether the code in an if
# statement should be executed.

# Checking for equality
# A single equal sign assings a value to a variable. A double equal sign (==)
# checks whether two values are equal.
car = 'bmw'
car == 'bmw' # True

car = 'audi'
car == 'bmw' # False

# => Ignoring case when making a comparison
car = 'Audi'
car.lower() == 'audi' # True

# => Checking for inequality
topping = 'mushrooms'
topping != 'anchovies' # True

######################################################################################
## Numerical comparisons
######################################################################################
# Testing numerical values is similar to testing string values.

# => Testing equality and inequality
age = 18
age == 18 # True

age != 18 # False

# => Comparison operators
age = 19
age < 21 # True
age <= 21 # True
age > 21 # False
age >= 21 # False

######################################################################################
## Checking multiple conditions
######################################################################################
# You can check multiple conditions at the same time. The and operator returns
# True if all the conditions listed are True. The or operator returns True if
# any of conditions is True.

# => Using and to check multiple conditions
age_0 = 22
age_1 = 18

age_0 >= 21 and age_1 >=21 # False

age_1 = 23
age_0 >= 21 and age_1 >= 21 # True

# => Using or to check multiple conditions
age_0 = 22
age_1 = 18

age_0 >= 21 or age_1 >= 21 # True

age_0 = 19
age_0 >= 21 or age_1 >= 21

######################################################################################
## Boolean values
#####################################################################################
# A boolean value is either True or False. Variables with boolean values are
# often used to keep track of certain conditions within a program.

# => Simple boolean values
game_active = True
can_edit = False

######################################################################################
## If statements
######################################################################################
# Several kinds of if statements exist. Your choice of which to use depends on
# the number of conditions you need to test. You can have as many elif blocks
# as you need, and the else block is always optional.

# A simple if statement
age = 19
if age >= 18:
    print("You're old enough to vote!")

# If-else statements
age = 17

if age >= 18:
    print("You're old enough to vote!")
else:
    print("You can't vote yet.")

# The if-elif-else statements
age = 12

if age <= 4:
    price = 0
elif age <= 18:
    price = 5
else:
    price = 10

print("Your cost is $" + str(price) + ".")


######################################################################################
## Conditional tests with lists
######################################################################################
# You can easily test whether a certain value is in a list. You can also test
# whether a list is empty before trying to loop through the list.

# Testing if a value is in a list
players = ['al', 'bea', 'cyn', 'dale']

if 'al' in players: # True
    print("al is in the game of this sunday")
elif 'eric' in players:
    print("eric will play too")

# Testing if a value is not in a list
banned_users = ['ann', 'chad', 'dee']
user = 'erin'

if user not in banned_users:
    print("You can play!")

# Checking if a list is emtpy
players = []

if players:
    for player in players:
        print(player)
else:
    print("We have no players yet!")

######################################################################################
## Accepting input
######################################################################################
# You can allow your users to enter input using the input() statement. In
# Python 3, all input is stored as a string.

# A simple input
name = input("Whats's your name? ")
print("Hello, " + name + ".")

# Accepting numerical input
age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("\nYou can vote!")
else:
    print("\nYou can't vote yet.")

# Accepting input in Python 2.7
# Use raw_input() in Python 2.7. This function interprets all input as a
# string, just as input() does in Python 3.
name = raw_input("What's your name? ")
print("Hello, " + name + ".")

######################################################################################
## While loops
#####################################################################################
# A while loop repeats a block of code as long as a condition is True.

# Couting to 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the user choose when to quit
prompt = "\nTell me something, and I'll repeat it back to you."
prompt += "\nEnter 'quit' to quit the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# Using a flag
prompt = "\nTell me something, and I'll repeat it back to you."
prompt += "\nEnter 'quit' to quit the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Using a break to exit a loop
prompt = "\nTell me something, and I'll repeat it back to you."
prompt += "\nEnter 'quit' to quit the program. "

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message)

######################################################################################
## Breaking out of loops
######################################################################################
# You can use the 'break' statement and the 'continue' statement with any of
# Python's loops. For example you can use 'break' to quit a for loop that's  
# working trough a list or a dictionary. You can use 'continue' to skip over
# certain items when looping through a list or dictionary as well.

# Using 'break' and 'continue' in a while loop
banned_players = ['reinildo', 'tico tico', 'madeira', 'messi', 'cristiano ronaldo']

prompt = "\nAdd a player to your team."
prompt += "\nEnter 'quit' when you're done. "

players = []
while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_players:
        print(player + " was banned")
        continue
    else:
        players.append(player)

print("\nYour team:")
for player in players:
    print(" -", player)

######################################################################################
## Avoiding infinite loops
######################################################################################
# Every while loop needs a way to stop running so it won't continue to run
# forever. If there's no way for the condition to become False, the loop will
# never stop running.

# An infinite loop
while True:
    name = input("\nWho are you?")
    print("Nice to meet you," + name)

######################################################################################
## Removing all instances of a value from a list
######################################################################################
# The remove() method removes a specific value from a list, but it only
# removes in that list the first occurence of the value you provide. You can
# use a while loop to remove all instances of a particular value.

# Removing all 'cats' from a list of 'pets'
pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)