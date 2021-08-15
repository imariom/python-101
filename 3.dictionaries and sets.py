######################################################################################
## What are dictionaries?
######################################################################################
# Python's dictionaries allow you to connect pieces of related information.
# Each piece of information in a dictionary is stored as a key-value pair.
# When you provide a key, Python returns the value associated with that key.
# You can loop through all the key-value pairs, all the keys, or all the
# values.

######################################################################################
## Defining a dictionary
######################################################################################
# Use curly braces to define a dictionary. Use colons to connect keys and
# values, and use commas to separate individual key-value pairs.

# ==> Making a dictionary <==
capitals = {'mozambique': 'maputo', 'tanzania': 'dodoma', 'south africa': 'cape town'}
print(capitals)

######################################################################################
## Accessing values
######################################################################################
# To access the value associated with an individual key give the name of the
# dictionary and then place the key in a set of brackets. If the key you're
# asking for is not in the dictionary, and error will occur.
# You can also use the 'get()' method, which returns 'None' instead of an
# error if the key doesn't exist. You can also specify a default value to use
# if the key is not in the dictionary.

# ==> Getting the value associated with a key <==
capitals = {'mozambique': 'maputo', 'tanzania': 'dodoma', 'south africa': 'cape town'}

print(capitals['mozambique'])
print(capitals['south africa'])

# ==> Getting the value with 'get()' <==
capitals = {'mozambique': 'maputo', 'tanzania': 'dodoma', 'south africa': 'cape town'}

mozambique_capital = capitals.get('mozambique')
tanzania_capital = capitals.get('tanzania')
angola_capital = capitals.get('angola')

print(mozambique_capital)
print(tanzania_capital)
print(angola_capital)

######################################################################################
## Adding new key-value pairs
######################################################################################
# You can store as many key-value pairs as you want in a dictionary, until
# your computer runs out of memory. To add a new key-value pair to an existing
# dictionary give the name of the dictionary and the new key in square
# brackets, and set it equal to the new value.
# This also allows you to start with an empty dictionary and add key-value
# pairs as they become relevant.

# ==> Adding a key-value pair <==
capitals = {'mozambique': 'maputo'}

capitals['tanzania'] = 'dodoma'
capitals['south africa'] = 'cape town'

print(capitals)

# ==> Adding to an empty dictionary <==
capitals = {}

capitals['mozambique'] = 'maputo'
capitals['tanzania'] = 'dodoma'
capitals['south africa'] = 'cape town'

print(capitals)

######################################################################################
## Modifying values
######################################################################################
# You can modify the value associated with any key in a dictionary. To do so
# give the name of the dictionary and enclose the key in square brackets, then
# provide the new value for that key.

# ==> Modifying values in a dictionary <==
person = {'name': 'Mario A. Moiane', 'age': 92, 'height': 2.3}
print(person)

# Change the person's age and height
person['age'] = 17
person['height'] = 1.4

print(person)

######################################################################################
## Removing key-value pairs
######################################################################################
# You can remove any key-value pair you want from a dictionary. To do so use
# the 'del' keyword and the dictionary name, followed by the key in square
# brackets. This will delete the key and its associated value.

# ==> Deleting a key-value pair <==
capitals = {'mozambique': 'maputo', 'tanzania': 'dodoma', 'angola': 'luanda'}
print(capitals)

del capitals['mozambique']
print(capitals)

######################################################################################
## Looping through a dictionary
######################################################################################
# You can loop through a dictionary, in three ways: you can loop through all
# the key-value pairs, all the keys, or all the values.
# A dictionary only tracks the connections between keys and values; it doesn't
# track the order of items in the dictionary. If you want to process the
# information in order, you can sort the keys in your loop.

fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# ==> Looping through all key-value pairs <==
for name, language in fav_languages.items():
    print(name + ": " + language)

# ==> Looping through all keys <==
for name in fav_languages.keys():
    print(name + " has a favorite programming language")

# ==> Looping through all values <==
for language in fav_languages.values():
    print(language + " is a favorite programming language")

# ==> Looping all the keys in order <==
for name in sorted(fav_languages.keys()):
    print(name + ": " + fav_languages[name])

######################################################################################
## Dictionary length
######################################################################################
# You can find the number of key-value pairsin a dictionary.

# ==> Finding a dictionary's length <==
capitals = {'mozambique': 'maputo', 'tanzania': 'dodoma', 'france': 'paris'}

num_capitals = len(capitals)
print(num_capitals)

######################################################################################
## Nesting - A list of dictionaries
######################################################################################
# It's sometimes useful to store a set of dictionaries in a list; this is
# called nesting.

# => Storing dictionaries in a list
# Start with an emtpy list.
users = []

# Make a new user, and add them to the list.
new_user = {
    'last': 'fermi',
    'first': 'enrico',
    'username': 'efermi'
}
users.append(new_user)

# Make another new user, and add them as well.
new_user = {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie'
}
users.append(new_user)

# Show all information about each user.
for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
    print("\n")

# => You can also define a list of dictionaries directly, without using
# append():
# Define a list of users, where each user is represented by a dictionary.
users = [
    {
        'last': 'fermi',
        'first': 'enrico',
        'username': 'efermi'
    },
    {
        'last': 'curie',
        'first': 'marie',
        'username': 'mcurie'
    }
]

# Show all information about each user.
for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
    print("\n")

######################################################################################
## Nesting - Lists in dictionary
######################################################################################
# Storing a list inside a dictionary allows you to associate more than one
# value with each key.

# => Storing lists in a dictionary
# Store multiple languages for each person.
fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

# Show all responses for each person.
for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)

######################################################################################
## Nesting - A dictionary of dictionary
######################################################################################
# You can store a dictionary inside another dictionary. In this case each
# value associated with a key is itself a dictionary.

# => Storing  dictionaries in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_dict in users.items():
    print("\nUsername: " + username)
    full_name = user_dict['first'] + " "
    full_name += user_dict['last']
    location = user_dict['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

######################################################################################
## Levels of nesting
######################################################################################
# Nesting is extremely useful in certain situations. However, be aware of
# making your code overly complex. If you're nesting items much deeper than
# what you see here there are probably simpler ways of managing your data,
# such as using classes.

######################################################################################
## Using an OrderedDict
######################################################################################
# Standard Python dictionaries don't keep track of the order in which keys and
# values are added; They only preserve the association between each key and
# its values. If you want to preserve the order in which keys and values are
# added, use an OrderedDict.

# ==> Preserving the order of keys and values <==
from collections import OrderedDict

fav_languages = OrderedDict()

fav_languages['mario'] = ['c++', 'python']
fav_languages['jen'] = ['python', 'ruby']
fav_languages['sarah'] = ['c']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['python', 'haskell']

for name, languages in fav_languages.items():
    print(name + ": ")
    for language in languages:
        print("\t-", language)

######################################################################################
## Generating a million dictionaries
######################################################################################
# You can use a loop to generate a large number of dictionaries efficiently,
# if all the dictionaries start out with similar data.

# ==> A million aliens <==
aliens = []

# Make a million green aliens, worth 5 points each. Have them all
# start in one row.
for alien_num in range(1000000):
    alien = {
        'color': 'green',
        'points': 5,
        'x': 20 * alien_num,
        'y': 0
    }

    aliens.append(alien)

# Prove the list contains a million items
num_aliens = len(aliens)
print("Number of aliens created:", num_aliens)