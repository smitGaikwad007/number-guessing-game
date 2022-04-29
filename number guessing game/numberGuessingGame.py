import random
print ("number guessing game")
number = random.randint(1, 9)
chances = 0
print ("geuss a number (between 1 and 9):")

while chances < 5:

  guess = int(input("enter your guess :- "))


  if guess == number:
    print ("congratulation !! you won !!")
    break

  elif guess < number:
    print ("Your guess was too low :", guess)

  else :
    print ("your gues is too high :", guess)
    

  chances += 1
if not chances < 5 :

  print("you loose")