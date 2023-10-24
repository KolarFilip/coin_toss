import random

while True:
 choices = "heads", "tails"   
 options = (random.choice(choices))
 flip = options 

 user_input = input("Type your choice: ")
 if user_input == "heads" or "tails":
   print("You choosen!", user_input)

 if flip == "tails":
    print("Coin flipped on tails!")
 if flip == "heads":
    print("Coin flipped on heads!")  

 if user_input == flip:
    print("You won!")
 else:
    print("You lost!")