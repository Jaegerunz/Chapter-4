"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge=0.00
freeChars=5
numChars=20
color="gold"
woodType="pine"

charge=35.00
# Write assignment and if statements here as appropriate.
if numChars > 5:
    charge+=4*(numChars-freeChars)
if color=="gold":
    charge+= 15.00
if woodType=="oak":
    charge+=20.00
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))