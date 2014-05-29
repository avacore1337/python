class Node(object):

    EMPTY = ' '
    WALL = '#'
    PLAYER = '@'
    EMPTYGOAL = '.'
    PLAYERONGOAL = '+'
    BOX = '$'
    BOXONGOAL = '*'

    def __init__(self):
        self.value = self.EMPTY
    
    def isEmpty(self):
        return self.value in (self.EMPTY, self.EMPTYGOAL)    

    def isGoal(self):
        return self.value in (self.BOXONGOAL, self.EMPTYGOAL, self.PLAYERONGOAL)

    def isBox(self):
        return self.value in (self.BOXONGOAL,self.BOX)

    def isPlayer(self):
        return self.value in (self.PLAYER,self.PLAYERONGOAL)

    def setEmpty(self):
        if self.isGoal():
            self.value = self.EMPTYGOAL
        else:
            self.value = self.EMPTY

    def setPlayer(self):
        if self.isGoal():
            self.value = self.PLAYERONGOAL
        else:
            self.value = self.PLAYER

    def setBox(self):
        if self.isGoal():
            self.value = self.BOXONGOAL
        else:
            self.value = self.BOX



