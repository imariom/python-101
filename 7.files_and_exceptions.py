#############################################
#### WHAT ARE FILES? WHAT ARE EXCEPTIONS ####
#############################################
# Your programs can read information in from files, and they can write data to
# files. Reading from files allows you to work with a wide variety of
# information; writing to files allows users to pick up where they left off
# the next time they run a program. You can write text to files, and you can
# store python structures such as lists in data files.

# Exceptions are special objects that help your programs respond to errors in
# appropriate ways. For example if your program tries to open a file that
# doesn't exist, you can use exceptions to display an informative error
# message instead of having the program crash.

#############################
#### READING FROM A FILE ####
#############################
# To read from a file your program needs to open the file and then read the
# contents of the file. You can read the entire contents of the file at once,
# or read the file line by line. The 'with' statement makes sure the file is
# closed properly when the program has finished accessing the file.

# => Reading an entire file at once
from os import error
from types import resolve_bases


filename = 'siddhartha.txt'

with open(filename) as file_handle:
    contents = file_handle.read()

print(contents)

# => Reading line by line
# Each line that's read from the file has a newline character at the end of
# the line, and the print function adds its own newline character. The
# rstrip() method gets rid of the extra newline character that would result
# in printing to the terminal.
filename = "siddhartha.txt"

with open(filename) as file_handle:
    for line in file_handle:
        print(line.rstrip())

# => Storing the lines in a list
filename = 'siddhartha.txt'

with open(filename) as file_handle:
    lines = file_handle.readlines()

for line in lines:
    print(line.rstrip())

###########################
#### WRITING TO A FILE ####
###########################
# Passing the 'w' argument to open() tells Python you want to write to the
# file. Be careful; this will erase the contents of the file if it already
# exists. Passing the 'a' argument tells Python you want to append to the end
# of an existing file.

# => Writing to an empty file
filename = "programming.txt"

with open(filename, 'w') as file_handle:
    file_handle.write("I love programming")

# => Writing multiple lines to an empty file
filename = "programming.txt"

with open(filename, 'w') as file_handle:
    file_handle.write('I love programming\n')
    file_handle.write("I love creating compilers.\n")

# => Appending to a file
filename = "programming.txt"

