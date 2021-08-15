#############################
#### WHY TEST YOUR CODE? ####
#############################
# When you write a function or a class, you can also write tests for that
# code.

# Testing proves that your code works as it's supposed to in the situations
# it's designed to handle, and also when people use your programs in
# unexpected ways.

# Writing tests gives you confidence that your code will work correctly as
# more people begin to use your programs.

# You can also add new features to your programs and know that you haven't
# broken existing behavior.

# A unit test verifies that one specific aspect of your code works as it's
# supposed to.

# A test case is a collection of unit tests which verify your code's behavior
# in a wide variety of situations.

############################################
#### TESTING A FUNCTION: A PASSING TEST ####
############################################
# Python's 'unittest' module provides tools for testing your code.
# To try it out, we'll create a function that returns a full name.
# We'll use the function in a regular program, and then build a test case for
# the function.

# => A functio to test
def get_full_name(first, last): # save this as full_names.py
    """Return a full name"""
    full_name = f"{first} {last}"
    return full_name.title()

# => Using the function
# from full_names import get_full_name # uncommnet this line

janis = get_full_name('janis', 'joplin')
print(janis)

bob = get_full_name('bob', 'dylan')
print(bob)

############################
#### TESTING A FUNCTION ####
############################
# => Building a test case with one unit test.
# To build a test case, make a class that inherits from unittest.TestCase and
# write methods that begin with 'test_'.

# Save this as test_full_names.py
import unittest
from full_names import get_full_name

class NamesTestCase(unittest.TestCase):
    """Tests for full_names.py"""

    def test_first_last(self):
        """Test names like Janis Joplin"""
        full_name = get_full_name('Janis', 'Joplin')
        self.assertEqual(full_name, 'Janis Joplin')

unittest.main()

# => Running the test
# Python reports on each unit test in the test case.
# The dot reports a single passing test.
# Python informs us that it ran 1 test in less than 0.000 seconds, and the OK
# lets us know that all unit tests in the test case passed.


############################################
#### TESTING A FUNCTION: A FAILING TEST ####
############################################
# Failing tests are important; they tell you that a change in the code has
# affected existing behavior.

# When a test fails, you need to modify the code so the existing behavior
# still works.

# => Modifying the function
# We'll modify get_full_name() so it handles middle names, but we'll do it in
# a way that breaks existing behavior.
def get_full_name(first, middle, last):
    """Return a full name"""
    full_name = "{} {} {}".format(first, middle, last)
    return full_name.title()

# => Using the function
# from full_names import get_full_name # uncomment this line

john = get_full_name('john', 'lee', 'hooker')
print(john)

david = get_full_name('david', 'lee', 'roth')
print(david)

# => Running the test
# When you change your code, it's important to run your existing tests.
# This will tell you wether the changes you made affected existing behavior.

# => Fixing the code
# When a test fails, the code needs to be modified until the test passes again.
# (Don't make the mistake of rewrinting your tests to fit your new code)
# Here we can make the middle name optional.
def get_full_name(first, last, middle=None):
    """Return a full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# => Running the test
# Now the test should pass again, which means our original functionality is
# still intact.

##########################
#### ADDING NEW TESTS ####
##########################
# You can add as many unit tests to a test case as you need.
# To write a new test, add a new method to your test case class.

# => Testing middle names
# We've shown that get_full_name() works for first and last names.
# Let's test if it works for middle names as well.
import unittest
from full_names import get_full_name

class NamesTestCase(unittest.TestCase):
    """Tests for full_names.py"""

    def test_first_last(self):
        """Test names like Mario Moiane"""
        full_name = get_full_name('mario', 'moiane')
        self.assertEqual(full_name, 'Mario Moiane')

    def test_middle(self):
        """Test names like Mario Alfredo Moiane"""
        full_name = get_full_name('mario', 'moiane', 'alfredo')
        self.assertEqual(full_name, 'Mario Alfredo Moiane')

unittest.main()

# => Running the tests
# The two dots represent two passing tests.

#####################################
#### A VARIETY OF ASSERT METHODS ####
#####################################
# Python provides a number of assert methods you can use to test your code.

# => Verify that a==b or a!=b
# assertEqual(a, b)
# assertNotEqual(a, b)

# => Verify that x is True or x is False
# assertTrue(x)
# assertFalse(x)

# => Verify an item is in a list, or not in a list
# assertIn(item, list)
# assertNotIn(item, list)

#########################
#### TESTING A CLASS ####
#########################
# Testing a class is similar to testing a function, since you'll
# mostly be testing your methods.

# => A class to test save this in a file "accountant.py"
class Accountant:
    """Manage a bank account."""

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if ((self.balance - amount) >= 0):
            self.balance -= amount

# => Building a testcase
# For the first test, we'll make sure we can start out with different initial
# balances.
# Save this in a file "test_accountant.py"
import unittest
# from accountant import Accountant # uncomment this line

class AccountantTestCase(unittest.TestCase):
    """Tests for the class Accountant"""

    def test_initial_balance(self):
        # Initial balance should be 0
        acc = Accountant()
        self.assertEqual(acc.balance, 0)

        # Test non-default balances
        acc = Accountant(100)
        self.assertEqual(acc.balance, 100)

unittest.main()

# => Running the test

#####################################
#### WHEN IS OK TO MODIFY TESTS? ####
#####################################
# In general you shouldn't modify a test once it's written.
# When a test fails it usually means new code you've written has broken
# existing functionality, and you need to modify the new code untill all
# existing tests pass.
# If your original requirements have changed, it may be appropriate to modify
# some tests. This usually happens in the early stages of a project when
# desired behavior is still being sorted out.

############################
#### THE setUp() METHOD ####
############################
# When testing a class, you usually have to make an instance of the class.
# The setUp() method is run before every test.
# Any instances you make in setUp() are available in every test you write.

# => Using setUp() to support multiple tests
# The instance self.acc can be used in each new test.
import unittest
from accountant import Accountant

class AccountantTestCase(unittest.TestCase):
    """Tests for the class Accountant."""

    def setUp(self):
        self.acc = Accountant()

    def test_initial_balance(self):
        # Initial balance should be 0
        self.assertEqual(self.acc.balance, 0)

        # Test non-default initial balance
        acc = Accountant(100)
        self.assertEqual(acc.balance, 100)

    def test_deposit(self):
        # Test single deposit
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 100)

        # Test multiple deposits
        self.acc.deposit(100)
        self.acc.deposit(100)
        self.assertEqual(self.acc.balance, 300)

    def test_withdrawal(self):
        # Test single withdraw
        self.acc.deposit(1000)
        self.acc.withdraw(100)
        self.assertEqual(self.acc.balance, 900)

unittest.main()

# => Runnint the test