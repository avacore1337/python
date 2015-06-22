from Node import Node


class Board(object):
    def __init__(self):
        mapData = self.readfile()
        mapData = self.removeEmptyLines(mapData)
        self.numberOfRows, self.numberOfColumns = self.getMapSizeInfo(mapData)
        self.nodes = []
        self.createLogicalBoardNodes()
        self.applyFileInfo(mapData)

    def readfile(self):
        file = open("map")
        mapData = file.read().split("\n")
        return mapData

    def removeEmptyLines(self, mapData):
        return [x for x in mapData if x != ""]

    def createLogicalBoardNodes(self,):
        for x in range(self.numberOfRows):
            self.nodes.append([])
            for y in range(self.numberOfColumns):
                self.nodes[x].append(Node())

    def applyFileInfo(self, mapData):
        for row in range(self.numberOfRows):
            for column in range(len(mapData[row])):
                self.nodes[row][column].value = mapData[row][column]

    def getMapSizeInfo(self, mapData):
        longestRow = 0
        numberOfRows = 0
        for row in mapData:
            numberOfRows += 1
            if len(row) > longestRow:
                longestRow = len(row)
        return numberOfRows, longestRow

    def dostuff(self, x, y):
        self.clickedNode = self.nodes[x][y]
        if self.clickedNode.isEmpty():
            self.moveToPosition(x, y)
        elif self.clickedNode.isBox():
            self.pushFromPosition(x, y)

    def moveToPosition(self, x, y):
        downNode = self.nodes[x][y-1]
        uppNode = self.nodes[x][y+1]
        leftNode = self.nodes[x-1][y]
        rightNode = self.nodes[x+1][y]
        self.checkIfPlayerIsAdjesent(downNode)
        self.checkIfPlayerIsAdjesent(uppNode)
        self.checkIfPlayerIsAdjesent(leftNode)
        self.checkIfPlayerIsAdjesent(rightNode)

    def checkIfPlayerIsAdjesent(self, potentialPlayerOriginNode):
        if potentialPlayerOriginNode.isPlayer():
            self.movePlayer(potentialPlayerOriginNode)

    def movePlayer(self, playerOriginNode):
        self.clickedNode.setPlayer()
        playerOriginNode.setEmpty()

    def pushFromPosition(self, x, y):
        uppNode = self.nodes[x][y-1]
        downNode = self.nodes[x][y+1]
        leftNode = self.nodes[x-1][y]
        rightNode = self.nodes[x+1][y]
        self.tryToPush(uppNode, downNode)
        self.tryToPush(downNode, uppNode)
        self.tryToPush(leftNode, rightNode)
        self.tryToPush(rightNode, leftNode)

    def tryToPush(self, targetNode, playerOriginNode):
        if (targetNode.isEmpty() and playerOriginNode.isPlayer()):
            targetNode.setBox()
            playerOriginNode.setEmpty()
            self.clickedNode.setPlayer()
