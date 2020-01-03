class PointCounter():
  def __init__(self):
    self.__userPoints = 0
    self.__compPoints = 0

  def getUserPoints(self):
    return str(self.__userPoints)

  def getCompPoints(self):
    return str(self.__compPoints)

  def incUserPoints(self):
    self.__userPoints += 1

  def incCompPoints(self):
    self.__compPoints += 1

  def winner(self):
    if self.__compPoints == self.__userPoints:
      return ('It is a Draw. Both were equally good')
    else:
      winner = {self.__compPoints : 'Computer', self.__userPoints : 'User'}
      return winner.get(max(winner)) + ' wins!!!!'
    
  