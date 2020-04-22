class Point:
	# __init__: Initialise with x and y coordinates of Elliptic curve point
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# __str__: Allows Point objects to be printed intuitively
	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	# __eq__: Allows Point objects to be compared
	def __eq__(self, other):
		return self.getX() == other.getX() and self.getY() == other.getY()

	# getX: Return x coordinate of Elliptic curve point
	def getX(self):
		return self.x

	# getY: Return y coordinate of Elliptic curve point
	def getY(self):
		return self.y
