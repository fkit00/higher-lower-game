#Okay so a good start is run while true 
# we want a random pick- we want to go through the dictionary at random 
# we need to import art and data 
import art 
import random
from game_data import data 
from replit import clear
#okay we have a random number 
a= random.randint(0,len(data))

# we are printing the art! fabulous but vs will be in the while loop


# so in the game the second one becomes the first one in the next round 
game_over= False
score = 0
first_no=random.randint(0,len(data)-1)
first_id=data[first_no]

while game_over == False:
  clear()
  print(art.logo)
  print(f"The score is {score}")
  print(f"Compare A: {first_id['name']}, a {first_id['description']},from {first_id['country']}")
  print(art.vs)
  second_no=random.randint(0,len(data)-1)
  second_id=data[second_no] 
  answer=input(f"Compare B: {second_id['name']}, a {second_id['description']},from {second_id['country']}. Type who has more followers: A or B ").lower()
  if answer != 'a' and answer != 'b':
    print('what are you playing at ')
   
  elif answer == 'a' and first_id['follower_count']> second_id['follower_count']:
    print('Congrats you got it right!')
    first_id=second_id
    score+=1
  
  elif answer == 'b' and second_id['follower_count']> first_id['follower_count']:
    print('Congrats you got it right!')
    first_id=second_id
    score+=1
   
  else:
    print(f"You got it wrong! {first_id['name']} has {first_id['follower_count']} million followers and {second_id['name']} has {second_id['follower_count']} million followers  ")
    game_over=True
  
    
  