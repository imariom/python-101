######################################################################################
## What are classes
######################################################################################
# Classes are the foundation of object-oriented programming. Classes 
# represent real-world things that you want to model in your programs: for
# example dogs, cars, and robots. You use a class to make objects, wich are
# specific instances of dogs, cars and robots. A class defines the general 
# behavior that a whole category of objects can have, and the information
# that can be associated with those objects.

# Classes can inherit from each other - you can write a class that extends the
# functionality of an existing class. This allows you to code efficiently for
# a wide variety of situations.

######################################################################################
## Creating and using a class
######################################################################################
# Consider how we might model a car. What information would we associate with
# a car and what behavior would it have? The information is stored in 
# variables called attributes, and the behavior is represented by functions.
# Functions that are part of a class are called methods.

# => The Car class
class Car():
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")

# => Creatng an object from a class
my_car = Car('audi', 'a4', 2016)

# => Accessing attribute values
print(my_car.make)
print(my_car.model)
print(my_car.year)

# => Calling methods
my_car.fill_tank()
my_car.drive()

# => Creating multiple objects
my_car = Car('audi', 'a4', 2016)
my_old_car = Car('subaru', 'outback', 2013)
my_truck = Car('toyota', 'tacoma', 2010)

######################################################################################
## Modifying attributes
######################################################################################
# You can modify an attribute's value directly, or you can
# write methods that manage updating values more carefully.

# => Modifying an attribute directly
my_new_car = Car('audi', 'a4', 2016)
my_new_car.fuel_level = 5

# => Writing a method to update and increment an attribute's value
class Car():
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year

        # Fuel capacity and level in gallons.
        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")

    def drive(self):
        """Simulate driving."""
        print("The car is moving.")

    # Update
    def update_fuel_level(self, new_level):
        """Update the fuel level."""
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank can't hold that much!")

    #  Increment
    def add_fuel(self, amount):
        """Add fuel to the tank."""
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Added fuel.")
        else:
            print("The tank won't hold that much.")

######################################################################################
## Naming conventions
######################################################################################
# In Python class names are written in CamelCase and object names are written
# in lowercase with underscores. Modules that contain classes should still be
# named in lowercase with underscores.

######################################################################################
## Class Inheritance
######################################################################################
# If the class you're writing is a specialized version of another class, you
# can user inheritance. When once class inherits from another, it 
# automatically takes on all the attributes and methods of the parent class.
# The child class is free to introduce new attributes and methods, and 
# override attributes of the parent class.
# To inherit from another class include the name of the parent class in
# parentheses when defining the new class.

# => The __init__() method for a child class
class ElectricCar(Car):
    """A simple model of an electric car."""

    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)

        # Attributes specific to electric cars.
        # Battery capacity in kwh.
        self.battery_size = 70
        # Charge level in %.
        self.charge_level = 0

# => Adding new methods to the child class
class ElectricCar(Car):
    """A simple model of an electric car."""

    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)

        # Attributes specific to electric cars.
        # Battery capacity in kwh.
        self.battery_size = 70
        # Charge level in %.
        self.charge_level = 0
    
    def charge(self):
        """Fully chage the vehicle."""
        self.charge_level = 100
        print("The vehicle is fully charged.")

# => Using child methods and parent methods
my_ecar = ElectricCar('tesla', 'model s', 2016)

my_ecar.charge()
my_ecar.drive()

# => Overrinding parent methods
class ElectricCar(Car):
    """A simple model of an electric car."""

    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)

        # Attributes specific to electric cars.
        self.battery_size = 70 # battery capacity in kwh
        self.charge_level = 0

    def charge(self):
        """Fully charge the vehicle."""
        self.charge_level = 1000
    
    def fill_tank(self):
        """Display an error message."""
        print("This car has no fuel tank!")

######################################################################################
## Instances as attributes
######################################################################################
# A class can have objects as attributes. This allows classes to work
# together to model complex situations.

# => A Battery class
class Battery():
    """A battery for an electric car."""

    def __init__(self, size=70):
        """Initialize battery attributes."""
        # Capacity in kwh, charge level in %.
        self.size = size
        self.charge_level = 0
    
    def get_range(self):
        """Return the battery's range."""
        if self.size == 70:
            return 240
        elif self.size == 85:
            return 270

# => Using an instance as an attribute
class ElectricCar(Car):
    """A simple model of an electric car."""

    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)

        # Attributes specific to electric cars.
        self.battery = Battery()

    def charge(self):
        """Fully charge the vehicle."""
        self.battery.charge_level = 100
        print("The vehicle is fully charged.")

# => Using the instance
my_ecar = ElectricCar('tesla', 'model x', 2016)

my_ecar.charge()
print(my_ecar.battery.get_range())
my_ecar.drive()


######################################################################################
## Importing classes
######################################################################################
# Class files can get long as you add detailed information and functionality.
# To help keep your program files uncluttered, you can store your classes in
# modules and import the classes you need into your main program.

# => Storing classes in a file (car.py)
"""Represent gas an electric cars."""

class Car():
    """A simple attempt to model a car."""
    pass

class Battery():
    """A battery for an electric car."""
    pass

class ElectricCar(Car):
    """A simple model of an electric car."""
    pass

# => Importing individual classes from a module (my_cars.py)
from car import Car, ElectricCar

my_beetle = Car('volskwagen', 'beetle', 2016)
my_beetle.fill_tank()
my_beetle.drive()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.charge()
my_tesla.drive()

# => Importing an entire module
import car

my_beetle = car.Car('volskwagen', 'beetle', 2016)
my_beetle.fill_tank()
my_beetle.drive()

my_tesla = car.ElectricCar('tesla', 'model s', 2016)
my_tesla.charge()
my_tesla.drive()


######################################################################################
## Classes in Python 2.7
######################################################################################

# => Classes should inherit from object
class ClassName(object):
    pass

# => The Car class in Python 2.7
class Car(object):
    pass

# => Child classs __init__() method is different
class ChildClass(ClassName):
    def __init__(self):
        super(ClassName, self).__init__()

# => The ElectricCar class in Python 2.7
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)

######################################################################################
## Storing objects in a list
######################################################################################
# A list can hold as many items as you want, so you can make a large number
# of objects from a class and store them in a list.

# => A fleet of rental cars
from car import Car, ElectricCar

# Make lists to hold a fleet of cars.
gas_fleet = []
elecric_fleet = []

# Make 500 gas cars and 250 electric cars.
for _ in range(500):
    car = Car('ford', 'focus', 2016)
    gas_fleet.append(car)

for _ in range(250):
    ecar = ElectricCar('nissan', 'leaf', 2016)
    elecric_fleet.append(ecar)

# Fill the gas cars, and charge electric cars.
for car in gas_fleet:
    car.fill_tank()

for car in electric_fleet:
    car.charge()

print("Gas cars:", len(gas_fleet))
print("Electric  cars:", len(electric_fleet))