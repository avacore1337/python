class FiveInRow(object):
	"""docstring for FiveInRow"""
	def __init__(self):
		super(FiveInRow, self).__init__()
		self.data = []
		self.NumberOfRows = 0
		self.NumberOfColumns = 0
		
	def loadData(self):
		with open("data5.txt") as f:
			self.data = f.read().split("\n")
			self.NumberOfColumns = len(self.data[0])
			self.NumberOfRows = len(self.data)

	def checkHorisontal(self,symbol):
		ret = False
		for x in self.data:
			ret |= self.checkFiveInRow(x,symbol)
		return ret

	def checkVertical(self,symbol):
		ret = False
		for x in range(self.NumberOfColumns):
			tempList = []
			for y in range(self.NumberOfRows):
				tempList.append(self.data[y][x])
			ret |= self.checkFiveInRow(tempList,symbol)
		return ret

	def checkDiagonal(self,symbol):
		ret = False
		for x in range(self.NumberOfRows - 4):
			for y in range(self.NumberOfColumns - 4):
				forwardList = []
				backwardList = []	
				for z in range(5):
					forwardList.append(self.data[x+z][y+z])
					backwardList.append(self.data[-x-z-1][y+z])
				ret |= self.checkFiveInRow(forwardList,symbol)
				ret |= self.checkFiveInRow(backwardList,symbol)
		return ret

	def checkFiveInRow(self,theList,symbol):
		count = 0
		for x in theList:
			if count > 4:
				return True
			if x == symbol:
				count += 1
			else:
				count = 0
		if count > 4:
			return True
		else:
			return False

	def __str__(self):
		return str(self.data) + "\n NumberOfRows: " + str(self.NumberOfRows) + "\n NumberOfColumns: " + str(self.NumberOfColumns)

