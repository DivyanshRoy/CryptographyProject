import random
from Point import Point

class Helper:
	def __init__(self):
		self.asciiToPoint = {}
		self.pointToAscii = {}

	def getSegmentSize(self, m):
		numPoints = ((m ** 2) + 1)
		size = 0
		while (numPoints != 0):
			numPoints //= 26
			size += 1
		return size

	def generateCharacterPointMappings(self, curvePoints):
		numPoints = len(curvePoints)
		maxMappings = min(numPoints, 2 ** 16)

		asciiCodes = []
		for i in range(0, maxMappings):
			asciiCodes.append(i)
		random.shuffle(asciiCodes)

		asciiToPoint = {}
		pointToAscii = {}
		sno = 0

		for asciiCode in asciiCodes:
			p = curvePoints[sno]
			p = (p.getX(), p.getY())
			pointToAscii[p] = asciiCode
			asciiToPoint[asciiCode] = p
			sno += 1

		self.asciiToPoint = asciiToPoint
		self.pointToAscii = pointToAscii

	def charToPoint(self, c):
		p = self.asciiToPoint[ord(c)]
		p = Point(p[0], p[1])
		return p

	def pointToChar(self, p):
		p = (p.getX(), p.getY())
		return chr(self.pointToAscii[p])

	def streamToPoint(self, stream, m):
		segmentSize = self.getSegmentSize(m)
		v = []
		i = 0

		while i < len(stream):
			temp = stream[i:i+segmentSize]
			val = 0
			for j in range(0, len(temp)):
				d = ord(temp[j]) - ord('a')
				val = (val * 26) + d

			p = Point(val // m, val % m)
			v.append(p)
			i += segmentSize

		return v

	def pointToStream(self, p, m):
		stream = ""
		temp = ""
		segmentSize = self.getSegmentSize(m)
		val = (p.getX() * m) + p.getY()
	
		for i in range(0, segmentSize):
			temp += chr(ord('a') + (int(val) % 26))
			val /= 26
			if val < 1:
				break

		while i >= 0:
			stream += temp[i]
			i -= 1

		return stream

	def randomPoint(self, curvePoints):
		numPoints = len(curvePoints)
		r = random.randint(0, numPoints - 1)
		return curvePoints[r]

	def randomNumber(self, m):
		return random.randint(0, m - 2) + 1

	def modulus(self, l, m):
		while l < 0:
			l += m
		l %= m
		return l

