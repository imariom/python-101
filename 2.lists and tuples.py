#########################
#### What are lists? ####
#########################
# A list stores a series of items in a particular order. Lists allow you to
# store sets of information in one place, whether you have just a few or
# millions of items. Lists are one of Python's most powerfull features readily
# accessible to new programmers, and they tie together many important concepts
# in programming.

#########################
#### Defining a list ####
#########################
# Use square brackets to define a list, and use commas to separate individual
# items in the list. Use plural names for lists, to make your code easier to
# read.

# ==> Making a list <==
users = ['val', 'bob', 'mia', 'ron', 'ned']
print(users)

############################
#### Accessing elements ####
############################
# Individual elements in a list are accessed according to their position,
# called the index. The index of the first element is 0, the index of the
# second is 1, and so forth. Negative indices refer to items at the end of
# the list. To get a particular element, write the name of the list and then
# the index of the element in square brackets.

countries = ['mozambique', 'south africa', 'tanzania', 'malawi']

# ==> Getting the first element <==
first_country = countries[0]
print(first_country)

# ==> Getting the second element <==
second_country = countries[1]
print(second_country)

# ==> Getting the last element <==
last_country = countries[-1]
print(last_country)

####################################
#### Modifying individual items ####
####################################
# Once you've defined a list, you can change individual elements in the list.
# You do this by referring to the index of the item you want to modify.

# ==> Changing an element <==
countries = ['mozambique', 'south africa', 'tanzania', 'malawi']
print(countries)

countries[0] = 'lesotho'
countries[-2] = 'zimbabwe'

print(countries)

#########################
#### ADDING ELEMENTS ####
#########################
# You can add elements to the end of a list, or you can insert them wherever
# you like in a list.

# ==> Adding an element to the end of the list 'list.append()' <==
countries= ['mozambique', 'south africa', 'tanzania', 'malawi']
print(countries)

countries.append('zimbabwe')
print(countries)

# ==> Starting with an empty list <==
countries = []

countries.append('mozambique')
countries.append('south africa')
countries.append('tanzania')
countries.append('malawi')
print(countries)

# ==> Inserting elements at a particular position 'list.insert()' <==
countries = ['mozambique', 'south africa', 'tanzania', 'malawi']

countries.insert(1, 'zimbabwe')
print(countries)

countries.insert(-1, 'namibia')
print(countries)

###########################
#### REMOVING ELEMENTS ####
###########################
# You can remove elements by their position in a list, or by the value of the
# item. If you remove an item by its value, Python removes only the first item
# that has that value.

# ==> Deleting an element by its position 'del' <==
countries = ['mozambique', 'south africa', 'tanzania', 'malawi']
del countries[-1]

print(countries)

# ==> Removing an item by its value 'list.remove()' <==
countries = ['mozambique', 'south africa', 'tanzania', 'malawi']

countries.remove('south africa')
print(countries)

##########################
#### POPPING ELEMENTS ####
##########################
# If you want to work with an element that you're removing from the list, you
# can "pop" the element. If you think of the list as a stack of items,
# 'list.pop()' takes an item of the top of the stack. By default 'list.pop()'
# returns the element in the list, but you can also pop elements from any
# position in the list.

# ==> Pop the last item from a list 'list.pop()' <==
artists = ['cesaria evora', 'djmi dludlu', 'moreira chonguissa', 'lira']

recent_artist = artists.pop()
print(recent_artist)
print(artists)

# ==> Pop an item from a particular position in a list 'list.pop(index)' <==
artists = ['cesaria evora', 'djmi dludlu', 'moreira chonguissa', 'lira']

old_artist = artists.pop(0)
print(old_artist)
print(artists)

#####################
#### LIST LENGTH ####
#####################
# The 'len()' function returns the number of items in a list.

# ==> Find the length of a list <==
artists = ['cesaria evora', 'djimi dludlu', 'moreira chonguissa', 'lira']
num_artists = len(artists)

print("There are " + str(num_artists) + " artists in my playlist.")

########################
#### SORTING A LIST ####
########################
# The list.sort() method changes the order of a list permanently. The sorted()
# function returns a sorted copy of the list, leaving the original list
# unchanged. You can sort the items in a list in alphabetical order, or
# reverse alphabetical order. You can also reverse the original order of the
# list. Keep in mind that lowercase and uppercase letters may affect the sort
# order.

# => Sorting a list permanently
artists = ['cesaria evora', 'djimi dludlu', 'moreira chonguissa', 'lira']

artists.sort()
print(artists)

# => Sorting a list permanently in reverse alphabetical order
artists = ['cesaria evora', 'djimi dludlu', 'moreira chonguissa', 'lira']

artists.sort(reverse=True)
print(artists)

# => Sorting a list temporarily
artists = ['cesaria evora', 'djimi dludlu', 'moreira chonguissa', 'lira']

print(sorted(artists))
print(sorted(artists, reverse=True))

# => Reversing the order of a list
artists = ['cesaria evora', 'djimi dludlu', 'moreira chonguissa', 'lira']

artists.reverse()
print(artists)

################################
#### LOOPING THROUGH A LIST ####
################################
# Lists can contain millions of items, so Python provides an efficient way to
# loop through all the items in a list. When you set up a loop, Python pulls
# each item from the list one at a time and stores it in a temporary variable,
# which you provide a name for. This name should be the singular version of
# the list name.
# The indented block of code makes up the body of the loop, where you can work
# with each individual item. Any lines that are not indented run after the 
# loop is completed.

