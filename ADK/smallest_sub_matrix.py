def main():
	matrix = readmatrix()
	# print(matrix)
	average = getaverage(matrix)
	print(average)
	heavyMatrix = getHeavyMatrix(matrix,average)
	# for x in heavyMatrix:
	# 	print(x)
	summmedMatrix = getSummedMatrix(heavyMatrix)
	# for x in summmedMatrix:
	# 	print(x)
	row, column = findBiggestSubmatrix(summmedMatrix)
	print("row: ", row + 1, ", column: ", column + 1)

def findBiggestSubmatrix(summmedMatrix):
	biggest = 0
	bigx = 0
	bigy = 0
	size = len(summmedMatrix)
	for i in range(size):
		for j in range(size):
			if summmedMatrix[i][j] > biggest:
				biggest = summmedMatrix[i][j]
				bigx = i
				bigy = j
	return bigx, bigy

def getSummedMatrix(heavyMatrix):
	newmatrix = sumRows(heavyMatrix)
	# print("------------------------------")
	# for x in newmatrix:
	# 	print(x)
	newmatrix = transpose(newmatrix)
	# print("------------------------------")
	# for x in newmatrix:
	# 	print(x)
	newmatrix = sumRows(newmatrix)
	# print("------------------------------")
	# for x in newmatrix:
	# 	print(x)
	# print("------------------------------")
	return transpose(newmatrix)
		
def sumRows(matrix):
	newmatrix = []
	n = int(len(matrix[0])/2)
	for row in matrix:
		nRow = []
		total = 0
		for j in range(n):
			total += row[j]
		nRow.append(total)
		for i in range(n):
			total -= row[i]
			total += row[i+n]
			nRow.append(total)
		newmatrix.append(nRow)
	return newmatrix

def transpose(matrix):
	return [list(i) for i in zip(*matrix)]

def getHeavyMatrix(matrix, average):
	for x in matrix:
		for i in range(len(x)):
			if x[i] > average:
				x[i] = 1
			else:
				x[i] = 0
	return matrix

def getaverage(matrix):
	total = 0
	for x in matrix:
		for y in x:
			total += y
	total = total/len(matrix)
	total = total/len(matrix)
	return total

def readmatrix():
	f = open("matrix_data.txt")
	rows = f.read().split("\n")
	while rows[-1] == "":
		rows.pop()
	for rowNumber in range(len(rows)):
		list = []
		for element in rows[rowNumber].split(" "):
			list.append(int(element))
		rows[rowNumber] = list
	return rows
main()