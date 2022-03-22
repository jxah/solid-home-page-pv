# small game to guess a number while waiting
import random

# a is my random number
a = 1#random.randrange(1,10)

responses = ["O. M. G.!", "wow!","awesome!", "ooh!", "good!", "almost gone!", "maybe next time. oh and the number is "+str(a)]
i=0
#this is for counting times you have guessed

while True:
  try:
    guess = input("Guess my number, which is a number from 1 to 10:")
    int(guess)
  except:
    continue
    
  correct = (a == int(guess))
  strikeout = (i == 6)
  if correct or strikeout: 
    print(responses[i])
    break
  else: 
    i = i+1
  pass
