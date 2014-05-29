import string

class StringManager(object):
	"""docstring for StringManager"""
	def __init__(self, text):
		super(StringManager, self).__init__()
		self.text = text
		self.wordList = []
		self.specList = []
		self.wordBuffer = ""
		self.specBuffer = ""
		self.splitLists()
		self.readExceptionsfromFile()
		self.countOccurances()

	def splitLists(self):
		for x in self.text:
			if x in (string.ascii_letters + "'"):
				self.wordBuffer += x
				if self.specBuffer != "":
					self.specList.append(self.specBuffer)
					self.specBuffer = ""
			else:
				self.specBuffer += x
				if self.wordBuffer != "":
					self.wordList.append(self.wordBuffer)
					self.wordBuffer = ""
		self.appendLastItems()

	def appendLastItems(self):
		if self.wordBuffer != "":
			self.wordList.append(self.wordBuffer)
			self.wordBuffer = ""	
		if self.specBuffer != "":
			self.specList.append(self.specBuffer)
			self.specBuffer = ""	

	def readExceptionsfromFile(self):
		self.exceptionList = open("exceptionsFromCounting.txt").read().split("\n")
		
	def countOccurances(self):
		self.dict1 = {}
		for x in self.wordList:
			if x not in self.dict1:
				if x not in self.exceptionList:
					self.dict1[x] = 1
			else:
				self.dict1[x] += 1

	def __str__(self):
		finalString = ""
		for index in range(len(self.wordList)):
			finalString += self.wordList[index] 
			if self.shouldItGetAppended(index):
				finalString += "(" + str(self.dict1[self.wordList[index]]) + ")"
			finalString += self.specList[index]
		return finalString

	def shouldItGetAppended(self,index):
		return self.wordList[index] in self.dict1 and self.dict1[self.wordList[index]] > 2