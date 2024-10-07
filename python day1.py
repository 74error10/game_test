import random
import os
import time
import sys
def if_youwant():
    while True:

     def get_choices():
        player_choice = input("Enter a choice(rock,paper,scissors)/stop:").lower()
        options = ["rock","paper","scissors"]
        computer_choices=random.choice(options)
        choices = {"player":player_choice,"computer":computer_choices}
        return choices
     def check_win(player, computer):
      if player == computer:
        return "It's a tie!"
      
      elif(player == "rock" and computer== "scissors") or  (player == "scissors" and computer== "paper") or  (player == "paper" and computer== "rock"):
        return "You win!"
      elif(player == "scissors" and computer== "rock") or  (player == "paper" and computer== "scissors") or  (player == "rock" and computer== "paper"):
        return "Computer win!"
     
     
      elif player =="stop":
        print("Thanks Sir .")
        time.sleep(1)
        sys.exit()
      else:
        return "Error!"
     check = get_choices()
     result = check_win(check["player"],check["computer"])
     print(result)
     time.sleep(4)
     os.system('clear')
os.system('clear')    
print("                    Hellow Sir                ")
user_input1=input("Do you wnat to play is game ?(yes or no):").lower()
if user_input1 == "yes":
  if_youwant()
elif user_input1 == "no":
   print("Thanks You sir ")
   time.sleep(1)
   sys.exit() 
 