class MasterMind(object):
	"""This is the main logical class for the MasterMind game"""
	def __init__(self):
		self.dict1 = {}
		self.generateNumberList()

	def generateNumberList(self):
		self.numberList = [str(a) + str(b) + str(c) + str(d) 
		for a in range(10) for b in range(10) for c in range(10) for d in range(10) 
		if a not in [b,c,d] and b not in [c,d] and c != d]

	def getAnswer(self):
		correct = False
		guess = ""
		while not(correct):
			correct = True
			guess = self.numberList.pop()
			for x in self.dict1.keys():
				value = self.compare(x,guess)
				if self.dict1[x] != value:
					correct = False
		return guess


	def calculateValue(self,text):
		total = 0
		for x in text:
			if x == "r":
				total += 10
			elif x == "f":
				total += 1
			else:
				total = -999
		return total

	def compare(self,string1,string2):
		total = 0
		for x in range(len(string1)):
			if string1[x] == string2[x]:
				total += 10
			elif string1[x] in string2:
				total += 1
		return total


def main():
	masterMind = MasterMind()
	printWelcomeMenu()
	answer = ""
	while answer != "rrrr":
		guess = masterMind.getAnswer()
		answer = getPlayerAnswer(guess).lower()
		value = masterMind.calculateValue(answer)
		print(value)
		while value < 0:
			printErrormMessage()
			answer = getPlayerAnswer(guess).lower()
			value = masterMind.calculateValue(answer)
		masterMind.dict1[guess] = value


def printWelcomeMenu():
	print("This is the mastermind game, hope you will enjoy it")
	print("Please write an 'r' for every character that match in both position and existance")
	print("Please write an 'f' for every character that only exist but are in the wrong position")

def printAnswer(answer):
	print("Is this the number?", answer)

def getPlayerAnswer(guess):
	printAnswer(guess)
	return input("reply: ").lower()

main()
		