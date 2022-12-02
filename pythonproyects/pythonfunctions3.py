# Implement a function that will flatten and sort an array of integers in
# ascending order, and which adheres to a functional programming paradigm.

def sortasc(arr):
    arr.sort()


dateofbirth = [1989, 1902, 1886, 2000]
sortasc(dateofbirth)
print(dateofbirth)

# datebyorder = sortasc(dateofbirth)

# print(datebyorder)
# How does this solution ensure data immutability?
# Is this solution a pure function? Why or why not ?
# Is this solution a higher order function? Why or why not ?
# Would it have been easier to solve this problem using a different programming style?
# Why in particular is functional programming a helpful paradigm when solving this problem?


# ---------------------------------------------------------------------------------------------------------

# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object
#  Oriented solution according to the following criteria.
# First, he'll need a general Podracer class defined with max_speed, condition(perfect, trashed, repaired) and
#  price attributes.
# Define a repair() method that will update the condition of the podracer to "repaired".
# Define a new class , AnakinsPod that inherits the Podracer class, but also contains a special
# method called boost that will multiply max_speed by 2.
# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special
#  method called flame_jet that will update
# the condition of another podracer to "trashed".

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"


class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed = self.max_speed*2


class SebulbasPod(Podracer):
    def flame_jet(self):
        self.condition = "trashed"


print(Podracer(50, "new", 100))

print(Podracer.repair())
