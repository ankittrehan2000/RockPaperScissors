import random

def RockPaperScissor():
  number = random.randint(1,3)
  #1 - Rock 
  #2 - Paper 
  #3 - Scissors
  if (number == 1):
    return 'rock'
  elif (number == 2):
    return 'paper'
  elif (number == 3):
    return 'scissors'
  else:
    return 'Facing errors'