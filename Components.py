def nameCheck():
  name = ''
  while True:
    name = input('Enter Your Name \n')
    if ((len(name) > 16) or (len(name) < 0)): #name must be smaller than 15 characters and bigger than zero characters
      print ('Enter a name which is shorter than 15 characters')

    elif (len(name) > 0): #if name fits the criteria break the loop
      print('Welcome ' + name + ' !!! \n')
      break

    else: #if the user does not enter a name
      print('Please make sure that you are entering a name') 
      name = input('Enter Your Name to Start \n')


def checkInps(Input): #checks to see if the input is valid and if not return an invalid string
  if (Input.lower() == 'rock') or (Input.lower() == 'paper') or (Input.lower() == 'scissors') or (Input.lower() == 'quit') or (Input.lower() == 'score'):
    return 'valid'

  else:
    return 'Invalid Input'


def Instructions(): #prints the instructions for the game
  print('Let\'s begin the game \n Game rules: Each win gets you one point, choose one of the objects and enter their name. \n  Remember: \n   A rock beats a scissor \n   A paper beats a rock \n   A scissor beats a paper \n')
  print('Type \'Quit\' if you wish to quit the game \n')
  print('To view your points enter score')