with open(filename, 'a') as file_handle:
    file_handle.write("I also love working with Machine Learning\n")
    file_handle.write("I love making mathematical models.\n"

####################
#### FILE PATHS ####
####################
# When Python runs the open() function, it looks for the file in the same
# directory where the program that's being executed is stored. You can open a
# file from a subfolder using a relative path. You can also use an absolute
# path to open any file on your system.

# => Opening a file froma subfolder
file_path = "text_files/alice.txt"

with open(file_path) as file_handle:
    lines = file_handle.readlines()

for line in lines:
    print(line.rstrip())

# => Opening a file using an absolute path
file_path = "/home/imariom/books/alice.txt"

with open(file_path) as file_handle:
    for line in file_handle:
        print(line.rstrip())

# => Opening a file on Windows
# Windows will sometimes interpret forward elements incorrectly. If you run
# into this, use backslashes in you file paths.
file_path = "C:\\Users\\imariom\\books\\alice.txt"

with open(file_path) as file_handle:
    for line in file_handle:
        print(line.rstrip()

##############################
#### THE try-except BLOCK ####
##############################
# When you think an error may occur, you can write a try-except block to
# handle the exception that might be raised. The try block tells Python
# to try running some code, and the except block tells Python what to do
# if the code results in a particular kind of error.

# => Handling the ZeroDivisionError exception
try:
    print(5/0)
except ZeroDivisionError as error:
    print("You can't divide by zero!")
    print(error)

# => Handling the FileNotFoundError exception
file_name = "module.cc"

try:
    with open(file_name) as file_handle:
        for line in file_handle:
            print(line.rstrip())
except FileNotFoundError as error:
    message = "Can't find file {0}.".format(file_name)
    print(message)
    print(error)

##########################################
#### KNOWING WICH EXCEPTION TO HANDLE ####
##########################################
# It can be hard to know what kind of exception to handle when writing code.
# Try writing your code without a try block, and make it generate an error.
# The traceback will tell you what kind of exception your program needs to
# handle.

########################
#### THE else BLOCK ####
########################
# The try block should only contain code that may cause an error. Any code
# that depends on the try block running successfully should be placed in
# the else block.

# => Using an else block
print("Enter two numbers. I'll divide them.")

x = input("First number: ")
y = input("Second number: ")

try:
    result = int(x) / int(y)
except (ZeroDivisionError, ValueError) as error:
    print("Th value you provided is not valid or a zero division was made")
else:
    print(result)

# => Preventing crashes from user input
# Without the except block in the following example, the program would crash
# if the user tries to divide by zero. As written, it will handle the error
# gracefully and keep running.
"""A simple calculator for division only."""

print("Enter two numbers. I'll divide them.")
print("Enter 'q' to quit.")

while True:
    x = input("\nFirst number: ")
    if x == 'q':
        break
    
    y = input("Second number: ")
    if y == 'q':
        break

    try:
        result = int(x) / int(y)
    except ZeroDivisionError as error:
        print("You can't divide by zero!")
    else:
        print(result)

######################################################################################
## Deciding which errors to report
######################################################################################
# Well-written, properly tested code is not very prone to internal errors such
# as syntax or logical errors. But every time your program depends on
# something external such as user input or the existence of a file, there's a
# possibility of an exception being raised.

# It's up to you how to communicate errors to your users. Sometimes users need
# to know if a file is missing; sometimes it's better to handle the error
# silently. A little experience will help you know how much to report.

######################################################################################
## Failing silently
######################################################################################
# Sometimes you want your program to just continue running when it encounters
# an error, without reporting the error to the user. Using the pass statement
# in an else block allows you to do this.

# => Using the pass statement in an else block
file_names = ['alice.txt', 'siddharthat.txt', 'moby_dick.txt',
    'little_women.txt']

for file_name in file_names:
    # Report the length of each file found
    try:
        with open(file_name) as file_handle:
            lines = file_handle.readlines()
    except FileNotFoundError as error:
        # Just move on to the next file.
        pass
    else:
        num_lines = len(lines)
        message = "{0} has {1} lines.".format(file_name, num_lines)
        print(message)

######################################################################################
## Avoid bare except blocks
######################################################################################
# Exception-handling code should catch specific exceptions that you expect to
# happen during your program's execution. A bare except block will catch all
# exceptions, including keyboard interrupts and system exits you might need when
# forcing a program to close.

# If you want to use a try block and you're not sure which exception to catch,
# use Exception. It will catch most exceptions, but still allow you to
# interrupt programs intentionally.

# => Don't use bare except blocks
try:
    # Do something
    pass
except:
    pass

# => Use Exception instead
try:
    # Do something
    pass
except Exception as error:
    pass

# => Printing the exception
try:
    # Do somthing
    pass
except Exception as exc:
    print(exc, type(exc))

######################################################################################
## Storing data with json
######################################################################################
# The json module allows you to dump simple Python data structures into a file,
# and load the data from that file the next time the program runs. The JSON
# data format is not specific to Python, so you can share this kind of data
# with people who work in other languages as well.

# Knowing how to manage exceptions is important when working with stored data.
# You'll usually want to make sure the data you're trying to load exists
# before working with it.

# => Using json.dump() to store data
"""Store some numbers."""

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = "numbers.json"
with open(filename, 'w') as file_handle:
    json.dump(numbers, file_handle)

# => Using json.load() to read data
"""Load some previously stored numbers."""
import json

filename = "numbers.json"
with open(filename) as file_handle:
    numbers = json.load(file_handle)

print(numbers)

# => Making sure the stored data exists
import json

try:
    with open(filename) as file_handle:
        numbers = json.load(file_handle)
except FileNotFoundError as exc:
    message = "Can't find {0}.".format(filename)
    print(message)
else:
    print(numbers)

######################################################################################
## Practice with exceptions
######################################################################################
# Take a program you've already witten that prompts for user input, and add
# some error-handling code to the program.