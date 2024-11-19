"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge=0.00
freeChars=5
numChars=18
color="black"
woodType="oak"

charge=35.00

#input statements
numChars=int(input("How many Characters do you need?: "))
color=input("What color lettering do you want?: ")
woodType=input("What wood would you like?: ")
# Write assignment and if statements here as appropriate.
if numChars > 5:
    charge+=4*(numChars-freeChars)
if color=="Gold":
    charge+= 15.00
if woodType=="Oak":
    charge+=20.00
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))