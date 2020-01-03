from PointCounter import PointCounter
from Components import checkInps
from RockPaperScissors import RockPaperScissor

var = PointCounter()

def whoWins(userInput, computerInput): #returns the winner of the current play
  if (userInput == computerInput):
    return str('Both said ' + userInput + '\nNo Points scored\n')

  elif (userInput == 'scissors' and computerInput == 'paper') or (userInput == 'paper' and computerInput == 'rock') or (userInput == 'rock' and computerInput == 'scissors'): #checks for user winning scenarios and increases their points
    var.incUserPoints()
    return 'Player wins a point !!! \n'

  elif (userInput == 'scissors' and computerInput == 'rock') or (userInput == 'paper' and computerInput == 'scissors') or (userInput == 'rock' and computerInput == 'paper') : #checks for the computer winning scenarios and increses its points
    var.incCompPoints()
    return 'Computer wins a point \n'

def printScore():
  return 'User Points :' + var.getUserPoints() + '\nComputer Points :' + var.getCompPoints() + '\n'


def Run():
  while True: #keeps iterating until the user quits the game
    userInput = input('Enter your choice \n')



#checks if input is quit or score and acts accordingly
    def options():
      if (userInput.lower() == 'quit'): #checks to see if the input says quit
        print('Game Results:\n\n' + printScore())
        print(var.winner())
      if (userInput.lower() == 'score'):
        print(printScore())
    


    
    while True: #keeps iterating until a correct input is entered
      validityUserInp = checkInps(userInput)

      if (validityUserInp == 'Invalid Input'):
        print('Please enter a valid choice or check your spelling\n') 
        userInput = input('Enter your choice again \n')

#if input is valid proceed with the game
      else:
        if userInput.lower() == 'quit' or userInput.lower() == 'score':
          options() #call the options function to deal with the inputs
        if userInput.lower() == 'rock' or userInput.lower() == 'paper' or userInput.lower() == 'scissors':
        
          compInp = RockPaperScissor()
          print('Rock.. Paper.. Scissors.. Shoot\n')
          print(compInp)
          print(whoWins(userInput.lower(),compInp.lower()))
        break

#break the outer while loop if quit is chosen
    if userInput.lower() == 'quit':
      break


  

  




