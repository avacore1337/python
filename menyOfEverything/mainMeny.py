
import string
from StringManager import StringManager
from FiveInRow import FiveInRow

def main2():
	workingText = readFile("randomText.txt")
	stringManager = StringManager(workingText)
	print(stringManager)


def main():
	menuChoise = {	1:readFile,
					2:makeIntoLists,
					3:nameTheFuntionToCall,
					4:fiveInRow}
	for x in menuChoise.keys():
		tmp = str(menuChoise[x]).split()
		print(str(x) + ":", tmp[1])
	data = input("What should be run?")
	#data = 4
	menuChoise[data]()

def readFile(fileName):
	randomText = ""
	with open(fileName) as textFile:
		randomText = textFile.read()
		print(randomText)
	return randomText

def makeIntoLists():
	print("two")

def nameTheFuntionToCall():
	theText = "makeIntoLists"
	globals()[theText]()
	#getattr(self,theText)()
	print(locals())

def fiveInRow():
	fiveInRow = FiveInRow()
	fiveInRow.loadData()
	print(fiveInRow.checkVertical("a"))
	print(fiveInRow.checkHorisontal("x"))
	print(fiveInRow.checkDiagonal("n"))

main()





