from Point import Point
from Helper import Helper

class EllipticCurve:
	def __init__(self, a, b, m):
		self.a = a
		self.b = b
		self.m = m

	def getM(self):
		return self.m

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

		curvePoints = []
		for i in points:
			curvePoints.append(Point(i[0], i[1]))

		return curvePoints

	def modInverse(self, a, m, h):
		a = h.modulus(a, m)
		a %= m
		for x in range(1, m):
			if (a * x) % m == 1:
				return x
		return x

	def add(self, p1, p2, h):
		x1 = p1.getX()
		y1 = p1.getY()
		x2 = p2.getX()
		y2 = p2.getY()

		if x1 == 0 and y1 == 0:
			return p2
		if x2 == 0 and y1 == 0:
			return p1

		if x1 == x2:
			if y1 == y2:
				return self.addWithItself(p1, h)
			if y1 == self.m - y2:
				return Point(0, 0)

		n = h.modulus(y2 - y1, self.m)
		d = h.modulus(x2 - x1, self.m)
		d = self.modInverse(d, self.m, h)
		s = h.modulus(d * n, self.m)

		x3 = h.modulus((s * s) - x1 - x2, self.m)
		y3 = h.modulus((s * (x1 - x3)) - y1, self.m)
		return Point(x3, y3)

	def addWithItself(self, p, h):
		x = p.getX()
		y = p.getY()

		if y == 0:
			return Point(0, 0)

		s = h.modulus((3 * (x ** 2)) + self.a, self.m)
		d = 2 * y
		d = h.modulus(self.modInverse(h.modulus(d, self.m), self.m, h), self.m)
		s = h.modulus(s * d, self.m)
		xd = h.modulus((s ** 2) - (2 * x), self.m)
		yd = h.modulus((s * (x - xd) - y), self.m)
		
		return Point(xd, yd)	

	def multiply(self, p, l, h):
		if l == 1:
			return p
		
		halfMultiply = self.multiply(p, l // 2, h)
		ans = self.addWithItself(halfMultiply, h)

		if l % 2 == 1:
			ans = self.add(ans, p, h)

		return ans

	def subtract(self, p1, p2, h):
		p3 = Point(p2.getX(), self.m - p2.getY())
		return self.add(p1, p3, h)

