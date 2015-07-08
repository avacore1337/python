

def fun(numbers, build):
	if(numbers):
		for char in ["+","","-"]:
			tmp = build + char + numbers[0]
			fun(numbers[1:], tmp)
	elif(eval(build) == 100):
		print(build)
		
def printTheNumbers():
	fun("23456789","1")
