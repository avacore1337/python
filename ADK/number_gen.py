import random
def main():
	size = 5000
	matrix = []
	for x in range(size):
		matrix.append([random.randint(1,100) for x in range(size)])
	# print(matrix)
	f = open("matrix_data.txt", "w")
	for row in matrix:
		string = ""
		for element in row:
			string += str(element) + " "
		f.write(string[:-1])
		f.write("\n")
main()

