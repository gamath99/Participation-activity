""" 
Dice Game 
Gama Mathurin
Cretion  of a dice game that contain 6 sides, another one with 10 sides and a last one with 20 sides, which should be roll 10 times for each. 
6/30/2026
"""

#import the random module that would be use whenthe dice will roll
import random

#Create the die class
class die:
    """initialize the dice with a default of 6 sides """
    def __init__(self, sides = 6):
        self.sides = sides


    """create the method that will be useto roll the die"""
    def roll_die(self):
        print(random.randint(1,self.sides))

#Create the 6 sided dice
print("Rolling of a 6-sided die 10 times:")
die_6side = die()

#Launch of the 6 sided die
 
for i in range(10):
    die_6side.roll_die()

#Create the 10 sided dice
print("\nRolling of a 10-sided die 10 times:")
die_10sides = die(10)

#Launch of the 10 sided die
 
for i in range(10):
    die_10sides.roll_die()

#Create the 20 sided dice
print("\nRolling of a 6-sided die 10 times:")
die_20sides = die(20)

#Launch of the 20 sided die
 
for i in range(10):
    die_20sides.roll_die()    