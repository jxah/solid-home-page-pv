# small game to guess a number while waiting
import random

# a is my random number
 workspace-3
a = random.randrange(1,10)

responses = ["Genius!", "Magnificent!", "Impressive!", "Splendid!", "Great!", "Phew!", string(a)]

a = 1#random.randrange(1,10)

responses = ["O. M. G.!", "wow!","awesome!", "ooh!", "good!", "almost gone!", "maybe next time. oh and the number is "+str(a)]
 main
i=0
#this is for counting times you have guessed

while True:
 workspace-3
  guess = input("Guess my number, which is a number from 1 to 10:")

  try:
    guess = input("Guess my number, which is a number from 1 to 10:")
    int(guess)
  except:
    continue
    if guess > 10:
      continue
 main
  correct = (a == int(guess))
  strikeout = (i == 6)
  if correct or strikeout: 
    print(responses[i])
    break
  else: 
 workspace-3
    i = i+i

    i = i+1
 main
  pass
