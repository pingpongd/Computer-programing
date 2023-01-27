import random
print("Roll a die!")
print("How many sides does you dice have?")
sides = input("Sides:") 
sides_int = int(sides)
#asks for amount of sides and converts into a integer

print(random.randint(1,sides_int))
#prints out as if you were to roll a dice with the number of sides
answer = input("Would you like to re-roll? Y/N ")
if answer == ("Y"):
    print(random.randint(1,sides_int))

if answer == ("N"):
     print("Goodbye")
#asks for re-roll or not