#Okay so a good start is run while true 
# we want a random pick- we want to go through the dictionary at random 
# we need to import art and data 
import art 
import random
from game_data import data 
#okay we have a random number 
a= random.randint(0,len(data))
# we are printing the art! fabulous but vs will be in the while loop
print(art.logo)
print(art.vs)
print(a)


game_over= False
