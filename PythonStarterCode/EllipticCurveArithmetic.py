from Point import Point
from Helper import Helper

class EllipticCurveArithmetic:
	'''
	__init__: Initialise an elliptic curve with Curve Parameters
    Curve Equation: y^2 = (x^3 + ax + b) modulo m
	'''
	def __init__(self, a, b, m):
		self.a = a
		self.b = b
		self.m = m

	# getM: Return m
	def getM(self):
		return self.m

	'''
	getCurvePoints: Generate curve points which follow the Elliptic Curve equation y^2 = (x^3 + ax + b) modulo m
    Output:-
        Return list of Elliptic curve points
	'''
	def getCurvePoints(self):
		mx = {}
		my = {}
		tmp = []

		for x in range(0, self.m):
			v = ((x ** 3) + (self.a * x) + self.b) % self.m
			if v in mx:
				tmp = mx[v]
				tmp.append(x)
				mx[v] = tmp
			else:
				mx[v] = [x]

		for y in range(0, self.m):
			v = (y ** 2) % self.m
			if v in my:
				tmp = my[v]
				tmp.append(y)
				my[v] = tmp
			else:
				my[v] = [y]

		points = [(0, 0)]

		vx = []
		vy = []
		for s in list(mx.keys()):
			if s in my:
				vx = mx[s]
				vy = my[s]

			for x1 in vx:
				for y1 in vy:
					if (x1, y1) not in points:
						points.append((x1, y1))

		hashedPoints = []
		for i in points:
			v = i[0]*self.m + i[1]
			hashedPoints.append(v)
		hashedPoints.sort()
		curvePoints = []
		for h in hashedPoints:
			x = h//self.m
			y = h%self.m
			curvePoints.append(Point(x,y))
		return curvePoints

	'''
	modInverse: Calculate the modular inverse of a with m as modulus
    Output:-
        Return a^-1 modulo m
	'''
	def modInverse(self, a, m, h):
		# Write your code below

		# Write your code above
		return

	'''
	add: Add 2 Elliptic curve points
    Input:-
        p1: Point 1
        p2: Point 2
    Output:-
        Return a Point which is the addition of p1 and p2 according to Elliptic curve arithmetic.
	'''
	def add(self, p1, p2, h):
		# Write your code below

		# Write your code above
		return

	'''
	addWithItself: Add a point to itself.
    Input:-
        p: Point p
    Output:-
        Return the sum of p and p using Elliptic curve arithmetic
	'''
	def addWithItself(self, p, h):
		# Write your code below

		# Write your code above
		return

	'''
	multiply: Multiply a Point with a scalar number
    Input:-
        p: Point p
        l: Scalar to be used for multiplication
    Output:-
        Return the multiplication of p with l.
        Hint: Multiplication is just repeated addition.
        Challenge: Make this operation O(log(l)) instead of O(l).
	'''
	def multiply(self, p, l, h):
		# Write your code below

		# Write your code above
		return

	'''
	subtract: Return the difference between 2 curve points
    Input:-
        p1: Point p1
        p2: Point p2
    Output:-
        Return difference of p1 and p2.
	'''
	def subtract(self, p1, p2, h):
		p3 = Point(p2.getX(), self.m - p2.getY())
		return self.add(p1, p3, h)
