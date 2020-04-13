class Point:
  def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

	def getX(self):
		return self.x

	def getY(self):
		return self.y

