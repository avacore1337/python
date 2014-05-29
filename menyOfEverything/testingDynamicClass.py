class Vehicle(object):
	"""docstring for Vehicle"""
	def __init__(self, price, color, speed):
		super(Vehicle, self).__init__()
		self.price = price
		self.color = color
		self.speed = speed
		

class Car(Vehicle):
	"""docstring for Car"""
	def __init__(self, color,price,speed, passengers = 4):
		super(Car, self).__init__(price,color,speed)
		self.passengers = passengers

	def __str__(self):
		return self.color + " " + str(self.price)

class Bike(Vehicle):
	"""docstring for Bike"""
	def __init__(self, color,price,speed):
		super(Bike, self).__init__(price,color,speed)
		self.text = "hej"

	def __str__(self):
		return self.color + " " + str(self.price)

	def getValue(self):
		return self.text

	def printGeneric(self):
		const = globals()["Bike"]
		func = getattr(const,"text")
		print(func)
		print("works")



def main():
	string1 = "Car"
	string2 = "Bike"
	const = globals()[string2]
	print(const("red", 666,100))
	bike = Bike(666,"yellow",55)
	bike.printGeneric()


main()