# => Printing all items in a list
artists = ['cesaria evora', 'djimi dludlu', 'moreira chonguissa', 'lira']

for artist in artists:
    print(artist)

# => Printing a message for each item, and a separate message afterwards
artists = ['cesaria evora', 'djimi dludlu', 'moreira chonguissa', 'lira']

for artist in artists:
    print("Playing " + artist + " music!")

print("All musics in the playlist where played.")

##############################
#### THE RANGE() FUNCTION ####
##############################
# You can use the range() function to work with a set of numbers efficiently.
# The range() function starts at 0 by default, and stops one number below the
# number passed to it. You can use the list() function to efficiently generate
# a large list of numbers.

# => Printing the numbers 0 to 100
for number in range(101):
    print(number)

# => Printing the number 1 to 100
for number in range(1, 101):
    print(number)

# => Making a list of numbers from 1 to a million
numbers = list(range(1, 1000001))
print(len(numbers))

###########################
#### SIMPLE STATISTICS ####
###########################
# There are a number of simple statistical functions you can run on a list
# containing numerical data.

# => Finding the minimum height in a list
heights = [1.2, 0.5, 1.0, 1.1, 0.4, 2.1, 1.9]
shortest = min(heights)
print(shortest)

# => Finding the maximum height
heights = [1.2, 0.5, 1.0, 1.1, 0.4, 2.1, 1.9]
tallest = max(heights)
print(tallest)

# => Finding the avergae height
heights = [1.2, 0.5, 1.0, 1.1, 0.4, 2.1, 1.9]
average = sum(heights) / len(heights)
print(average)

########################
#### SLICING A LIST ####
########################
# You can work with any set of elements from a list. A portion of a list is
# called a slice. To slice a list start with the index of the first item you
# want, then add a colon and the index after the last item you want. Leave off
# the first index to start at the beginning of the list, and leave off the
# last index to slice through the end of the list.

# => Getting the first three items
programming_languages = ['assembly', 'c', 'c++', 'python', 'ruby']
first_three = programming_languages[:3]
print(first_three)

# => Getting the middle
programming_languages = ['assembly', 'c', 'c++', 'python', 'ruby']
middle_three = programming_languages[1:4]
print(middle_three)

# => Getting the last three items
programming_languages = ['assembly', 'c', 'c++', 'python', 'ruby']
last_three = programming_languages[-3:]
print(last_three)

######################################################################################
#### Copying a list ####
######################################################################################
# To copy a list make a slice that starts at the first item and ends at the
# last item. If you try to copy a list without using this approach, whatever
# you do to the copied list will affect the original list as well.

# => Making a copy of a list
programming_languages = ['assembly', 'c', 'c++', 'python', 'ruby']
copy_of_programming_languages = programming_languages[:]
print(copy_of_programming_languages)

######################################################################################
#### List comprehensions ####
######################################################################################
# You can use a loop to generate a list based on a range of numbers on another
# list. This is a common operation, so Python offers a more efficient way to
# do it. List comprehensions may look complicated at first, if so, use the for
# loop approach until you're ready to start using comprehensions.
# To write a comprehension, define an expression for the values you want to
# store in the list. Then write a for loop to genearte input values needed to
# make the list.

# ==> Using a loop to generate a list of square numbers <==
squares = []
for x in range(1, 11):
    square = x ** 2
    squares.append(square)

print(squares)

# ==> Using a comprehension to generate a list of square numbers <==
squares = [x ** 2 for x in range(1, 11)]
print(squares)

# ==> Using a loop to convert a list of names to upper case <==
cities = ['matola', 'marracuene', 'polana', 'boane', 'ntenga']

upper_cities = []
for city in cities:
    upper_city = city.upper()
    upper_cities.append(upper_city)

print(upper_cities)

# ==> Using a comprehension to convert a list of names to upper case <==
cities = ['matola', 'marracuene', 'polana', 'boane', 'ntenga']

upper_cities = [city.upper() for city in cities]
print(upper_cities)

######################################################################################
#### Sytling your code ####
######################################################################################
# Use four spaces per indentation level.
# Keep your lines to 79 characters or fewer.
# Use single blank lines to group parts of your program visually.

######################################################################################
#### Tuples ####
######################################################################################
# A tuple is like a list, except you can't change the values in a tuple once
# it's defined. Tuples are good for storing information that shouldn't be
# changed throughout the life of a program. Tuples are designated by
# parentheses instead of square brackets. (You can overwrite an entire tuple,
# but you can't change the individual elements in a tuple).

# ==> Defining a tuple <==
person = ('mario', 92, 2.3)
print(person)

# ==> Looping through a tuple <==
person = ('mario', 92, 2.3)
for attribute in person:
    print(attribute)

# ==> Overwriting a tuple <==
person = ('mario', 92, 2.3)
print(person)

person = ('alfredo', 1.8)
print(person)

######################################################################################
#### Visualizing your code ####
######################################################################################
# When you're first learning about data structures such as lists, it helps to
# visualize how Python is working with the information in your program.
# pythontutor.com is a great tool for seeing how Python keeps track of the
# information in a list. Try the following code on pythontutor.com, and
# then run your own code.

# ==> Build a list and print the items in the list <==
dogs = []

dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')

for dog in dogs:
    print("Hello, " + dog + "!")

print("\nThese were my first two dogs:")
old_dogs = dogs[:2]
for old_dog in old_dogs:
    print(old_dog)

del dogs[0]
dogs.remove('peso')
print(dogs)